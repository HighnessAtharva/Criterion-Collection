import scrapy
from criterion_scraper.itemloaders import CriterionMovieLoader
from criterion_scraper.items import CriterionMovieItem

class CollectionScraperSpider(scrapy.Spider):
    name = "collection_scraper"
    allowed_domains = ["www.criterion.com"]
    # start_urls = ["https://www.criterion.com/shop/browse/list"]
    start_urls = ["https://www.criterion.com/shop/browse/list?sort=spine_number&direction=desc"]
    


    def parse(self, response):    
        movies = response.xpath("//table[@id='gridview']//tbody/tr")
        
        for movie in movies:
                # configure the item loader
                criterion_movie = CriterionMovieLoader(item=CriterionMovieItem(), selector=movie)
                 
                # NOTE: Currently it only gets the spined releases, not the box sets
                
                # load the data 
                criterion_movie.add_xpath("page_url", ".//@data-href")
                criterion_movie.add_xpath("spine", ".//td[@class='g-spine']/text()")                
                criterion_movie.add_xpath("thumb_url", ".//td[@class='g-img']/img/@src")
                criterion_movie.add_xpath("movie", ".//td[@class='g-title']/span/text()")
                criterion_movie.add_xpath("director", ".//td[@class='g-director']/text()")
                criterion_movie.add_xpath("country", ".//td[@class='g-country']/text()")
                criterion_movie.add_xpath("year", ".//td[@class='g-year']/text()")
            
                # check if /film/ or /boxsets/ is in the url
                page_url = criterion_movie.get_output_value("page_url")
                if "/boxsets/" in page_url:
                    yield response.follow(
                        criterion_movie.get_output_value("page_url"),
                        callback=self.parse_boxset_page,
                        meta={"criterion_movie": criterion_movie.load_item()},           
                    )
                else:
                    yield response.follow(
                        criterion_movie.get_output_value("page_url"),
                        callback=self.parse_movie_page,
                        meta={"criterion_movie": criterion_movie.load_item()},           
                    )
    
    def parse_boxset_page(self, response):
        # TODO [OPTIONAL]
        pass
    
    def parse_movie_page(self, response):
        criterion_movie = CriterionMovieLoader(item=CriterionMovieItem(), response=response)
        criterion_movie.add_value("page_url", response.url)
        criterion_movie.add_value("spine", response.meta["criterion_movie"]["spine"])
        criterion_movie.add_value("thumb_url", response.meta["criterion_movie"]["thumb_url"])
        criterion_movie.add_value("movie", response.meta["criterion_movie"]["movie"])
        criterion_movie.add_value("director", response.meta["criterion_movie"]["director"])
        criterion_movie.add_value("country", response.meta["criterion_movie"]["country"])
        criterion_movie.add_value("year", response.meta["criterion_movie"]["year"])
        
        criterion_movie.add_value("isBluRay_available", False)
        criterion_movie.add_value("isDVD_available", False)
        criterion_movie.add_value("BluRay_price", None)
        criterion_movie.add_value("DVD_price", None)
        criterion_movie.add_value("runtime", None)
        criterion_movie.add_value("isColor", "")
        criterion_movie.add_value("aspect_ratio", "")
        criterion_movie.add_value("language", "")
        criterion_movie.add_value("poster_url", "")
        criterion_movie.add_value("media_type", "")
         
        # check if the movie is a boxset or a film 
        page_url = response.url
        if "/boxsets/" in page_url:
            criterion_movie.add_value("media_type", "boxset")
        else:
            criterion_movie.add_value("media_type", "film")

        if poster_url := response.xpath("//div[@class='product-box-art']/img/@src").get():
            criterion_movie.add_value("poster_url", poster_url)

        if runtime := response.xpath("//li/meta[@itemprop='duration']/following-sibling::text()").get():
            criterion_movie.add_value("runtime", runtime.replace(" minutes", ""))

        if isColor := response.xpath("//li[meta[@itemprop='duration']]/following-sibling::li[1]/text()").get():
            criterion_movie.add_value("isColor", isColor)

        if aspect_ratio := response.xpath("//li[meta[@itemprop='duration']]/following-sibling::li[2]/text()").get():
            criterion_movie.add_value("aspect_ratio", aspect_ratio)
            
        if language := response.xpath("//li[@itemprop='inLanguage']/span[@itemprop='name']/text()").get():
            criterion_movie.add_value("language", language)

        formats = response.xpath("//div[@class='purchase-option']")
        formats_list = []

        for f in formats:     
            format_name = f.xpath("./label/span[@class='meta-item']/span[@class='item']/text()").get()
            format_price = f.xpath("./label/span[@class='meta-prices']/span[@class='item-price']/text()").get().replace("$", "")
            formats_list.append((format_name, format_price))


        for format_name, format_price in formats_list:
            if format_name == "Blu-Ray":
                criterion_movie.add_value("isBluRay_available", True)
                criterion_movie.add_value("BluRay_price", format_price)
                
            if format_name == "DVD":
                criterion_movie.add_value("isDVD_available", True)
                criterion_movie.add_value("DVD_price", format_price)
            
        yield criterion_movie.load_item()

        
