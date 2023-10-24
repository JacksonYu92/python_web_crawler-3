#观察下述代码出现的问题是什么？（了解）
from multiprocessing import Process
import time
ticketNum = 10 #全部的车票
def func(num):
    print('我是子进程，我要购买%d张票！'%num)
    global ticketNum
    ticketNum -= num
    print('子进程的ticketNum: ', ticketNum)
    time.sleep(2)

if __name__ == '__main__':
    p = Process(target=func,args=(3,))
    p.start()
    #主进程在子进程结束之后在结束
    p.join() #只有当子进程结束后，join的调用结束，才会执行join后续的操作
    print('主进程的ticketNum为:',ticketNum) #输出结果依然是10
    #进程和进程之间是完全独立。两个进程对应的是两块独立的内存空间，每一个进程只可以访问自己内存空间里的数据。