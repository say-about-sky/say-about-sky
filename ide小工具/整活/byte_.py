LEN=range(-128,128)#把取值看作区间
#LEN=range(-12,12)
class Be:#具有特殊功能的标识符称为关键字
    def __init__(self,*a:[int,"确保输入每一个参数都是整型"],**k):
        bt=Bt(a)
        self._bytes=[bt(i) for i in a]
        self.i=0
    def __next__(self):#未完成
        try:
            return self._bytes[self.i]
        except:
            self.i=0
            return self._bytes[self.i]
        finally:
            self.i+=1
    def __iter__(self=None):#未完成
        return (Bt(i) for i in self._bytes)
    
class Bt(Be):#返回一个专属无限迭代器
    def __init__(self,a):#迭代的是数组传入序号对应的数据
        self.a=sum(a)
    def __call__(self,nem=None):
        nem=self.a if nem==None else nem
        #ne=nem-128*(abs(nem)//128)
        ne=abs(nem)%LEN.stop
        return ne+LEN.stop if ne==nem else ne#根据byte总长的索引返回值
    def __get__(self,i,o):
        return i
class Byte_(int):
    def __new__(cls,inx:int=0):
        cls._len=LEN#把取值看作区间
        return super().__new__(cls,inx)
    def __init__(self,inx=0):
        inx=Be(int(inx))
        #print(onmn)
        self._gh=self._len[next(inx)]
        self._i=-1
        self._in=iter((1,0))
    def __getitem__(self,i):#当切片操作时被调用
        return range(self._gh)[i] if self._gh>=0 else range(self._gh,0)[i]
    def __setitem__(self,i,v):
        self.i=v
    def __repr__(self):
        return str(self._gh)
    def __next__(self=None):#迭代器模拟指针
        self._i+=1
        if self._i in self._len:
            return self._i
        self._i=self._len[0]
        return self._i
    def zr(self=None):#重置迭代器
        self._i=-1
    def __eq__(self,value):
        return int(self._gh) == int(value) and type(self) == type(value)
    '''
    以下是测试运算符
    '''
    def __truediv__(self,o):
        return self//o
    def __iadd__(self,o):
        return Byte_(self+o)
    def __isub__(self,o):
        return Byte_(self-o)
    def __imul__(self,o):
        return Byte_(self*o)
    def __matmul__(self,*o):
        return None
    def __pos__(self):
        return Byte_(self._gh+1)
    def __get__(self,i,o):
        return self
    def __int__(self):
        return int(self._gh)
class Byte:
    def __init__(self,byt):
        self._byte=Byte_(byt)
    def byte(self):
        return bin((int(self._byte)).to_bytes(1,'big',signed=True)[0])[2:]
    def __repr__(self):
        return str(self._byte)
    #在前面输入+/++可以自增
    def __pos__(self):
        self._byte=Byte_(-~self._byte)#利用按位取反缺位自增
        return int(self._byte)
    #在前面输入-/--可以自减
    def __neg__(self):
        self._byte=Byte_(~-self._byte)#利用按位取反缺位自减
        return -int(self._byte)
    def __int__(self):
        return int(self._byte)
    def __eq__(self,value):
        try:
            return self._byte==value._byte
        except:
            return False
    def __add__(self,o):
        return self._byte+o
    def __radd__(self,o):
        return o+self._byte
    def __sub__(self,o):
        return self._byte-o
    def __rsub__(self,o):
        return o-self._byte
    def __mul__(self,o):
        return self._byte*o
    def __rmul__(self,o):
        return o*self._byte
    def __iadd__(self,o):
        self._byte=Byte_(self+o)
        return self
    def __isub__(self,o):
        self._byte=Byte_(self-o)
        return self
    def __imul__(self,o):
        self._byte=Byte_(self*o)
        return self
if __name__=='__main__':
    be=Byte(10)
