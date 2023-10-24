import asyncio
import time

urls = ['www.1.com', 'www.2.com', 'www.3.com']

start = time.time()
#在特殊函数内部不可以出现不支持异步的模块代码
async def get_requests(url):
    print('正在下载：', url)
    await asyncio.sleep(2)
    print('请求结束：', url)
    return '{"name":"bobo", "age":30}'

#给任务对象绑定的回调函数
def func(x): #参数x：任务对象
    ret = x.result() #使用任务对象调用result（），该函数会返回任务对象表示的特殊函数内部的返回值
    print(ret)

tasks = [] # 存放所有的任务对象
for url in urls:
    c = get_requests(url) # 创建了3个协程对象
    task = asyncio.ensure_future(c) # 创建3个任务对象
    #给任务对象绑定一个回调函数(一定是在任务对象执行完毕后，才可以执行）
    task.add_done_callback(func)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)