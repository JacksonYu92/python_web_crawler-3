from multiprocessing import Process

def func(a,b):
    print('我是子进程，正在执行')
    return a + b
if __name__ == '__main__':
    print('主进程开始执行！')
    #创建一个子进程
    p = Process(target=func, args=(1,2))
    p.start()

    print('主进程执行结束！')