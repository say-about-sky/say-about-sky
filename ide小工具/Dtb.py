from multiprocessing import Process,Queue
import time
#from pathos.multiprocessing import ProcessingPool as Pool
#装饰函数为put
class Plk:
    def __init__(self,func):
        self.func=func
    def __call__(self,q,*v,**k):
        try:
            self.func(*v,**k)
            return q.put(True)
        except:
            return q.put(False)

@Plk
def fun1(name):
    global r_bool
    print('测试%s函数多进程运行动态提示' %name)
    time.sleep(3)
    print('ok')
#泡菜不成功所以暂时用这种方法直接改原函数
def fun2(q,name):
    print('测试%s函数多进程运行动态提示' %name)
    time.sleep(3)
    print('ok')
    q.put('no')#要输出的值
    
#动态监听函数并用子进程动态显示加载循环
class Qu:
    def __init__(self,func):
        self.func=func
    def login(self,q):
        lis=['-','--','>--','->-','-->','--']
        up=iter(lis)
        while 1:
            try:
                if q.qsize()==1:#q.get_nowait():
                    print()
                    return q.put(q.get_nowait())
            except:
                #print(q.qsize())
                pass
            try:
                print(u'\r'+next(up),end='')
                time.sleep(0.2)
            except:
                up=iter(lis)
                #print(r_bool)
    def main(self,func=fun1,*tup,**k):
        #func=self.plk(func)
        #开启子进程执行fun1函数
        q=Queue()
        p = Process(target=self.login,args=(q,)) #实例化进程对象
        args=(q,)+tup
        #print(args)
        p2 = Process(target=func,args=args)

        n1=p.start()
        n2=p2.start()
    
        p.join()
        p2.join()
        return q.get()
    @staticmethod
    def plk(func):
        def pk(q,v,k):
            try:
                func(*v,**k)
                q.put(True)
            except:
                q.put(False)
        return pk
    def __call__(self,*tup,**k):
        return self.main(self.func,*tup,**k)


    
if __name__=="__main__":
    #main()
    fun=Qu(fun2)
    print(fun(''))
