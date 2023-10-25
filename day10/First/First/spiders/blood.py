import scrapy


class BloodSpider(scrapy.Spider):
    # 爬虫文件的唯一标识
    name = "blood"
    # 允许的域名
    # allowed_domains = ["www.xxx.com"]
    #起始的url列表（重要）：列表内部的url都会被框架进行异步的请求发送
    start_urls = ["https://www.xiachufang.com/category/40076/"]

    #数据解析：parse调用的次数取决于start urls列表元素的个数
    def parse(self, response): #response参数就表示响应对象
        # print(response.text())
        # 如何实现数据解析：xpath
        li_list = response.xpath('/html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[2]/ul/li')
        for li in li_list:
            #xpath最终会返回的是Selector对象，我们想要的解析的数据是存储在该对象的data属性中（extract可以实现该功能）
            # title = li.xpath('./div/div/p[1]/a/text()')[0].extract()

            #extract_first可以将xpath返回列表中的第一个Selector对象中的data属性值获取
            # title = li.xpath('./div/div/p[1]/a/text()').extract_first()

            #extract可以将xpath返回列表中的每一个Selector对象中的data属性值获取
            title = li.xpath('./div/div/p[1]/a/text()').extract()

            #如果xpath返回的列表元素只有一个则使用extract_fiirst, 否则使用extract
            print(title)
