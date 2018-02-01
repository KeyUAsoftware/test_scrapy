# -*- coding: utf-8 -*-
import scrapy
from houzz.items import HouzzItem
from scrapy import Request
from scrapy.loader import ItemLoader


class HouzzSpiderSpider(scrapy.Spider):
    name = 'houzz_spider'
    allowed_domains = ['www.houzz.jp']
    start_urls = ['https://www.houzz.jp/professionals/p/{0}'.format(str(x)) for x in range(15, 5000, 15)]

    def parse(self, response):
        profiles = response.xpath('//div[contains(@class, "pro-card")]')
        for profile in profiles:
            item = HouzzItem()
            link_to_profile = profile.xpath('.//div[@class="name-info"]/a')
            item['company_name'] = link_to_profile.xpath('./text()').extract_first()
            item['profile_url'] = link_to_profile.xpath('./@href').extract_first()
            item['phone_number'] = profile.xpath(
                './/span[@class="pro-list-item--text"]/text()').extract_first()

            yield Request(url=item['profile_url'], meta={'item': item}, callback=self.parse_profile)

    def parse_profile(self, response):
        item = response.meta['item']
        l = ItemLoader(item=item, response=response)

        l.add_xpath('website', '//a[@class="proWebsiteLink"]/@href')
        l.add_xpath('category', '//span[@itemprop="child"]/a/span[@itemprop="title"]/text()')
        l.add_xpath('pro_rating', '//meta[@itemprop="ratingValue"]/@content')

        additional_info = response.xpath('//div[@class="info-list-text"]')

        contact_name = response.xpath('//div[@class="info-list-label"]/i[contains(@class, "hzi-Man-Outline")]/'
                                      'following-sibling::div/text()').extract_first()

        postal_code = additional_info.xpath('.//span[@itemprop="postalCode"]/text()').extract_first()
        prefecture = additional_info.xpath('.//span[@itemprop="addressRegion"]/text()').extract_first()
        city = additional_info.xpath('.//span[@itemprop="addressLocality"]/a/text()').extract_first()
        street = additional_info.xpath('.//span[@itemprop="streetAddress"]/text()').extract_first()
        service_cost = response.xpath(
            '//div[@class="info-list-label"]/i[contains(@class, "hzi-Cost-Estimate")]/'
            'following-sibling::div/span/text()').extract_first()

        number_of_projects_done = response.xpath('//div[@class="project-section"]/div/a/text()').re_first('(\d+)')
        number_of_reviews = response.xpath('//div[@class="review-section"]/div/a/text()').re_first('(\d+)')

        l.add_value('contact_name', contact_name)
        l.add_value('postal_code', postal_code)
        l.add_value('prefecture', prefecture)
        l.add_value('city', city)
        l.add_value('street', street)
        l.add_value('service_cost', service_cost)
        l.add_value('number_of_projects_done', number_of_projects_done)
        l.add_value('number_of_reviews', number_of_reviews)

        return l.load_item()
