'''目录表达式或dir derivation'''
import os,shutil,glob as gb
import rust_pub.Fds as fd
#import cv2
#from moviepy.editor import *

class Zhou:
    def __init__(self):
        self._self=self
        
    #没有对照属性则返回字典的keys 
    def __getattr__(self,name):
        try:
            return self.__zwcs.keys()
        except:
            try:
                return self.sf.__dict__['中文']
            except:
                self.sf.中文=0
                return self.sf.__dict__['中文']
    def __get__(self,i,o):
        self.sf=i
        return self
    #设置
    def __set__(self,i,v):
        i.__dict__['中文']=v
    def __delete__(self,i):
        try:
            self.__dict__=self.__dict.copy()
            i.中文=False
            del self.__dict
        except:
            i.中文=self.__class__()
    def __call__(self)->'加载中文变量(可以通过__set__设置开关)':
        self.__dict=self.__dict__.copy()
        self.__zwcs={
            '目录下所有盘符':[i[0][0] for i in os.walk(self.sf.url)],
            '子目录列表字典':{Mou(i[0]):i[1:] for i in os.walk(self.sf.url)}
            }
        self.__dict__.update(self.__zwcs)
#暂时废弃
class Mou_set(set):
    def __eq__(self,o):
        if type(o)==type(self):
            return super().__eq__(o)
#主逻辑 原理是集合微观的快捷操作符 如果可以使用/操作符完成就尽量避免使用其他操作避免高时间复杂度
class Mou:
    中文=Zhou()
    #返回一个以输入路径为相对路径的实例化url对象
    def __new__(cls,url,*o,**k):
        if os.path.exists(url):
            self=object.__new__(cls)
            return self
        elif url:
            print('可能没有或找不到该路径')
            return None
    def __init__(self,url:'本地目录'):
        self.url=url#实例的核心,字符串路径
        self.__boo=False
        self.mul_bool=dict(((str,lambda o:gb.glob(self.url)),(int,lambda o:gb.glob(self.url*o))))
        self.tel_dict={'<<':self.__lshift__,'>>':self.__rlshift__,
                  '>':self.__gt__,'<':self.__lt__}
        self.tel_tuple=([('<<','>>'),self.copy_fd],[('<','>'),self.move_fd])
    #self
    def __repr__(self):
        return f'url-<{self.url}>'
    def __str__(self):
        return str(self.url)
    #+子目录的并集
    def __add__(self, other):
        val= ({*(self/'*'),*other} if '__iter__' in dir(other) and type(other)!=str else {*(self/'*'),other})
        return {Mou(i) for i in val}
    # +
    def __radd__(self, other):
        return self.__add__(other)
    #- 子目录的差集
    def __sub__(self, other):
        val=({*(self/'*')}-{*other} if '__iter__' in dir(other) and type(other)!=str else {*(self/'*')}-{other})
        return {Mou(i) for i in val}
    def __rsub__(self, other):
        return other.__add__(self)
    #*次数
    def __mul__(self, other:int):
        #if self.__boo:
            #print(self.look_code(self.__mul__))
        return self.mul_bool[type(other)](other)
    #/ 不包含子文件夹内文件的索引操作
    def __truediv__(self, other:str):
        return gb.glob(self.url+'/'+other)
    #哈希-取目录的字符串哈希
    def __hash__(self):
        return hash(str(self))
    #==判断目录的哈希是否相等
    def __eq__(self,o):
        if type(o)==type(self):
            return str(self)==str(o)
        return super().__eq__(o)
    #返回一个使用字典封装的详细目录key=路径 value={时间，大小...}
    #& 取两个子目录的交集
    def __and__(self,other:"Mou"):
        if type(other)!=type(self):
            other=other if '__iter__' in dir(other) and type(other)!=str else {other}
        else:
            other=other+''
        val=(self+'')
        val.intersection_update(other)
        return val
    #子目录路径字符串的容器(注意容器类型每次调用都会更新) self['文件匹配字符串']->[Mou('匹配到的路径'), ...] self[int] -> list:[str]
    def __getitem__(self, key:(str,int))->(str,list):
        if type(key)==str:
            val=self/key
            return self.__class__(val[0]) if len(val)==1 else [self.__class__(i) for i in val]
        elif type(key)==tuple:
            return tuple((self[i] for i in key))
        return (self/'*')[key] if key!=None else Mou_set()
    #容器创建目录 self[None]=r'新文件夹目录' self['']=r'新文件目录' (反过来也可以)
    def __setitem__(self, key:(str,int,bool), value:str)->(None):
        """
        self[文件目录1]=文件目录2(改变1的内容)
        self[文件夹目录1]=文件夹目录2(改变1子目录的内容)
        """

        if (not value)and key:
            key,value=value,key
            #call_value=os.makedirs if os.path.isdir((self/key)[-1]) or type(value)==type(None) else self.wos
            #value=key if os.path.isabs(key) else self.url+'\\'+value
        try:
            call_value=os.makedirs if os.path.isdir(value) or type(key)==type(None) else self.wos
            #print(type(key)==type(None))
            value=value if os.path.isabs(value) else self.url+'\\'+value
            try:
                lm=str(self[key])
                if not key:
                    return call_value(value)
                elif os.path.isfile(lm):
                    os.remove(lm)
                else:
                    os.rmdir(lm)
                return call_value(value)
            except:
                #print('no',value)
                try:
                    self.cs=call_value
                    return call_value(value)
                except BaseException as e:
                    print(e)
                    return None
        except :
            print('__setitem__报错')
    #删除容器的元素就是删除目录 如果你把子目录内的Mou在删除前赋值，虽然不影响原文件的删除但是在Mou逻辑上仍然有效
    def __delitem__(self, key:(str,int,bool)):
        #获取所有根文件
        get_fi=(fr"{i[0]}\{l}" for i in os.walk(str(self[key])) for l in i[2])
        val=self[key]
        if os.path.isfile(str(val)):
            return os.remove(str(val))
        #如果是self[:]等切片操作删除则递归删除切片内容
        elif (type(key)==slice or (type(key) in (tuple,list))) and val:
            for i in val:
                i=str(i)
                l=self.__class__(os.path.dirname(i))
                del l[os.path.basename(i)]
        try:
            [os.remove(i) for i in get_fi]
        except BaseException as e:
            print('无法删除子文件:',e)
        try:
            get_dir=[i[0] for i in os.walk(str(self[key]))][::-1]
            return [os.rmdir(i) for i in get_dir]
            #return os.removedirs(str(self[key]))
        except BaseException as e:
            print('无法删除目录:',e)
            
    #删除自身指代的目录或文件
    def clear(self):
        path=str(self)
        return os.remove(path) if os.path.isfile(path) else shutil.rmtree(path)
    #>>
    def __rlshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return other<<self
        return self.__terl(other,'>>')
    #>>
    def __rshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return other.__lshift__(str(self))
        return self.__terl(other,'>>')
    #<<复制操作相当于url的os
    def __lshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            pa=str(self)+'\\'
            [self.copy_fd(i,pa+os.path.basename(i)) for i in other]
            return [(i,pa+os.path.basename(i)) for i in other]
        return self.__terl(other,'<<')
    def __rrshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return other<<self
        return self.__terl(other,'<<')
    #<
    def __lt__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            pa=str(self)+'\\'
            [self.move_fd(i,pa+os.path.basename(i)) for i in other]
            return self
        return self.__terl(other,'<')
    #> 移动如果右侧类型为字符串目录则操作整个目录
    def __gt__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return other<self
        return self.__terl(other,'>')
    #| 取或
    def __or__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return (self-''|other+'')
        elif '__iter__' in dir(other):
            return (self-''|set(other))
    def __ror__(self, other:('Mou',str,iter))->('Mou',str,iter):
            return other|self
    #^ 取余
    def __xor__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if type(self)==type(other):
            return (self-''^other+'')
        elif '__iter__' in dir(other):
            return (self-''^set(other))
        return self-''^other
    def rxor__(self, other:('Mou',str,iter))->('Mou',str,iter):
        return other^self
    #% 取样分割相对路径
    def __mod__(self, other):
        if type(other)==int:
            path_ele=self.path_list(os.path.abspath(str(self)))
            return path_ele[other]#os.path.relpath(str(self),path_ele[other])
        return os.path.relpath(str(self),other)
    def __rmod__(self,other):
        pass
    #// 查找某个目录名或判断目录名是否在目录内
    def __floordiv__(self, other:(int,str))->(str,bool):
        lst=str(self).split('\\')[::-1]
        if type(other)==int:
            return lst[other]
        elif type(other)==str:
            return other in lst
    #int ->len()
    def __int__(self)->'当前目录下的所有子目录长度':
        return len(gb.iglob(self.url+'/*'))
    #以后添加根据外部,内部调用改变返回值的判断
    def __len__(self)->int:
        return 1 
    #def __iter__(self):
        #pass
    #操作符内部替换方法(相当于中介) < > << >>
    def __terl(self,other,sb:'符号的字符串'):
        tel_dict, tel_tuple = self.tel_dict, self.tel_tuple
        tup=tel_tuple[0][1] if sb in tel_tuple[0][0] else tel_tuple[1][1] if sb in tel_tuple[1][0] else None
        if other and type(other)==str:
            if os.path.exists(other) or os.path.exists(str(self)):
                st=(str(self),other) if sb in ('>','>>') else (other,str(self))
                tup(*st)
                #print(tup,st)
                return Mou(st[1])
        elif '__iter__' in dir(other):
            return [tel_dict[sb](str(i)) for i in other]
    @staticmethod#根目录列表解析
    def path_list(pa):
        ki=[]
        def hk(pa):
            ki[-1:]+=[pa]
            if pa.count('\\')<1:
                return ki
            elif os.path.dirname(pa)!=pa:
                return hk(os.path.dirname(pa))
            return ki
        return hk(pa)
    #快速创建一个含有该文件的路径和文件
    def wos(self,fn='文件路径'):
        #if os.path.isfile(fn):
        #def wj(value):
        if not os.path.isfile(fn) and os.path.isdir(os.path.dirname(fn)):
            try:
                os.makedirs(os.path.dirname(fn))
            except FileExistsError:
                pass
            with open(fn,'a') as f:pass
        #return wj
    @staticmethod#移动文件或目录
    def move_fd(path1,path2):
        try:
            shutil.move(path1,path2)
        except shutil.Error as e:
            print('当前操作只提供移动而不覆盖:',e)
    @staticmethod#复制文件或目录
    def copy_fd(path1,path2):
        try:
            if os.path.isfile(path1):
                #if os.path.isfile(path2):
                    #path2=path2+'\\'+os.path.basename(path1)
                #print(os.path.isdir(path2))
                #if os.path.isdir(path2):
                    #path2=path2+'\\'+os.path.basename(path1)
                try:
                    #print(path1,path2)
                    shutil.copyfile(path1,path2)
                except:#FileExistsError:
                    #print('no')
                    path2=path2+'\\'+os.path.basename(path1)
                    shutil.copyfile(path1,path2)
            elif os.path.isdir(path1):
                #if not os.path.isdir(path2):
                    #path1=path1+'\\'+os.path.basename(path2)
                try:
                    shutil.copytree(path1,path2)
                except:
                    path2=path2+'\\'+os.path.basename(path1)
                    shutil.copytree(path1,path2)
        except PermissionError as e:
            print('访问失败:',e)
        except RuntimeError:
            print('超出递归限制,无法复制(可能目标文件为源文件子文件，或复制文件自身递归)')
            print('正在尝试还原')
            try:
                os.mkdir('_空目录')
            except:
                pass
            [os.remove(i) for i in os.listdir('_空目录')]
            try:
                ppa=os.getcwd()+'\\_空目录'
                get=os.popen("robocopy /MIR "+f"{ppa} {path2}")
            except:
                print('删除递归目录失败')
            try:
                os.remove('_空目录')
            except PermissionError:
                print('删除空目录失败')
        except BaseException as e:
            print(e)
    #查看当前函数源码
    def look_code(self=None,func=None):
        return func.__code__.co_consts
    #显示调用提示
    def show_help(self)->'打开源码帮助':
        self.__boo=True
        print("self.__boo=True")
    #关闭调用提示
    def shut_help(self)->'关闭源码帮助':
        self.__boo=False


#解析并还原函数的原参
def parse_func_args(func:'func'=lambda _:None)->tuple:
    import inspect
    g=inspect.getfullargspec(func)
    g_ln=abs(len(g.args)-len(g.defaults))
    return tuple(filter(None,g.args[:g_ln]+[f"{i[0]}={repr(i[1])}" for i in zip(g.args[g_ln:],g.defaults)]+[{g.varargs:f'*{g.varargs}',None:None}[g.varargs]]+[{g.varkw:f'**{g.varkw}',None:None}[g.varkw]]))
#解析并还原函数的传参
def parse_func_opt(func:'func'=lambda _:None)->tuple:
    import inspect
    g=inspect.getfullargspec(func)
    return tuple(filter(None,g.args+[f'*{g.varargs}' if g.varargs else None]+[f'**{g.varkw}' if g.varkw else None]))
#元类装饰器
def cas(mt:type=type,*v)->'被{mt}元类加工的类':
    def add(cls):
        nonlocal mt
        return mt(cls.__name__,v,dict(cls.__dict__))#原理核心
    return add
#Kp方法容器 内部方法根据类型环境自行判断调用何种方法
class Jk:
    #判断self.vol是声音还是视频
    def Video_ro_Audio(self=None,if_Video:'func'=lambda _:'Video',if_Audio:'func'=lambda _:'Audio')->'func':
        return if_Video if ~type(self.vol).__name__.find('Video') else if_Audio if ~type(self.vol).__name__.find('Audio') else self.vol
    #获取ed_tuple
    def __get_ed_tuple(self,other):
        ed_tuple=(other,) if self.is_self_type(other) or self.is_vol(other) else tuple(filter(self.is_self_type,other)) if '__getitem__' in dir(other) else tuple()
        ed_tuple=tuple(filter(None,((i.vol if self.is_self_type(i) else i if self.is_vol(i) else None)for i in ed_tuple)))
        return ed_tuple
    #保存vol作为副本
    def stored_old(self):
        self.__old_vol=self.vol.copy()
        self.__old_clip_list=self.clip_list.copy()
        self.__old_vlo_list=self.vol_list.copy()
    #读取vol副本覆盖vol
    def read_old(self):
        self.vol=self.__old_vol.copy()
        self.clip_list=self.__old_clip_list.copy()
        self.vol_list=self.__old_vlo_list.copy()
    #刷新vol值
    def refresh_vol(self):
        self.vol=self.Video_ro_Audio(CompositeVideoClip,CompositeAudioClip)([self.get_vol()]+self.clip_list)
    def 刷新vol(self):#同refresh_vol
        self.refresh_vol()
        return self.vol
    #根据self.vol_list获取vol(拼接列表)
    def get_vol(self):
        return self.Video_ro_Audio(concatenate_videoclips,concatenate_audioclips)(self.vol_list)
    #解析并生成哈希文件名
    def fname_hash(self,other,add_hash=0)->'basename':
        #print(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}")
        if os.path.isfile(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}"):
            return self.fname_hash(other,add_hash=add_hash+1)
        return f"{self.matrix_dict['name']}_{hash(self)+add_hash}"
    #@staticmethod #判断是否与自身类对象相同
    def is_self_type(self=None,o:type=None)->bool:
        try:
            return 'Kp' in o.__class__.__name__
        except:
            return False
    #@staticmethod #判断是否是moviepy对象
    def is_vol(self=None,o:type=None):
        try:            
            return o.__module__.rsplit('.',1)[0]==self.vol.__module__.rsplit('.',1)[0]
        except:
            return False
    @staticmethod#这个可以用rust写 解析字符串参数
    def format(*s:str)->(iter,'Err'):
        import re;from collections import OrderedDict
        try:
            return (Kp.format_dict[''.join(OrderedDict.fromkeys(re.sub('[0-9]','',str(i))))](str(i)) for i in s)
        except:
            return f"Err: {[''.join(OrderedDict.fromkeys(re.sub('[0-9]','',str(i))))for i in s]}"
    @staticmethod#正则匹配字符串数字
    def zermat(*s:str)->(iter,'Err'):
        import re
        try:
            return (tuple(map(lambda i:int(i),re.findall('(\d+)',i))) for i in s )#([int(l) for l in re.findall('(\d+)',i)] for i in s )
        except Exception as e:
            return f"Err: {e}"
    @staticmethod
    def could_float(*s:str)->bool:
        try:
            [float(i) for i in s]
            return True
        except:
            return False

#音频元类
class Kt(type):
    def __new__(cls,*v,**k):
        if not 'Kp' in v[0]:
            raise '类名中没有 Kp 关键字'
        g=(v[2]['__new__'],'__new__') if '__new__' in v[2] else None #(v[2]['__init__'],'__init__') if '__init__' in v[2] else None
        v=v[:2]+({**Jk.__dict__,**v[2]},)+v[3:]
        #print(g,v,k)
        #修改子类的构造函数
        if g:
            g_str=','.join(parse_func_args(g[0]))
            g_str_o=','.join(parse_func_opt(g[0]))
            suec_func_str=f'''
def call({g_str}):
    exec("import cv2;from moviepy.editor import *",globals(),globals())
    return g[0]({g_str_o})
        '''
            #print(suec_func_str)
            val_dict={'g':g}
            exec(suec_func_str,val_dict,val_dict)
            cls.__call__=val_dict['call']
        return super().__new__(cls,*v)

#视频操作
class Kp_video:
    format_dict={'s':lambda i:float(i.rstrip('s')),'min':lambda i:float(i.rstrip('min'))*60,
        '.':lambda i:float(i.split('.')[-1])+sum((float(i.split('.')[l])*60*(l+1) for l in range(len(i.split('.'))-1))),#将小数拆分转为s单位的浮点型 如'1.2'=>62.0(s)
        ':':lambda i:float(i.split(':')[-1])+sum((float(i.split(':')[l])*60*(l+1) for l in range(len(i.split(':'))-1))),#将冒号拆分转为s单位的浮点型 如'1:2'=>62.0(s)
        '':lambda i:float(i),'.min':lambda i:float(i.rstrip('min'))*60,'None':lambda i:0,#这里有问题不应该只返回0
        ':.':lambda i:float(i.split(':')[-1])+sum((float(i.split(':')[l])*60*(l+1) for l in range(len(i.split(':'))-1))),
                 }
    def __new__(cls,path,vol=None):
        self=super().__new__(cls)
        self.matrix_dict={'name':os.path.basename(path).split('.')[0],#这里应该生成图片哈希
                     'suffix':'.'+os.path.basename(path).split('.')[-1]#用于储存扩展的参数
                     }
        self.path=str(path)
        self.vol_file= vol if vol else VideoFileClip(path)
        self.all_dict={
    'write':{i.split('write_')[-1]:i for i in filter(lambda i:'write_' in i,dir(self.vol_file))},
    'to':{i.split('to_')[-1]:i for i in filter(lambda i:'to_' in i,dir(self.vol_file))},
    'set':{i.split('set_')[-1]:i for i in filter(lambda i:'set_' in i,dir(self.vol_file))}
        }
        #vol_list播放序列(包括自身对象)
        self.vol_list=[self.vol_file]
        #vol_list对照副本
        self.__old_vlo_list=self.vol_list.copy()
        #clip_list剪辑序列(不包括自身对象)
        self.clip_list=[]
        #clip_list对照副本
        self.__old_clip_list=self.clip_list.copy()
        #vol对照副本
        try:
            self.vol= concatenate_videoclips(self.vol_list)
        except:
            self.vol= self.vol_file
        self.__old_vol=self.vol.copy()
        self.matrix=cv2.VideoCapture(path)
        self.fps=self.matrix.get(cv2.CAP_PROP_FRAME_COUNT)/self.vol.duration if self.vol.duration else (self.vol.fps,exec(f'self.vol=self.vol.set_duration({self.matrix.get(7)})'))[0]
        #print(self.vol.duration)
        return self
    #当实例被直接调用是支持下面几种对象操作
    def __call__(self,write=None,to=None,set=None):
        lo=locals()
        name=tuple(filter(lambda i:(i in ['write','to','set'])and lo[i],lo))[0]
        tpc=(write,to,set)
        match name:
            case "write":
                return eval(f'self.vol.{self.all_dict["write"][write]}')
            case "to":
                return eval(f'self.vol.{self.all_dict["to"][to]}')
            case "set":
                return eval(f'self.vol.{self.all_dict["set"][set]}')
    #>>输出文件
    def __rshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if not (os.path.exists(str(other)) or os.path.exists(os.path.dirname(str(other)))):
            return "Err: 不是一个有效路径"
        npv=other if '.' in os.path.basename(str(other)) else f"{other}\\"+(self.fname_hash(other) #f"{self.matrix_dict['name']}_{hash(self)}"
                    if os.path.isfile(f"{other}\\{self.matrix_dict['name']}{self.matrix_dict['suffix']}") else
                        self.matrix_dict['name'])+self.matrix_dict['suffix']#os.path.basename(str(other)).split('.')[-1]
        npvn=os.path.basename(other).split('.')[-1] if type(other)==str  else 'images_sequence'
        #if not self.__old_vlo_list==self.vol_list:
        self.refresh_vol()
        if npvn in self.all_dict['write']:
            return eval(f"self.vol.{self.all_dict['write'][npvn]}")(npv)
        return self.vol.write_videofile(npv)
    #<<
    def __rrshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        return self>>other
    #倍速播放设置并返回自身
    def __rpow__(self, other):
        bx=next(self.format(other))
        #调整视频速度
        vol=self.vol.fl_time(lambda t:bx*t)
        #调整音频速度
        self.vol=vol.set_duration(self.vol.duration/bx)
        return self
    #返回设置倍速后的浅拷贝对象
    def __pow__(self, other):
        bx=next(self.format(other))
        #调整视频速度
        vol=self.vol.fl_time(lambda t:bx*t)
        #调整音频速度
        return vol.set_duration(self.vol.duration/bx)
    #拼接并返回拼接后的Kp视频对象
    def __add__(self, other):
        rm=type(self)(self.path,vol=concatenate_videoclips([self.vol,other.vol])) if type(other)==type(self) else type(self)(self.path,vol=concatenate_videoclips([self.vol,other])) if type(other)==type(self.vol) else None
        return rm
    def __radd__(self, other):
        rm=type(self)(self.path,vol=concatenate_videoclips([other.vol,self.vol])) if type(other)==type(self) else type(self)(self.path,vol=concatenate_videoclips([other,self.vol])) if type(other)==type(self.vol) else None
        return rm
    #将对象添加到vol_list播放序列 self<other
    def __lt__(self, other):
        self.vol_list[len(self.vol_list):]=self.__get_ed_tuple(other)
        return self.vol_list
    #other>self
    def __gt__(self, other):
        self.vol_list[:0]=self.__get_ed_tuple(other)
        return self.vol_list
    #视频合成 self&other
    def __and__(self, other):
        if 'vol' in dir(other):
            return type(self)(self.path,vol=CompositeVideoClip([self.vol,other.vol]))
        try:
            return type(self)(self.path,vol=CompositeVideoClip([self.vol,other]))
        except Exception as e:
            return f"Err:{e}"
    #视频合成 other&self
    def __rand__(self, other):
        if 'vol' in dir(other):
            return type(self)(self.path,vol=CompositeVideoClip([other.vol,self.vol]))
        try:
            return type(self)(self.path,vol=CompositeVideoClip([other,self.vol]))
        except Exception as e:
            return f"Err:{e}"
    #加入字幕返回浅拷贝对象
    def __or__(self,other):
        text=other if type(other)==Kp_text else Kp_text(vol=other) if type(other)==TextClip else Kp_text(str(other),time=self.vol.duration if self.vol.duration else 0)
        return self&text #type(self)(self.path,vol=self.get_vol())
    #加入字幕返回自身
    def __ror__(self,other):
        text=other if type(other)==Kp_text else Kp_text(vol=other) if type(other)==TextClip else Kp_text(str(other),time=self.vol.duration if self.vol.duration else 0)
        self.vol=(self&text).vol
        return self
    #设置大小并返回自身(size) other^self
    def __rxor__(self, other):
        self.vol=self.vol.resize(next(self.zermat(str(other))))
        return self
    #返回新大小的浅拷贝对象 self^other
    def __xor__(self, other):
        return type(self)(self.path,vol=self.vol.resize(next(self.zermat(str(other)))))
    #设置位置并返回自身 other//self
    def __rfloordiv__(self, other:str):
        self.vol=self.vol.set_position(next(self.zermat(str(other))))
        return self
    #返回新位置的浅拷贝对象 self//other 
    def __floordiv__(self, other:str):
        return type(self)(self.path,vol=self.vol.set_position(next(self.zermat(str(other)))))
    #def __truediv__(self, other:str):
        #return type(self)(self.path,vol=self.vol.set_position(next(self.zermat(str(other)))))
    #将视频对象(或对象的容器)快捷添加到编辑队列self.clip_list self%other
    def __mod__(self, other):
        self.clip_list[len(self.clip_list):]=self.__get_ed_tuple(other)
        return self.clip_list
    #other%self
    def __rmod__(self, other):
        self.clip_list[:0]=self.__get_ed_tuple(other)
        return self.clip_list
    #索引或切片(默认单位是s 可选单位看format_dict)
    def __getitem__(self,k):
        if type(k)==slice:
            return type(self)(self.path,vol=self.vol.subclip(next(self.format(k.start)),next(self.format(k.stop)) if k.stop else self.vol.end))
        try:
            #这里要改vol和matrix要同步
            #self.matrix.set(cv2.CAP_PROP_POS_FRAMES,int(next(self.format(k))*self.matrix.get(5)))
            #bol,matrix=self.matrix.read()
            return Kp_matrix(self.vol.get_frame(float(k) if self.could_float(k) else next(self.format(k))),name=os.path.basename(self.path).split('.')[0])#Kp_matrix(matrix)
        except Exception as e:
            return f"Err:{e}"
    #可以删除索引到的帧或片段
    def __delitem__(self, k):
        self.vol=self.vol.cutout(next(self.format(k.start)),next(self.format(k.stop)))
        return self.vol
    def __del__(self):
        try:
            self.matrix.release()
        except:
            pass
    #获取ed_tuple
    def __get_ed_tuple(self,other):
        ed_tuple=(other,) if self.is_self_type(other) or self.is_vol(other) else tuple(filter(self.is_self_type,other)) if '__getitem__' in dir(other) else tuple()
        ed_tuple=tuple(filter(None,((i.vol if self.is_self_type(i) else i if self.is_vol(i) else None)for i in ed_tuple)))
        return ed_tuple
    #保存vol作为副本
    def stored_old(self):
        self.__old_vol=self.vol.copy()
        self.__old_clip_list=self.clip_list.copy()
        self.__old_vlo_list=self.vol_list.copy()
    #读取vol副本覆盖vol
    def read_old(self):
        self.vol=self.__old_vol.copy()
        self.clip_list=self.__old_clip_list.copy()
        self.vol_list=self.__old_vlo_list.copy()
    #刷新vol值
    def refresh_vol(self):
        self.vol= CompositeVideoClip([self.get_vol()]+self.clip_list)
    def 刷新vol(self):#同refresh_vol
        self.vol= CompositeVideoClip([self.get_vol()]+self.clip_list)
        return self.vol
    #根据self.vol_list获取vol
    def get_vol(self):
        return concatenate_videoclips(self.vol_list)
    #解析并生成哈希文件名
    def fname_hash(self,other,add_hash=0)->'basename':
        #print(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}")
        if os.path.isfile(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}"):
            return self.fname_hash(other,add_hash=add_hash+1)
        return f"{self.matrix_dict['name']}_{hash(self)+add_hash}"
    #@staticmethod #判断是否与自身类对象相同
    def is_self_type(self=None,o=None):
        try:
            return 'Kp' in o.__class__.__name__
        except:
            return False
    #@staticmethod #判断是否是moviepy对象
    def is_vol(self=None,o=None):
        try:            
            return o.__module__.rsplit('.',1)[0]==self.vol.__module__.rsplit('.',1)[0]
        except:
            return False
    @staticmethod#这个可以用rust写 解析字符串参数
    def format(*s:str)->(iter,'Err'):
        import re;from collections import OrderedDict
        try:
            return (Kp.format_dict[''.join(OrderedDict.fromkeys(re.sub('[0-9]','',str(i))))](str(i)) for i in s)
        except:
            return f"Err: {[''.join(OrderedDict.fromkeys(re.sub('[0-9]','',str(i))))for i in s]}"
    @staticmethod#正则匹配字符串数字
    def zermat(*s:str)->(iter,'Err'):
        import re
        try:
            return (tuple(map(lambda i:int(i),re.findall('(\d+)',i))) for i in s )#([int(l) for l in re.findall('(\d+)',i)] for i in s )
        except Exception as e:
            return f"Err: {e}"
    @staticmethod
    def could_float(*s:str)->bool:
        try:
            [float(i) for i in s]
            return True
        except:
            return False
#视频的图片矩阵附加操作
class Kp_matrix:
    color_dict={'BGR':(0,1,2),'RGB':(2,1,0)}
    def __new__(cls,matrix,name:str='Kp',suffix:str='.png',color='RGB',**k):
        self=object.__new__(cls)
        self.matrix_dict={'name':name,#这里应该生成图片哈希
                     'suffix':suffix#用于储存扩展的参数
                     }
        self.matrix_dict.update(k)
        self.matrix=matrix
        self.color=color
        return self
    def __repr__(self):
        return f'Kp_matrix:{repr(self.matrix)}'
    #self<other
    def __lt__(self, other):
        pass
    #self>other
    def __gt__(self, other):
        pass
    #>>输出文件
    def __rshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if not (os.path.exists(str(other)) or os.path.exists(os.path.dirname(str(other)))):
            return "Err: 不是一个有效路径"
        npv=other if '.' in os.path.basename(str(other)) else f"{other}\\"+(self.fname_hash(other) #f"{self.matrix_dict['name']}_{hash(self)}"
                    if os.path.isfile(f"{other}\\{self.matrix_dict['name']}{self.matrix_dict['suffix']}") else
                        self.matrix_dict['name'])+self.matrix_dict['suffix']#os.path.basename(str(other)).split('.')[-1]
        #这里输出的图片不正常
        return cv2.imwrite(npv,self.matrix[:,:,self.color_dict[self.color]])
    #<<
    def __rrshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        return self>>other
    #解析并生成哈希文件名
    def fname_hash(self,other,add_hash=0)->'basename':
        #print(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}")
        if os.path.isfile(f"{other}\\{self.matrix_dict['name']}_{hash(self)+add_hash}{self.matrix_dict['suffix']}"):
            return self.fname_hash(other,add_hash=add_hash+1)
        return f"{self.matrix_dict['name']}_{hash(self)+add_hash}"
    #添加更多关于图片的快捷处理 如矩阵的变换
#声音操作
@cas(mt=Kt)
class Kp_audio:
    default_arg_dict={'buffersize':'200000','nbytes':'2','fps':'44100'}
    def __init__(self,path=None,audio=None,**k):
        self.default_arg_dict={**self.default_arg_dict,**k}
        self.matrix_dict={'name':os.path.basename(path).split('.')[0],#这里应该生成图片哈希
                     'suffix':'.'+os.path.basename(path).split('.')[-1]#后缀
                     } if path else {'name':type(self).__name__,'suffix':'mp3'}
        self.vol_file=AudioFileClip(path,**self.default_arg_dict)if path else audio
        self.all_dict={
    'write':{i.split('write_')[-1]:i for i in filter(lambda i:'write_' in i,dir(self.vol_file))},
    'to':{i.split('to_')[-1]:i for i in filter(lambda i:'to_' in i,dir(self.vol_file))},
    'set':{i.split('set_')[-1]:i for i in filter(lambda i:'set_' in i,dir(self.vol_file))}
        }
        #vol_list播放序列(包括自身对象)
        self.vol_list=[self.vol_file]
        #vol_list对照副本
        self.__old_vlo_list=self.vol_list.copy()
        #clip_list剪辑序列(不包括自身对象)
        self.clip_list=[]
        #clip_list对照副本
        self.__old_clip_list=self.clip_list.copy()
        try:
            self.vol= concatenate_videoclips(self.vol_list)
        except:
            self.vol= self.vol_file
        self.__old_vol=self.vol.copy()
    #当实例被直接调用是支持下面几种对象操作
    def __call__(self,write=None,to=None,set=None):
        lo=locals()
        name=tuple(filter(lambda i:(i in ['write','to','set'])and lo[i],lo))[0]
        tpc=(write,to,set)
        match name:
            case "write":
                return eval(f'self.vol.{self.all_dict["write"][write]}')
            case "to":
                return eval(f'self.vol.{self.all_dict["to"][to]}')
            case "set":
                return eval(f'self.vol.{self.all_dict["set"][set]}')
    #>>输出文件
    def __rshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        if not (os.path.exists(str(other)) or os.path.exists(os.path.dirname(str(other)))):
            return "Err: 不是一个有效路径"
        npv=other if '.' in os.path.basename(str(other)) else f"{other}\\"+(self.fname_hash(other) #f"{self.matrix_dict['name']}_{hash(self)}"
                    if os.path.isfile(f"{other}\\{self.matrix_dict['name']}{self.matrix_dict['suffix']}") else
                        self.matrix_dict['name'])+self.matrix_dict['suffix']#os.path.basename(str(other)).split('.')[-1]
        npvn=os.path.basename(other).split('.')[-1] if type(other)==str  else 'images_sequence'
        #if not self.__old_vlo_list==self.vol_list:
        self.refresh_vol()
        if npvn in self.all_dict['write']:
            return eval(f"self.vol.{self.all_dict['write'][npvn]}")(npv)
        return self.vol.write_audiofile(npv)
    #<<
    def __rrshift__(self, other:('Mou',str,iter))->('Mou',str,iter):
        return self>>other
#Kp的字幕对象
@cas(mt=Kt)
class Kp_text:
    #{ 'fontsize':30, 'color':'black', 'transparent':True}
    #, 'bg_color':'white','bg_color': None,
    default_k_dict={'color': 'white',
    'fontsize': 30, 'font': './font/msyh.ttc',
    'stroke_color': 'black', 'stroke_width': 2, 'method': 'label',
    'align': 'center','filename': None,'tempfilename': None, 'size': None, 'temptxt': None, 'kerning': None, 'interline': None,
    'transparent': True,'remove_temp': True, 'print_cmd': False}
    def __init__(self,text=None,time=0,pos=('center','bottom'),vol=None,**k):
        if text:
            k={**self.default_k_dict,**k}
            self.vol= TextClip(text,**k).set_duration(time) if not vol else vol
            self.vol=self.vol.set_position(pos) if self.vol.pos(self.vol.start)==self.vol.pos(self.vol.end) else self.vol
    def __get__(self,obj,cls=None,**k):
        return obj._text
    def __set__(self,obj,value=None,**k):
        if type(value)==str:
            setattr(obj,'_text',Kp_text(text=value))
        else:
            setattr(obj,'_text',value)
            
        
#音频操作
class Kp(Kp_video):
    text=Kp_text()
    def __new__(cls,path_ro_vol=None):
        exec("import cv2;from moviepy.editor import *",globals(),globals())
        CompositeAudioClip.fps=44100
        if not path_ro_vol:
            return
        self=super().__new__(cls)
        self._text=None
        self.video=Kp_video(path=path_ro_vol) if os.path.exists(str(path_ro_vol)) else Kp_video(vol=path_ro_vol) if 'Clip' in type(path_ro_vol).__name__ else None
        if self.video:
            #print(self.video.vol.audio.set_fps(self.video.vol.fps))
            self.audio=Kp_audio(audio=self.video.vol.audio.set_fps(self.video.vol.fps))
            return self
        return
    #self>>other
    def __rshift__(self,other):
        return
    #other>>self
    def __rrshift__(self,other):
        return self>>other
    #做一个自动分配魔法方法运算符操作的装饰器或元类
    

#查找dir中是否有指定字符串的元素
def find_dir(cls:object,find_str:str='')->tuple:
    return tuple(filter(lambda i:find_str in i,dir(cls)))
#查找dir中是否有指定字符串的元素(Fds)
def rust_find_dir(cls:object,find_str:str='')->tuple:
    #调用Fds中的函数 由快到慢是find_set,find_vec,find
    return fd.find_set(dir(cls),find_str)
def test_time(f:"func",*u:"arg",**k:"ment"):
    import time
    lod_time=time.time()
    r=f(*u,**k)
    tm=time.time()-lod_time
    return {"time":tm,"return":r}

def test_func(*u:"arg",**k:"ment"):
    def test(f:"func"):
        return test_time(f,*u,**k)
    return test
if __name__=='__main__':
    m=Mou(r'C:\Users\saysky\Desktop\pyLi\基础\整活\public')
    ll=Mou(r'C:\Users\saysky\Desktop\pyLi\基础\整活\public\static')
    l=Mou(r'C:\Users\saysky\Desktop\pyLi\基础\整活\public\hjk')
    #kp=Kp('C:\\Users\\saysky\\Videos\\语法测试.mp4')
    k=Kp(r"C:\Users\Administrator\Videos\Captures\zy.mp4")
    
#列出文件下所盘符gk=tuple(os.walk(current_address));[i[0][0] for i in gk]
#将找到交集并复制到另一个文件[lj<<str(l[k]) for k in {i//0 for i in l-''}&{i//0 for i in ll-''}]
#在同样的交并操作中用运算符表示的操作是不同的 如交集中 kk-kk/'*.bat'=kk^kk['*.bat'] 前者是先字符串拼接后实例化集合元素;后者是先实例化集合元素后拼接.
#有时符号的正反用处是不同的type(lop)=type(kk);lop<<kk['*.py']!=kk['*.py']>>lop 前者是将kk中的所有子元素(目录)复制到lop 后者是复制kk目录自身到lop
#当然对于 lop<<str(kk['*.py'])=str(kk['*.py'])>>lop 是成立的因为提前str声明了要使用原路径
