# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from pcel_crawler.items import LaptopItem

class PcelSpider(scrapy.Spider):
    name = "pcel"
    allowed_domains = ["pcel.com"]
    start_urls = (
        'https://pcel.com/computadoras/laptops',
    )

    def parse(self, response):
        for product in response.xpath('//div[@class="product-list"]/table/tr[position() mod 2 = 1]'):
            laptop = LaptopItem()
            laptop['sku'] = ''.join(product.xpath('.//span[@class="price-tax" and contains(., "Sku: ")]/text()').re('Sku: (.*)'))
            laptop['model'] = ''.join(product.xpath('.//div[@class="name"]/a/text()[1]').extract()).strip()
            laptop['image'] = ''.join(product.xpath('.//div[@class="image"]/a/img/@src').extract())
            laptop['brand'] = ''.join(product.xpath('.//img[contains(@src, "manufacturer")]/@alt').extract())
            laptop['price'] = ''.join(product.xpath('.//div[@class="price"]/text()').re('[0-9.]'))
            laptop['new_price'] = ''.join(product.xpath('.//div[@class="price-new"]/text()').re('[0-9.]'))
            laptop['old_price'] = ''.join(product.xpath('.//div[@class="price-old"]/text()').re('[0-9.]'))
            yield laptop
        next_url = ''.join(response.xpath('//div[@class="links"]/a[text()=">"]/@href').extract())
        if next_url:
            yield Request(next_url, callback=self.parse)
