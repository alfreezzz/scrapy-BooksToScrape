# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import requests


class AllProductsSpider(CrawlSpider):
    name = 'all_products'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']
    base_url = 'http://books.toscrape.com/'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ol/li/article/h3/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )


    def parse_item(self, response):
        category = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        title = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()

        relative_image = response.xpath('//div[@class="item active"]/img/@src').extract_first()
        final_image = self.base_url + relative_image.replace('../..', '')

        # yield {"image": final_image}
        print(final_image)


        # url = 'https://www.facebook.com/favicon.ico'
        # for link in final_image:
        # #     r = requests.get(link, allow_redirects=True)

        # #     open(str(link) + '.ico', 'wb').write(r.content)
        
        # # url = 'http://books.toscrape.com//media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg'
        #     r = requests.get(link, allow_redirects=True)

        #     open(str(final_image.index(link)) + '.jpg', 'wb').write(r.content)


        # Get Stock
        # in_stock = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        # stock = in_stock.split("(")[1].split()[0]

        # # Get rating
        # rating = response.xpath("//p[contains(@class, 'star-rating')]/@class").get().split()[1]
        # if rating.lower() == "one":
        #     rating = 1
        # elif rating.lower() == "two":
        #     rating = 2
        # elif rating.lower() == "three":
        #     rating = 3
        # elif rating.lower() == "four":
        #     rating = 4
        # elif rating.lower() == "five":
        #     rating = 5

        # description = response.xpath("//article[@class='product_page']/p/text()").extract()
        # upc = response.xpath("//table[@class='table table-striped']/tr[1]/td/text()").get()
        # product_type = response.xpath("//table[@class='table table-striped']/tr[2]/td/text()").get()
        # price_excl_tax = response.xpath("//table[@class='table table-striped']/tr[3]/td/text()").get()
        # price_incl_tax = response.xpath("//table[@class='table table-striped']/tr[4]/td/text()").get()
        # tax = response.xpath("//table[@class='table table-striped']/tr[5]/td/text()").get()
        # number_of_reviews = response.xpath("//table[@class='table table-striped']/tr[7]/td/text()").get()

        # yield {
        #     "category": category,
        #     "title": title,
        #     "image": final_image,
        #     "stock": stock,
        #     "rating": rating,
        #     "description": description,
        #     "upc": upc,
        #     "product_type": product_type,
        #     "price_excl_tax": price_excl_tax,
        #     "price_incl_tax": price_incl_tax,
        #     "tax": tax,
        #     "number_of_reviews": number_of_reviews,
        # }