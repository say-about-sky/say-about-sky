import weakref as wf
import gc
#用于保存处理核心方法的类
class Hub:
    def __init__(self,cls):
        self._self=cls
        self._dic=self.__dict__#使用字典存储强引用,防止误删,删除自身后自锁,除非用__dict__否则不能删除元素
    def __get__(self,i,o):#在使用后如果没有任何绑定则自毁
        fun=wf.proxy(self._dic['func_'])
        return fun
    def __set__(self,i,v):
        self._dic[i]=v
    def __delete__(self,*v):
        gc.collect()
    def __delattr__(self,i):
        del self._dic[i]
        gc.collect()
    def __del__(self):
        try:
            del self.op
            del self._dic
        except:
            try:
                del self._dic
            except:
                del self
        finally:
            gc.collect()
    #调用函数体
    def __call__(self,*v,**k)->'输入_self添加连接':
        return self.func_(*v,**k)
#利用变量链表对照引用关系
#装饰器将方法装饰为弱引用积木结构[榫卯前身]
class Mortise:
    def __new__(cls,fun=lambda x=None:x):#加工成为弱引用类型并提交加工好的Hub的实例
        op=super().__new__(cls)
        self=self.op_=opl=Hub(wf.proxy(op))
        try:
            opl._dic['func_']=wf.proxy(fun)
        except:
            if type(j)==wf.CallableProxyType:
                opl._dic['func_']=fun
            elif type(j)==wf.ReferenceType:
                opl._dic['func_']=fun()
        try:
            name=fun.__class__.__name__
        except:
            name=fun.__name__
        self.__dict__.update(opl.func_.__dict__)
        opl._dic['op_']=(op,self,(fun,name))
        try:
            self.__call__.__annotations__['v']=opl.func_.__code__.co_varnames
            self.__call__.__annotations__['k']=opl.func_.__annotations__
        except:
            pass
        op.mortise=wf.proxy(opl._dic['op_'][1])#将加工好的自身弱引用在Mortise的实例中(self)
        return op.mortise
    #与其他方法绑定
    def __call__(self,*link:'def not func'):
        lp=locals();lin=None;i=0
        def weq(v,i=i,self=self):
            nonlocal lin
            try:
                if not i:
                    lin=self.__class__(v[i])
                self.tenon=self.__class__(v[i]) if i else lin
                weq(v,i=i+1,self=self.tenon._self)
            except:
                pass
        weq(link,i=i,self=self)
        return lin
if __name__=='__main__':
    j=Mortise()
