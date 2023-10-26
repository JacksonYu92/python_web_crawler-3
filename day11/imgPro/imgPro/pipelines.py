# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
#自定义了一个管道类，该类的父类为ImagesPipeline
class BytesPipeline(ImagesPipeline):
    #接收爬虫文件提交过来的item对象，并且可以对相关的多媒体资源进行网络请求
    def get_media_requests(self, item, info):
        #提取图片地址
        img_src = item['img_src']
        #可以对img_src进行网络请求获取图片数据
        yield scrapy.Request(img_src)


    def file_path(self, request, response=None, info=None, *, item=None):
        #用来将请求到的多媒体数据进行指定路径的存储
        #返回存储文件的名字
        img_src = request.url #图片地址
        img_title = img_src.split('/')[-1]
        return img_title

    def item_completed(self, results, item, info):
        return item