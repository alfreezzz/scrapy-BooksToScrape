# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllProductsSpider(CrawlSpider):
    name = 'all_products'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ol/li/article/h3/a'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        title = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        
        # Get Stock
        in_stock = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        stock = in_stock.split("(")[1].split()[0]

        # Get rating
        rating = response.xpath("//p[contains(@class, 'star-rating')]/@class").get().split()[1]
        if rating.lower() == "one":
            rating = 1
        elif rating.lower() == "two":
            rating = 2
        elif rating.lower() == "three":
            rating = 3
        elif rating.lower() == "four":
            rating = 4
        elif rating.lower() == "five":
            rating = 5

        price = response.xpath("//p[@class='price_color']/text()").get()

        yield {
            "title": title,
            "stock": stock,
            "rating": rating,
            "price": price,
        }
