import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1"]
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    #链接提取器：可以根据指定规则（allow='正则表达式‘）进行链接url的提取
    # link = LinkExtractor(allow=r"id=1&page=\d+")
    # link = LinkExtractor(allow=r"\\/inha\\/\d\\/") #在正则中遇到/需要在前面使用\进行转义
    #一个链接提取器一定对应一个规则解析器
    link = LinkExtractor(restrict_xpaths='//*[@id="list"]/div[4]/ul/li/a/@href')
    rules = (
        #规则解析器：可以接收链接并且对其进行请求发送，然后给根据指定规则对请求到的数据进行数据解析
        Rule(link, callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="list"]/div[1]/table/tbody/tr')
        for tr in tr_list:
            ip = tr.xpath('./td[1]/text()').extract_first()
            # print(ip)
            detail_url = xxx
            yield scrapy.Request(detail_url, callback=self.parse)

    def parse(self,response):
        # 对详情页进行数据解析
        link = LinkExtractor(restrict_xpaths='//*[@id="list"]/div[4]/ul/li/a/@href')