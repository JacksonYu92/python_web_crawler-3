from threading import Thread
import time
# def func(num):
#     print('num的值是：',num)
#
# if __name__ == '__main__':
#     #创建好了一个子线程（在主线程中创建）
#     t = Thread(target=func, args=(1,))
#     t.start()

def get_request(url):
    print('正在请求：', url)
    time.sleep(2)
    print('请求结束')

if __name__ == '__main__':
    start = time.time()
    urls = ['www.1.com','www.2.com','www.3.com','www.4.com','www.5.com']
    ts = []
    for url in urls:
        t = Thread(target=get_request, args=(url,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
    print('总耗时：', time.time() - start)
