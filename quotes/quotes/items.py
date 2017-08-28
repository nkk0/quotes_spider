import scrapy


class QuotesItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
