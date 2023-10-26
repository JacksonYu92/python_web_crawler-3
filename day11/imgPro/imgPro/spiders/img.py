import scrapy
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = "img"
    allowed_domains = ["www.xxx.com"]
    start_urls = ["https://pic.netbian.com/4kdongwu/"]

    def parse(self, response):
        #解析图片地址
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_src = "https://pic.netbian.com" + li.xpath('./a/img/@src').extract_first()
            #图片地址封装到item对象中，且将item提交给管道即可
            # print(img_src)
            item = ImgproItem()
            item['img_src'] = img_src

            yield item

            #特殊的管道类：主要是对二进制的数据进行持久化存储
