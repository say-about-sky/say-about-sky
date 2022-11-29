def de(str_r):
    return [i if i[0] in['o','O'] else None for i in str_r.split('\n')]



class Css:
    __slots__={'name':None,'val':None,'__cls__':None,'rdict':dict(),'keys':[],'values':[]}
    
    #判断类中rdict是否被定义
    def __new__(cls,name:str=None,*v):
        try:
            try:
                cls.keys=cls.keys if type(cls.keys)==tuple else ()
                cls.values=cls.values if type(cls.values)==tuple else ()
            except:
                cls.keys,cls.values=(),()
            print(cls.rdict[:])
        except:
            cls.rdict=dict()
        finally:
            return object.__new__(cls)
        
    #将传入的name 作为继承于Css的新类储存在变量val中
    def __init__(self,name:str,*v):
        self.name=name
        cmdf=f"""
class {name}(self.__class__):
    __slots__={'name','val','__cls__','rdict','keys','values'}
    pass
        """
        #如果不加__slots__会变量对照会默认变成0或None
        exec(cmdf,locals(),self.rdict)
        self.val=self.rdict[name]
    def __getitem__(self,i):#通过切片调用类函数
        try:
            return self.values[self.keys.index(i)]
        except:
            try:
                return self.__slots__[i]
            except:
                return 0
    def __setitem__(self,i,v):#通过字典切片添加类函数
        flo=self.__slots__
        los=locals()
        ftt=f"""
def {i}():
    return v
        """
        try:
            flo[i]=v
        except:
            exec(ftt,los,flo)
            lon=eval(i,los,flo)
            self.self_examination(lon)
    def __call__(self,*v):
        return [self.__getitem__(i) for i in v]
    @classmethod
    def self_examination(cls,func=lambda x=None:x):#类方法,用于动态添加类函数
        cls.keys+=(func.__name__,)#添加的对象必须要有__name__属性添加时自动读取该属性
        cls.values+=(func,)
    def __repr__(self,*v):
        return f'{self.name}{v}'
    
if __name__=='__main__':
    c=Css('O0001')
