import scrapy


class PostdemoSpider(scrapy.Spider):
    name = "postDemo"
    # allowed_domains = ["www.xxx.com"]

    #让scrapy对start_urls中的列表元素进行post请求的发送
    start_urls = ["https://fanyi.baidu.com/sug"]

    #该函数是scrapy已经写好了, 运行项目的时候，scrapy是在调用该方法进行相关请求的发送
    def start_requests(self):
        for url in self.start_urls:
            #FormRequest进行post请求发送
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata={"kw": "dog"})

    def parse(self, response):
        #数据解析
        ret = response.json()
        print(ret)
