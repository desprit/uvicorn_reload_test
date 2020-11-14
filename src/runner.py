"""
Taken from official docs:
https://scrapy-gallaecio.readthedocs.io/en/latest/topics/practices.html
"""
import os

from typing import Optional, List

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings


os.environ["SCRAPY_SETTINGS_MODULE"] = "settings"


class CrawlerScript:
    """
    This class is used to programmatically init and run spiders.
    """

    def __init__(self):
        print("Initializing CrawlerScript...")
        self.runner = CrawlerRunner(get_project_settings())

    def crawl(self) -> list:
        """
        Use billiard Process to get around of `ReactorNotRestartable`
        issue in the Twisted framework.
        """

        print("CrawlerScript.crawl started")
        d = self.runner.crawl("test_spider")
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        print("CrawlerScript.crawl finished")
        return []


def run_spider() -> dict:
    """
    Launch Scrapy spider.
    """

    crawler = CrawlerScript()
    result = crawler.crawl()
    return {"status": "success", "results": result}
