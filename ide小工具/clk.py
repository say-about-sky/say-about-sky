#-*- coding:utf-8 -*-
from 截屏 import run
import 扫图,腾讯识图
import tkinter

from multiprocessing import Process,Queue

class Hun(type):
    @staticmethod
    def __new__(m,*a,**k):
        #print(ctypes.cast(id(m),ctypes.py_object).value,a,len(a))
        a=a[:3]
        #print('m是metaclas调用的Hun自身:',m)
        cls=super().__new__(m,*a)
        #k 捕获的是传入类的参数 现在将它存储在字典中
        cls.dict=k
        cls.run_bool =False
        return cls
    
class Poo(Process,metaclass=Hun):
    def start(self,*v,**k):
        return super().start()
call_dict={'tx':lambda pt,js='':''.join((i.DetectedText for i in 腾讯识图.tenxOCR(腾讯识图.convertimg(picfile=pt)).TextDetections)),
            'bd':lambda pt,js='':扫图.baiduOCR(扫图.convertimg(pt),js=js)}#pt.split('.')[1]
def runn(q,pan=r'.\sept.png'):
    global Poo
    Poo.run_bool=run(patt=pan)
    q.put(Poo.run_bool)
    
def clk(pan=r'.\sept.png',js='',api:['bd','tx']='bd'):
    return call_dict[api](pan,js)

#通过队列进程截图并识图返回结果
def run_q(pan=r'.\sept.png',lbb=None,q=Queue(),js='',api:['bd','tx']='bd'):
    #multiprocessing.freeze_support()
    p = Poo(target=runn,args=(q,pan))  #注意args里面要把q对象传给我们要执行的方法，这样子进程才能和主进程用Queue来通信
    p.start()
    #传递
    runb=q.get()
    p.join()
    if runb:
        txt=clk(pan,js=js,api=api)
        return txt
    return '&正常退出'
#通过队列进程截图
def run_x(pan=r'.\sept.png',lbb=None,q=Queue()):
    #multiprocessing.freeze_support()
    p = Poo(target=runn,args=(q,pan))  #注意args里面要把q对象传给我们要执行的方法，这样子进程才能和主进程用Queue来通信
    p.start()
    #传递
    runb=q.get()
    p.join()
    if runb:
        return '&截图成功'
    return '&正常退出'
if __name__=='__main__':
    import sys
    if sys.argv[1:]:
        print(run_q(sys.argv[1]))
    else:
        print(run_q())
