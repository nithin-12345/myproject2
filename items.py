# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itertools import product
import scrapy


class BhhsambtutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    job_title = scrapy.Field()
    image_url = scrapy.Field()
    address = scrapy.Field()
    contact_details = scrapy.Field()
    social_accounts = scrapy.Field()
    office = scrapy.Field()
    languages = scrapy.Field()
    description = scrapy.Field()










    pass
