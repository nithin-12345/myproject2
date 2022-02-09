import scrapy
from ..items import BhhsambtutorialItem

class BhhsambTutorialSpider(scrapy.Spider):
    name = 'bhhsamb_tutorial'
    start_urls = ['https://www.bhhsamb.com/agents/74006-meg-wright']

    def parse(self, response):
        items = BhhsambtutorialItem()
        product_name = response.css('.body-title::text').extract()
        job_title = response.css('.big-text::text').extract()
        image_url = response.css('.agent-photo::attr(src)').extract()
        address = response.css('.non-link::text').extract()
        contact_details = response.css('.agent_email::text').extract()
        social_accounts = response.css('.social::text').extract()
        office = response.css('a::text').extract()
        languages = response.css('li::text').extract()
        description = response.css('.row p').css('::text').extract()


        items['product_name'] = product_name
        items['job_title'] = job_title
        items['image_url'] = image_url
        items['address'] = address
        items['contact_details'] = contact_details
        items['social_accounts'] = social_accounts
        items['office'] = office
        items['languages'] = languages
        items['description'] = description

        yield items
