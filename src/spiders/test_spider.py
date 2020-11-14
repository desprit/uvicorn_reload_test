from scrapy.spiders import Spider


class TestSpider(Spider):

    name = "test_spider"
    start_urls = ["https://www.wikipedia.org/"]

    def parse(self, response):
        print("TestSpider.parse started")