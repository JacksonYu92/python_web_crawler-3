import scrapy
from zlsPro.items import ZlsproItem
from redis import Redis

class ZlsSpider(scrapy.Spider):
    name = "zls"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/jianli/free.html"]
    #进行redis的链接
    conn = Redis(host='127.0.0.1', port=6379)
    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 简历的标题
            title = div.xpath('./p/a/text()').extract_first()
            # 简历详情页链接（存储到记录表中）
            detail_url = div.xpath('./p/a/@href').extract_first()

            item = ZlsproItem()
            item['title'] = title
            #判断是否要进行详情页的请求发送
            ex = self.conn.sadd('data_id', detail_url)
            if ex == 1:#detail_url作为简历的唯一标识在记录表中不存在（简历之前没有爬取过）
                print('有最新数据更新，正在爬取...。。。')
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item':item})
            else:
                print('暂无数据更新')

    def parse_detail(self, response):
        item = response.meta['item']
        download_url = response.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href').extract_first()
        item['download_url'] = download_url
        yield item

