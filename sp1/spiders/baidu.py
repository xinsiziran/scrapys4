# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        content_html=BeautifulSoup(response.text,"html.parser")
        obj_html=content_html.find(id='lg').find('img')
        htm_jpg=obj_html.get('src')
        print(htm_jpg)