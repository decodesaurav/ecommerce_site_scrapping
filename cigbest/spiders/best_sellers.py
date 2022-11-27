# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.cigbest.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.cigbest.com/collections/best-sellers', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath("//div[@class='product-list-item-list']/div/div[@class='col product-item-list']"):
            yield{
                'title': product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@data-name").get(),
                'url': response.urljoin(product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@href").get()),
                'discounted_price': product.xpath(".//div[@class='product-item__wrapper shopline-element-product-item']/div/a/@data-price").get(),
                'original_price': product.xpath(".//div[@class='product-item-price']/div/span[3]/@data-product-item-price").get()
            }

        next_page = response.urljoin(response.xpath(
            "//span[@class='pagination_next pagination_item']/a/@href").get())

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
            })
