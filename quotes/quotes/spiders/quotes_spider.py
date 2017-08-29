from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from quotes.items import QuotesItem


class QuotesSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = (
        Rule(LinkExtractor(allow='quotes.toscrape.com/page'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log('Scraping: ' + response.url)

        articles = response.css('.quote')

        for article in articles:
            item = QuotesItem()
            item['text'] = article.css('::text').extract()[1].strip()
            item['author'] = article.css('::text').extract()[4].strip()

            yield item
