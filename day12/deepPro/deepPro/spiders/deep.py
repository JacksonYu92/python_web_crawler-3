import scrapy
from deepPro.items import DeepproItem

class DeepSpider(scrapy.Spider):
    name = "deep"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest"]
    # 通用的url模板
    url_model = 'https://wz.sun0769.com/political/index/politicsNewest?id=1&page=%d'
    # 页码
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            state = li.xpath('./span[2]/text()').extract_first().strip()
            detail_url = 'https://wz.sun0769.com' + li.xpath('./span[3]/a/@href').extract_first()

            # 创建一个item类型的对象
            item = DeepproItem()
            item['title'] = title
            item['state'] = state
            # 请求传参的技术，将此处的item对象传递给指定的函数:meta作用，可以将一个字典传递给callback指定的回调函数

            #对详情页的url进行请求发送 （手动请求发送GET）
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item':item})

        if self.page_num <= 5:
            new_url = format(self.url_model % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        #负责对详情页的页面源码数据进行数据解析
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre//text()').extract()
        content = ''.join(content).strip()

        #接收通过请求传参传递过来的字典数据
        dic_meta = response.meta
        item = dic_meta['item']
        item['content'] = content

        yield item