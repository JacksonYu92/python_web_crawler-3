# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from redis import Redis
import pymongo

class BiliproPipeline: #一个管道类只负责将数据存储到一个载体中
    fp = None
    #全程只会被调用一次
    def open_spider(self, spider):
        print('i am open_spider()')
        self.fp = open('bili.txt', 'w')

    #process_item函数就是用来接收爬虫文件提交过来的item对象，且可以将item对象中的数据存储到任何载体中
    def process_item(self, item, spider):#参数item就是管道接收到item对象
        title = item['title']
        author = item['author']
        print('i am process_item()')
        #数据存储到文件里
        self.fp.write(author+':'+title+'\n')

        #将item传递给优先级其次的管道类
        return item
    #process_item函数调用的次数取决于爬虫文件给管道提交item的次数

    def close_spider(self, spider):
        print('i am close_spider()')
        #改函数只会在爬虫结束前被调用一次
        self.fp.close()
    # 爬虫文件：bili.py   进行请求发送和数据解析
    # item文件：items.py   定义n个变量
    # 管理文件：pipelines.py 接收item对象进行数据的持久化存储

# 负责将数据存储到mysql数据库中
class MysqlPipeLine:
    conn = None #链接对象
    cursor = None #游标对象
    def open_spider(self, spider):
        #连接数据库的操作只需要被执行一次
        self. conn = pymysql.Connect(
            host = '127.0.0.1', #mysql数据库服务器的ip地址
            port = 3307, #mysql的端口号
            user = 'root', #mysql的用户名
            password = 'root', #mysql密码
            db = 'spider' #数据仓库的名称
        )
        # 创建一个游标对象（用来使用python程序执行sql语句）
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider): # item是由上级优先级高的管道类传递过来的
        title = item['title']
        author = item['author']
        #使用游标对象cursor执行sql语句
        sql = 'insert into bili values ("%s","%s")'%(title, author)
        self.cursor.execute(sql)
        #提交事务
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class RedisPipeLine:
    conn = None  # 链接对象
    def open_spider(self, spider):
        #创建redis的链接对象
        self.conn = Redis(
            host = '127.0.0.1',
            port = 6379,
        )

    def process_item(self, item, spider):
        #item本身就是一个字典
        self.conn.lpush('bili', item)
        return item

# class MongoPipeLine:
#     conn = None
#     db_sanqi = None
#     def open_spider(self, spider):
#         self.conn = pymongo.MongoClient(
#             host='127.0.0.1',
#             port=27017
#         )
#         self.db_sanqi = self.conn['sanqi']
#     def process_item(self, item, spider):
#         self.db_sanqi['xiaoshuo'].insert_one({'title':item['title']})
#         return item