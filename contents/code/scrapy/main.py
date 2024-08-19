from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datawarehouse.spiders.topcv_crawler import TopcvCrawlerSpider


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(TopcvCrawlerSpider)
    process.start()


if __name__ == "__main__":
    main()
