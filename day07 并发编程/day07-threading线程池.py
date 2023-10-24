from multiprocessing.dummy import Pool
import time
urls = ['www.1.com','www.2.com','www.3.com','www.4.com','www.5.com']
def get_reqeust(url):
    print('正在请求数据：',url)
    time.sleep(2)
    print('请求结束:',url)

pool = Pool(5) #创建一个线程池，内部存储了3个已经被创建好的线程
pool.map(get_reqeust, urls) #基于线程池中的3个线程，依次对urls列表中的每一个列表元素进行get_request的操作