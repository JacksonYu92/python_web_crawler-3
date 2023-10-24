#特殊的函数：函数==一组指定形式的操作（任务），特殊之处就在于该函数在定义前需要使用一个async关键字进行修饰。该函数调用后函数内部的程序语句没有被立即执行，而是返回了一个携程对象
#协程对象：协程==特殊的函数==一组指定形式的操作
#任务对象：高级的协程对象。任务对象==协程==一组指定形式的操作
#事件循环
from time import sleep
import asyncio
#特殊的函数
async def get_requests(url):
    print('正在请求数据：', url)
    sleep(2)
    print('请求结束：', url)

# 该特殊函数会返回一个协程对象
c = get_requests('www.1.com')
#创建一个任务对象
task = asyncio.ensure_future(c)
# 如何执行任务
loop = asyncio.get_event_loop() # 创建一个事件循环对象（容器）
loop.run_until_complete(task) # 将任务对象转载在loop容器中,并且启动了loop
#启动loop：会将loop内部装载的所有的任务对象进行异步的执行