import scrapy
import json


class HttpbinIpCrawlerSpider(scrapy.Spider):
    name = "httpbin-ip-crawler"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/ip"]

    def parse(self, response):
        payload = json.loads(response.body)
        yield (payload)
