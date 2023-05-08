from itemloaders.processors import TakeFirst, MapCompose, Identity
from scrapy.loader import ItemLoader


class CriterionMovieLoader(ItemLoader):
    default_output_processor = TakeFirst()

    page_url_in = MapCompose(str.strip)
    spine_in = MapCompose(str.strip)  # strip and convert to int
    thumb_url_in = MapCompose(str.strip)
    movie_in = MapCompose(str.strip)
    director_in = MapCompose(str.strip)
    country_in = MapCompose(str.strip)
    year_in = MapCompose()

    # isBluRay_available_in = MapCompose(lambda v: bool(v))
    # BluRay_price_in = MapCompose(lambda v: float(v) if "Print" not in v else v)
    # isDVD_available_in = MapCompose(lambda v: bool(v))
    # DVD_price_in = MapCompose(lambda v: float(v) if "Print" not in v else v)

    runtime_in = MapCompose(int)  # strip and convert to int
    isColor_in = MapCompose(str.strip)
    aspect_ratio_in = MapCompose(str.strip)
    language_in = MapCompose(str.strip)
    poster_url_in = MapCompose(str.strip)
    media_type_in = MapCompose(str.strip)
