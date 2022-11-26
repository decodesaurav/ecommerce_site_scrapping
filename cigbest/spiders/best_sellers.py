# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.cigbest.com/collections/best-sellers']
    start_urls = ['http://www.cigbest.com/collections/best-sellers/']

    def parse(self, response):
        pass
