# -*- coding: utf-8 -*-

from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst


class HouzzItem(Item):
    category = Field(output_processor=TakeFirst())
    contact_name = Field(output_processor=TakeFirst())

    # ---Address---
    street = Field(output_processor=TakeFirst())
    city = Field(output_processor=TakeFirst())
    prefecture = Field(output_processor=TakeFirst())
    postal_code = Field(output_processor=TakeFirst())
    # --- ---

    # GEO: Lon, Lat
    geo = Field()

    company_name = Field(output_processor=TakeFirst())
    service_cost = Field(output_processor=TakeFirst())
    number_of_reviews = Field(output_processor=TakeFirst())
    number_of_projects_done = Field(output_processor=TakeFirst())
    website = Field(output_processor=TakeFirst())
    email = Field(output_processor=TakeFirst())
    profile_url = Field(output_processor=TakeFirst())
    phone_number = Field(output_processor=TakeFirst())
    pro_rating = Field(output_processor=TakeFirst())
