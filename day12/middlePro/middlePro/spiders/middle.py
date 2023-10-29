import scrapy


class MiddleSpider(scrapy.Spider):
    name = "middle"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.baidu.com/","https://www.sogou.com/","https://www.jd.com/"]

    # 代理池
    proxy_list = [
        'https://ip:port','https://ip:port','https://ip:port','https://ip:port','https://ip:port'
    ]#该代理池是需要在中间件中被应用/使用

    def parse(self, response):
        pass
