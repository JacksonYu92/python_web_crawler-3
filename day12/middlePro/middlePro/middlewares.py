# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddleproSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class MiddleproDownloaderMiddleware: #下载中间件：处于引擎和下载器之间
    # 拦截请求
    # 参数request: 拦截到的请求对象
    # 参数spider: 爬虫文件中爬虫类的实例化对象(可以实现爬虫文件和中间件的数据交互）
    def process_request(self, request, spider):
        print('i am process_request()')
        # print('拦截到请求对象的url:',request.url)
        # print('拦截到请求对象的请求头:', request.headers)

        #设置请求头-UA
        request.headers['User-Agent'] = 'xxxx'

        #设置Cookie
        request.headers['Cookie'] = 'xxxx'

        # 获取在爬虫文件中定义好的代理池
        proxy_list = spider.proxy_list
        print(proxy_list)
        # 设置拦截到请求对象的代理
        # import random
        # request.meta['proxy'] = random.choice(proxy_list)

        #设置拦截到请求对象的代理
        request.meta['proxy'] = 'https://ip:port'
        return None

    def process_response(self, request, response, spider):
        print('i am process_response()')
        return response

    # 拦截失败的请求对象
    # 参数request: 失败的请求对象
    # 参数exception： 异常信息
    def process_exception(self, request, exception, spider):
        print('该请求失败：',request.url)
        #将错误的请求进行代理的设置（修正）
        # request.meta['proxy'] = 'https://ip:port'

        #返回值的作用：将request表示的请求对象重新进行请求发送
        return request

