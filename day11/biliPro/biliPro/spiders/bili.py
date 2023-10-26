import scrapy
from biliPro.items import BiliproItem

class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://search.bilibili.com/all?vt=40586385&keyword=%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1&from_source=webtop_search&spm_id_from=333.1007&search_source=5"]

    # 基于终端指令的持久化存储（简单）只可以将parse方法的返回值存储写入到指定后缀(xml, csv)的文本文件中
    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
    #     all_data = []
    #     for div in div_list:
    #         title = div.xpath('./div/div[2]/div/div/a/h3/@title').extract_first()
    #         # title = ''.join(title)
    #         author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()').extract_first()
    #         dic = {
    #             'title':title,
    #             'author':author
    #         }
    #         all_data.append(dic)
    #
    #     return all_data





    #基于管道的持久化存储操作（复杂）(通用性）
    def parse(self, response):
        div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
        all_data = []
        for div in div_list:
            title = div.xpath('./div/div[2]/div/div/a/h3/@title').extract_first()
            author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()').extract_first()

            #创建一个item类型的对象
            item = BiliproItem()
            item['title'] = title
            item['author'] = author

            yield item

    #编码流程：1：数据解析 2.创建一个item类型的对象（存储解析出来的数据）3.将解析出来的数据存储到该item类型的对象中 4.将item对象提交给管道