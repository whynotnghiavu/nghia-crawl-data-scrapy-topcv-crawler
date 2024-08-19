import scrapy
from scrapy.loader import ItemLoader
from ..items import TopCVItem
from ..format import remove_query_url


class TopcvCrawlerSpider(scrapy.Spider):
    name = "topcv-crawler"
    allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://www.topcv.vn/tim-viec-lam-moi-nhat"]

    def parse(self, response):

        jobs = response.xpath("//div[contains(@class,'job-item-search-result')]")
        for job in jobs:
            job_url = job.xpath(".//h3[contains(@class,'title')]//@href").extract_first()
            # updated_at = job.xpath(".//label[contains(@class,'mobile-hidden')][2]").extract_first()

            if "https://www.topcv.vn/brand" in job_url:
                continue

            if job_url:
                job_url = remove_query_url(job_url)
                print(f"\tRequest URL: {job_url}")
                yield scrapy.Request(url=job_url, callback=self.parse_item)
                # yield scrapy.Request(url=job_url, callback=self.parse_item, meta={'updated_at': updated_at})

        # next_page = response.xpath("//a[contains(text(),'›')]/@data-href").get()
        # if next_page:
        #     next_page_url = response.urljoin(next_page)
        #     print(f"Request page: {next_page_url}")
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_item(self, response):
        loader = ItemLoader(item=TopCVItem(), response=response)

        # loader.add_value('updated_at', response.meta['updated_at'])
        loader.add_value('source', self.allowed_domains[0])

        loader.add_value("job_url", response.url)
        loader.add_value("title", response.css('title::text').get())

        loader.add_xpath("salary_range", "//div[@class='job-detail__info--section'][1]")
        loader.add_xpath("location", "//div[@class='job-detail__info--section'][2]")

        loader.add_xpath("description", "//div[@class='job-detail__information-detail--content']/div/div[1]")
        loader.add_xpath("requirements", "//div[@class='job-detail__information-detail--content']/div/div[2]")
        loader.add_xpath("benefit", "//div[@class='job-detail__information-detail--content']/div/div[3]")

        loader.add_xpath("company_url", "//a[@class='company-logo']/@href")
        loader.add_xpath("company_name", "//a[@class='name']")
        loader.add_xpath("company_avatar", "//img[@class='img-responsive']/@src")
        loader.add_xpath("company_scale", "//div[contains(@class, 'company-scale')]//text()")
        loader.add_xpath("company_address", "//div[contains(@class, 'company-address')]//text()")

        # loader.add_xpath("time_left", "//div[@class='job-detail__info--deadline']//text()")

        loader.add_xpath('position', "//div[@class='box-general-group'][1]")
        loader.add_xpath('experience', "//div[@class='box-general-group'][2]")

        loader.add_xpath('quantity', "//div[@class='box-general-group'][3]")

        loader.add_xpath('type', "//div[@class='box-general-group'][4]")
        loader.add_xpath('gender', "//div[@class='box-general-group'][5]")

        loader.add_xpath("branch", "//div[@class='box-category'][1]")

        yield loader.load_item()
