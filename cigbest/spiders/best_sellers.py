# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.cigbest.com']
    start_urls = ['https://www.cigbest.com/collections/best-sellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='product-list-item-list']/div/div[@class='col product-item-list']"):
            yield{
                'title': product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@data-name").get(),
                'url': response.urljoin(product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@href").get()),
                'discounted_price': product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@data-price").get(),
                'original_price': product.xpath(".//div[@class='product-item-price']/div/span[3]/@data-product-item-price").get()
            }
