# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllProductsSpider(CrawlSpider):
    name = 'advanced'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=["//ol/li/article/h3/a", "//*/a[text()='music']"]), callback='parse_item', follow=True),   
    )


    def parse_item(self, response):
        category = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
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


        upc = response.xpath("//table[@class='table table-striped']/tr[1]/td/text()").get()
        product_type = response.xpath("//table[@class='table table-striped']/tr[2]/td/text()").get()
        price_excl_tax = response.xpath("//table[@class='table table-striped']/tr[3]/td/text()").get()
        price_incl_tax = response.xpath("//table[@class='table table-striped']/tr[4]/td/text()").get()
        tax = response.xpath("//table[@class='table table-striped']/tr[5]/td/text()").get()
        number_of_reviews = response.xpath("//table[@class='table table-striped']/tr[7]/td/text()").get()

        yield {
            "category": category,
            "title": title,
            "stock": stock,
            "rating": rating,
            "upc": upc,
            "product_type": product_type,
            "price_excl_tax": price_excl_tax,
            "price_incl_tax": price_incl_tax,
            "tax": tax,
            "number_of_reviews": number_of_reviews,
        }
