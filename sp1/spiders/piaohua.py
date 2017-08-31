# -*- coding: utf-8 -*-
import scrapy


class PiaohuaSpider(scrapy.Spider):
    name = 'piaohua'
    allowed_domains = ['www.piaohua.com']
    start_urls = ['http://www.piaohua.com/']

    def parse(self, response):
        pass
