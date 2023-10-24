from threading import Thread
import time
def work():
    global n
    n = 0 #将全局变量修改为了0

if __name__ == '__main__':
    n = 1 #全局变量
    t = Thread(target=work)
    t.start()
    print(n) #在进程中输出全局变量的值就是线程修改后的结果为0