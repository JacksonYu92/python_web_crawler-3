import time
# def get_request(url):
#     print('正在请求网址的数据：',url)
#     time.sleep(2) #模拟阻塞操作
#     print('请求结束:',url)
#
# if __name__ == "__main__":
#     start = time.time()
#     urls = ['www.1.com','www.2.com','www.3.com']
#     for url in urls:
#         get_request(url)
#     print('总耗时：',time.time()-start)
from multiprocessing import Process
def get_request(url):

    print('正在请求网址的数据：',url)
    time.sleep(2) #模拟阻塞操作
    print('请求结束:',url)

if __name__ == "__main__":
    start = time.time()
    urls = ['www.1.com','www.2.com','www.3.com']
    p_list = [] #存放所有的子进程
    for url in urls:
        p = Process(target=get_request, args=(url,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join() #给每一个子进程调用join（）函数

    print('总耗时：', time.time() - start)