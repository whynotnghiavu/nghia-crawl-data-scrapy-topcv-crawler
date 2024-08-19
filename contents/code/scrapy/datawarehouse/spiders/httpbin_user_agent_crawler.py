import scrapy
import json


class HttpbinUserAgentCrawlerSpider(scrapy.Spider):
    name = "httpbin-user-agent-crawler"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/user-agent"]

    def parse(self, response):
        payload = json.loads(response.body)
        yield (payload)
