import time
from multiprocessing import Process
def get_request(url):
    print('正在请求网址的数据：',url)
    time.sleep(2)
    print('请求结束:',url)

if __name__ == "__main__":
    start = time.time()
    p = Process(target=get_request,args=('www.1.com',))
    # 将当前p这个子进程设置为了守护进程
    p.daemon = True #该操作必须放置在子进程启动操作之前
    p.start()

    print('主进程执行结束')