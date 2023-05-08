# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CriterionMovieItem(scrapy.Item):
    page_url = scrapy.Field()  # url of the movie page
    spine = scrapy.Field()  # spine number
    thumb_url = scrapy.Field()  # url of the thumbnail [small size]
    movie = scrapy.Field()  # title of the movie
    director = scrapy.Field()
    country = scrapy.Field()  # can be multiple countries
    year = scrapy.Field()  # is in YYYY format
    isBluRay_available = scrapy.Field()  # True or False
    BluRay_price = scrapy.Field()  # is in dollars
    isDVD_available = scrapy.Field()  # True or False
    DVD_price = scrapy.Field()  # is in dollars
    runtime = scrapy.Field()  # is in minutes
    isColor = scrapy.Field()
    aspect_ratio = scrapy.Field()
    language = scrapy.Field()
    poster_url = scrapy.Field()  # url of the poster [large size]
    media_type = scrapy.Field()  # can be film or boxset
