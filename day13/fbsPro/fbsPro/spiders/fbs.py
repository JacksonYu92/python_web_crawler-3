import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem
class FbsSpider(CrawlSpider):
    name = "fbs"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://www.xxx.com"]
    redis_key = 'fbsQueue' #可以被共享的调度器队列的名称
    rules = (Rule(LinkExtractor(allow=r"free_\d+\.html/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            title = div.xpath('./p/a/text()').extract_first()
            download_url = xxx
            item = FbsproItem()
            item['title'] = title

            yield scrapy.Request(download_url)

            yield item