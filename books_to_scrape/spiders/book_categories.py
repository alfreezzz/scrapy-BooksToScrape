# -*- coding: utf-8 -*-
import scrapy


class BookCategoriesSpider(scrapy.Spider):
    name = 'book_categories'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    def parse(self, response):
        all_categories = response.xpath("//div[@class='side_categories']/ul/li/ul/li")

        for category in all_categories:
            category_name = category.xpath("normalize-space(.//a/text())").get()
            category_url = category.xpath(".//a/@href").get()

            yield response.follow(url=category_url, callback=self.parse_books,
                                meta={"category_name":category_name})

    def parse_books(self, response):
        category_name = response.request.meta["category_name"]

        all_books = response.xpath("//article[@class='product_pod']")
        book_info = []
        for book in all_books:
            book_url = book.xpath(".//div/a/@href").get()
            book_title = book.xpath(".//div/a/img/@alt").get()
            book_rate = book.xpath(".//p/@class").get().split()[1]
            book_price = book.xpath(".//div[@class='product_price']/p[@class='price_color']/text()").get()

            book_info.append({
                "book_title": book_title,
                "book_url": response.urljoin(book_url),
                "book_rate": book_rate,
                "book_price": book_price
            })
            
        yield {
            "category_name": category_name,
            "data": book_info
        }
