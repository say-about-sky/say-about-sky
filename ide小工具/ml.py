#os.path.split分离地址字符串的文件和目录
#如果为True 则返回自身如果是False则返回None
#def Bool_Retuen_ro_None(get):
    #return get if get else None

class Clsr:#储存封闭变量的类
    #装饰器
    def Decorators(*value):
        def ddf(self):
            get=' '.join(value)
            return self(get=get)
        return ddf
    #解释器
    def Interpreter(*value,ren=True):
        if ren:
            return [f"Ml.{i.split()[0]}_l(get={i.split()})" if i.replace('Ml.','').split('(')[0].split()[0] in ds_key
                    else f"{i.split()[0]}(get={i.replace(i.split()[0],'',1).strip().split()})"
                    for i in value]
        return [f"{' '.join(eval(*i.split('(')[1].rstrip(');').split('=',1)[-1:]))}"
                if i.replace('Ml.','').split('(')[0].split()[0] in dsjb
                else ' '.join((i.rstrip(");").split('(',1)[0],i.rstrip(");").split('(',1)[-1].replace('get=','').strip("'[]'")))
                for i in value]
    def Actuators(*value):
        pass
    
#加工预处理命令的类,加工声明Ml中的函数为命令.
class Ds_:
    __slots__=('dsjb','ds_key','ds_vl','dds')
    def __new__(cls=None,funs=object,suffix='_l'):
        cls.dsjb=dsjb=tuple(filter(None,(None if ('__' in i)or not ~i.rfind(suffix) else i for i in funs.__dict__.keys())))
        cls.ds_key=ds_key=[l.replace(suffix,'') for l in dsjb]
        cls.ds_vl=ds_vl=[staticmethod(funs.__dict__[i]) for i in dsjb]#添加了静态方法现在可以不用写self参数了
        cls.dds=dds=dict(zip(ds_key,ds_vl))#表明Ml的字典
        cls.call(cls)#当被实例化时覆盖当前全局的参数容器[预处理]
    def call(cls=None):#覆盖当前全局的参数容器
        global dsjb,ds_key,ds_vl,dds
        dsjb,ds_key,ds_vl,dds=Ds_.dsjb,Ds_.ds_key,Ds_.ds_vl,Ds_.dds
    def Decorators(cls):
        Ds_(funs=cls)
        return cls
#自定义元类
class Value(type):
    @staticmethod
    def __new__(m,*a,**k):
        #print(ctypes.cast(id(m),ctypes.py_object).value,a,len(a))
        a=a[:3]
        cls=super().__new__(m,*a)
        cls.dict=k
        return cls


#命令开头格式必须为 {命令名}_l
@Ds_.Decorators#加载命令
class Ml(metaclass=Value):
    """
    默认储存命令的类,
    内部是一种语法糖,类中的函数会转化为可以被直接调用的特殊功能标识符[关键字]
    其命令必须传入明确的参数[get],这个类内部函数是可以随时修改的,
    命令会动态捕获类中添加的变量
    注意:在命令框中直接调用的命令是此类函数的静态方法不是直接调用函数本身
    当使用;进行命令划分时请在';'后面加上空格否则一律判定为字符串,
    如 echo Hello World; echo yee;
    '; '命令分割不是指结束命令而是嵌套执行,也就是说'; '分割其实是递归!
    """
    def __new__(cls,*a,**k):
        self=super().__new__(cls)
        self.Ml=M_t.Mortise(self)
        return self
    def __init__(self,txts='',name='_'):
        self.name=name
        self.text=txts
    #上下文管理器用于测试命令脚本: with Ml(<多行名字字符串>) as t:<python代码> 如with Ml('''echo 1''') as t:pass
    def __enter__(self,*a):
        self.text=[diy(i) for i in filter(lambda x:bool(x),self.text.split('\n'))]
        return self.Ml
    #结束上下文管理器
    def __exit__(self,*v):
        try:
            exec(f"del {self.name}",globals(),Clsr.loc)
        except:
            pass
        del self.Ml.op_
    @classmethod#类方法,用于动态添加类函数
    def self_examination(cls,func=lambda x=None:x):
        exec(f'cls.{func.__name__}=func',locals(),globals())#添加的对象必须要有__name__属性添加时自动读取该属性
    #获取任意变量并返回打包后的值(return)[命令优先] get 变量名; 一般的,所有的命令都会传递get,当输入命令时get是以字符串数组的形式传递的,所以命令中输入的变量也是字符串.
    def get_l(self=None,get=[]):
        #Interpreter(get)
        try:
            return diy(' '.join(get[1:])).value
        except:
            return (diy(' '.join(get[1:])),)
    #设置当前命名空间(作用域)内的字面量,一般配合get使用 set [变量]=[字面量/变量/命令];[变量]=[字面量/变量/命令]...
    def set_l(self=None,get=[]):
        global diy
        get=' '.join(get[1:]).split(';')
        ge=tuple((i.split('=') for i in get))
        bt=Byte(0)
        #{i[0]}={diy(i[1])}
        try:#set a= c int 10
            [(locals().update({'set_key':diy(i[1])}),exec(f"{i[0]} = set_key",dict(**locals(),**globals()),Clsr.loc),++bt) for i in ge]
        except BaseException as e:#下面这句不是抄的就是写着玩
            print('The parameter was not found in the commands/scope:',ge[int(bt.byte())][-1])
            try:
                diy(' '.join(get))
            except:
                [eval(i,Clsr.glo,Clsr.loc) for i in get]
                print('ok')
    #返回自身的字符串
    def string_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[str(diy(i)) for i in get] if len(get)>1 else str(diy(get[0]))
        except:
            get=[[diy(f"str {i}") for i in eval(i)] for i in get] if len(get)>1 else str(get[0])
        finally:
            return get
    #返回str类型的数据 str [对象];[对象]...
    def str_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[str(diy(i)) for i in get] if len(get)>1 else str(diy(get[0]))
        except:
            get=[[diy(f"str {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #返回int类型的数据 int [对象];[对象]...
    def int_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[int(diy(i)) for i in get] if len(get)>1 else int(diy(get[0]))
        except:
            get=[[diy(f"int {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #返回float类型的数据 float [对象];[对象]...
    def float_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[float(diy(i)) for i in get] if len(get)>1 else float(diy(get[0]))
        except:
            get=[[diy(f"float {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #返回byte类型的数据 byte [对象];[对象]...
    def byte_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[Byte(diy(i)) for i in get] if len(get)>1 else Byte(diy(get[0]))
        except:
            get=[[diy(f"byte {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #返回mortise类型的数据 mortise [对象];[对象]...
    def mortise_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            get=[M_t.Mortise(diy(i)) for i in get] if len(get)>1 else M_t.Mortise(diy(get[0]))
        except:
            get=[[diy(f"mortise {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #返回ctypes类型的数据 c [类型] [对象];...
    def c_l(self=None,get=[]):
        get=' '.join(get[1:]).split(';')
        try:
            ge=[tuple(i.split())if 'c_' in i else tuple(('c_'+i).split()) for i in get]
            get=[ctypes.__dict__[diy('string '+i[0])](diy(i[1])) for i in ge] if len(ge)>1 else ctypes.__dict__[diy('string '+ge[0][0])](diy(ge[0][1]))
        except:
            get=[[diy(f"c {i}") for i in eval(i)] for i in get]
        finally:
            return get
    #删除包括缓存的所有同名变量 del [变量] [变量] ...
    def del_l(self=None,get=[]):
        get=get[1:]
        def ddf(ge=get,err=True):
            l=0
            for i in [f"del Clsr.glo['{ge}']",f"del Clsr.loc['{ge}']",f"del bianl['{ge}']",]:
                try:
                    exec(i)
                except:
                    l+=1
            if l==3:
                if err:
                    print('无法从作用域检索到该变量: ',ge)
        if get[0] in newts.stat.keys():
            get=get[1:]
            try:
                [exec(f'del Ml.{ge}_l') if f'{ge}_l' in Ml.__dict__ else None for ge in get]
                Ds_(Ml);congzai_Ml()
                flushed_prog(user_keywords=Ds_.ds_key)
            except:
                pass
            return [ddf(ge,err=False) for ge in get ]
        return [ddf(ge) for ge in get ]
    #可设置结束符的echo print [变量/end='结束字符'(默认是空字符'')]...[变量]
    def print_l(self=None,get=[]):
        end='\n' if not get[1:] else get[2] if get[1] =='end' else ''
        get= get[2:] if not end in ('\n','') else get
        Ml.echo_l(self,get=get,end=end)
    #直接输入目录打开文件 open [目录/网址(如果是网址则返回requests.get对象)] [目录]...
    def open_l(self=None,get=[]):
        #print('get:',get)
        get=tuple(map(lambda i:Diy_to_code_or_str(i,local=globals()),get[1:]))
        #print('get=',get)
        try:
            return [roo_d(i)for i in get]
        except:
            if len(get)==1:
                return requests.get(get[0])
    #设置文件读取方式 open 'rb'[\...]或者open read [int](读取长度) 或 open zhr [bool值](打开覆盖)
    def set_open_l(self=None,get=[]):
        global rsr,reado
        if get[1] in ['read',]:
            reado=int(get[2])
        elif get[1] in ('zhr',):
            bools={True:code_color_Dio.l[0],False:code_color_Dio.l[1]}
            #如果传入的参数有一个bool为False 则结果为False(以后专门写一个判别器可以自定义逻辑门路)all()或any()达到同样效果
            oro=bools[not bool(tuple(filter(lambda i:not bool(eval(i)),get[2:] if get[2:] else [False])))]()
            congzai_Ml()
            return oro
        else:
            diy('file_type None None') if 'b' in get[1] else 'file_type UTF-8 ignore'
            rsr=get[1]
        congzai_Ml()
    #快捷设置文件解码要求(不输入可重置) file_type [解码格式/-r] [异常处理方式](固定顺序,[]内容不要加引号) 或者 encoding=[解码格式] 或者 errors=[异常处理方式] 或者两个都写
    def file_type_l(self=None,get=[]):
        get=get[1:]
        kl=[~i.find('=') for i in get]
        if len(kl)>kl.count(0) or not get:
            ad=kl.copy()
            add =get[kl.index(0)] if kl.count(0) else None
            jk=lambda key:dic[key] if key in dic else add
            dic={i.split('=')[0].replace(' ',''):i.split('=')[1].replace(' ','') if i.split('=')[0].replace(' ','') in ('encoding','errors')else add for i in get}
            Ml.encoding,Ml.errors=jk('encoding'),jk('errors')
        elif get[0]=='-r':
            Ml.encoding,Ml.errors='UTF-8','ignore'
        else:
            Ml.encoding,Ml.errors=get
        try:
            Ml.encoding,Ml.errors=eval(Ml.encoding),eval(Ml.errors)
        except:
            pass
        return Ml.encoding,Ml.errors
    #设置当前窗口分辨率 res [长] [宽]
    def res_l(self=None,get=[]):
        """
        width=[] height=[]
        [] []
        """
        get=get[1:]
        kl=[~i.find('=') for i in get]
        if not get:
            return [(root.winfo_height(),root.winfo_width()),
            (jp.panecget(jp.panes()[0],'width'),jp.panecget(jp.panes()[0],'height'))]
        elif len(kl)>kl.count(0) or not get:
            ad=kl.copy()
            add =get[kl.index(0)] if kl.count(0) else None
            jk=lambda key:dic[key] if key in dic else add
            dic={i.split('=')[0].replace(' ',''):i.split('=')[1].replace(' ','') if i.split('=')[0].replace(' ','') in ('width','height')else add for i in get}
            width,height=jk('width'),jk('height')
        elif get[0]=='-r':
            jp.paneconfig(jp.panes()[0],height=jp.panecget(jp.panes()[0],'height')+(400-root.winfo_height()))
            jp.paneconfig(jp.panes()[0],width=600)
            return root.geometry("600x400")
        else:
            width,height=get
        try:#res 400 200
            width_x=root.winfo_width()-int(width)
            height_x=int(height)-root.winfo_height()
            #获取原值
            Txt=jp.panecget(jp.panes()[0],'width'),jp.panecget(jp.panes()[0],'height')
            
            #设置cmd组件高度
            jp.paneconfig(jp.panes()[1],height=root.winfo_height()-jp.panecget(jp.panes()[0],'height'))
            #设置嵌套组件的宽度
            j.paneconfigure(j.panes()[0],width=int(width))
            #缩放
            jp.paneconfig(jp.panes()[0],height=Txt[1]+height_x if type(Txt[1])==int else Txt[1])
            jp.paneconfig(jp.panes()[0],width=int(width))
            root.geometry(f"{width}x{height}")
        except():
            pass
    #循环调用命令
    def __fori(i=0,fun=None):
        fun= fun.replace(';','; ')
        if ~i:
            for i in range(i):
                diy(fun)
        else:
            while 1:
                diy(fun)
    #快捷循环调用命令 fori [次数] [命令...];[命令...]
    def fori_l(self=None,get=[]):
        get=get[1:]
        if get:
            try:
                it=int(diy(get[0]))
            except:
                it=1
            Ml.__fori(i=it,fun=' '.join(get[1:]))
    #读取取文本框中所有字符串并返回 Text
    def Text_l(self=None,get=[]):
        try:
            txt=text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
            return {txt:txt,'':text.get('1.0', tk.END)[:''.rfind('\n')]}[txt]
        except: 
            return text.get('1.0', tk.END)[:''.rfind('\n')]
    #翻译传入的变量返回值/字符串并返回 translate [-r(将所有输入转换为字符串)/命令/字符串/.] [命令/字符串/.]
    def translate_l(self=None,get=[]):
        get=get[1:]
        if get:
            if get[0]=='-r':
                return text_Translation(' '.join(get[1:]))
        try:
            return ' '.join((text_Translation(diy(i))for i in get))
        except:
            return ' '.join((text_Translation(i) for i in get))
    
    def __say_api_ce(get,**k):
        try:
            return [engapi.txchemp(str(diy(i)),**k) for i in get[1:]]
        except:
            return engapi.txchemp(' '.join(get[1:]),**k)
    #字符串转音频并播放 say [eng/.] [变量]
    def say_l(self=None,get=[]):
        get=get[1:]
        if get[0] in ['help','-help','--help']:
            return print(engapi.yd_lang)
        if get:
            if get[0]=='eng':
                try:
                    return [engapi.txengmp(str(diy(i))) for i in get[1:]]
                except:
                    return engapi.txengmp(' '.join(get[1:]))
            #elif get[0]=='ce':
                #Ml.__say_api_ce(get)
            elif get[0] in engapi.yd_lang:
                Ml.__say_api_ce(get,lang=get[0])
            else:
                Ml.__say_api_ce([':']+get)
    #截图 screenshots [保存位置(默认传入命令的目录)] [保存位置(输入多个目录连续截屏)] 
    def screenshots_l(self=None,get=[]):
        if get[1:]:
            print([i for i in get[1:]])
            for i in get[1:]:
                print(clk.run_x(i))
        else:
            print(clk.run_x())
    #扫图取词并处理结果(暂不支持批量) scan_translation [图片地址.png/jpg] [输出目录(默认是返回)]
    def scan_screenshots_l(self=None,get=[]):
        if get[2:]:
            return 扫图.baiduOCR(get[1],get[2])
        return 扫图.baiduOCR(get[1])
    #用泡菜操作数据 pickle [dump/load/dumps/loads] [-t/-d/open/变量] [写入的格式[-t:]/写入的地址[-d:]/读取的地址或者空(默认)/变量]
    def pickle_l(self=None,get=[]):
        get=get[1:]
        rs=Ml.add_open
        tw='wb'
        if get:
            dic={'dump':pickle.dump,'load':pickle.load,
                 'dumps':pickle.dumps,'loads':pickle.loads}
            if get[0] == tuple(dic.keys())[0]:
                if get.count('-t'):
                    ind=get.index('-t')
                    tw=get[ind+1] if get[ind+1:] else 'ab'
                    del get[ind,ind+2]
                if get.count('-d'):
                    ind=get.index('-d')
                    ws=get[ind+1]
                    del get[ind,ind+2]
                else:
                    ws=asksaveasfilename(title=u'选择要写入的文件')
                    Ml.add_open=ws
                get=list(filter(lambda x:x not in ['-t','-d','ab','wb'],get))
                print(get)
                with open(ws,tw) as f:
                    return [(pickle.dump(diy(i),f),diy(i)) for i in get[1:]]
            elif get[0] == tuple(dic.keys())[1]:
                if get[1:]:
                    rs=askopenfilename(title=u'选择要读取的文件') if get[1]=='open' else get[1]
                with open(rs,'rb') as f:
                    lio=tuple()
                    f.seek(0)
                    while 1:
                        try:
                            lio+=(pickle.load(f),)
                        except:
                            break
                return lio
            elif get[0] in dic.keys():
                return [dic[get[0]](diy(i)) for i in get[1:]]
    cme_dict={'GUI':lambda _:None,'CMD':lambda _:None,'TK':lambda _:None}
    #额外开一个交互窗口以某一或某类命令为头命令交互(未完成)
    def cme_l(self=None,get=[]):
        get=get[1:]
        out=None
        if get:
            if get[0] in Ml.cme_dict:
                out=Ml.cme_dict[get[0]](get[1:])
        return out
    #强制使用python执行 cmd<空格>[要执行的py命令]
    def cmd_l(self=None,get=[]):
        get=get[1:]
        ser=' '.join(get)
        return exec(ser,Clsr.glo,Clsr.loc)
    #启动java虚拟机 cmdor java(虚拟机返回的内容只能被命令窗口捕获idle有自己的捕获函数)
    def cmdor_l(self=None,get=[]):
        get=get[1:]
        if get and get[0]=='java':
            Ml.Single_thread=Single_thread_bool(bool(1),call=jv)
        else:
            try:
                Ml.Single_thread=Single_thread_bool(bool(1))
                shutdownJVM()
            except Exception as e:
                print('>虚拟机无响应< \t :( \t'+str(e)+'\t')
    #将py文件编译为字节码pyc文件-->py虚拟机 pyc [open/-t [保存目录]/,]
    def pyc_l(self=None,get=[]):
        get=get[1:]
        if not get:
            print('注意当前编译的是原文件如果你修改了文本框中的代码请及时保存')
        elif get[0]=='open':
            pyt=askopenfilename(title=u'选择文件')
            Ml.add_open=pyt
        elif get[0]=='-t':
            compileall.compile_path(get[1])
        if ~os.path.basename(Ml.add_open).find("."):
            compileall.compile_file(Ml.add_open)
        else:
            compileall.compile_dir(Ml.add_open)
    #将java文件编译为字节码class文件-->java虚拟机 javac [open/,]
    def javac_l(self=None,get=[]):
        get=get[1:]
        if not get:
            print('注意当前编译的是原文件如果你修改了文本框中的代码请及时保存')
        elif get[0]=='open':
            javat=askopenfilename(title=u'选择文件')
            Ml.add_open=javat
        print(f'{Ml.add_open}')
        print(os.popen(f'javac {Ml.add_open} -encoding UTF-8').read())
    #一键式读取字符串备份并编译java文件为class javae [-jar/Text/str] [str/Text/-jar];并存储在当前.cache文件内如果有'-jar'则同时打包为jar文件
    def javae_l(self=None,get=[]):
        add_jar_bool=(True,get.remove('-jar'))[0] if '-jar' in get else False
        get=diy(' '.join(get[1:]))
        tree = javalang.parse.parse(get)#获取java语法解析树
        classs=tree.types[0]#解析类方法
        add_open=r'/'.join(Ml.add_open.split(r'/')[:-1])+r'/.cache/' if '.' in Ml.add_open.split(r'/')[-1] else Ml.add_open+r'/.cache/'
        print(add_open)#获取当前上级目录并打印
        if not os.path.exists(add_open):#如果当前目录没有.cache则创建
            os.makedirs(add_open)
        add=add_open+classs.name+'.java'#使用类方法名
        with open(add,'w',encoding='UTF-8',errors=Ml.errors) as f:
            f.write(get)
        print(add_jar_bool,f"jar cvf {add_open+classs.name+'.jar'} {add_open+classs.name+'.class'}")
        try:
            print(os.popen(f'javac {add} -encoding UTF-8').read())
            if add_jar_bool:
                Ml.__java_e(name=classs.name,opend=add_open)
        except BaseException as e:
            print(get)
        finally:
            return tree,add_open
    #内部函数用于打包java的.class文件
    def __java_e(self=None,get=[],name='',opend=''):
        return os.popen(f"jar cvf {opend+name+'.jar'} {opend+name+'.class'}")
    #一键式捕获文本框并缓存编译java文件后返回函数属性地址列表或调试类 javar [类名/None(不写)]; 如果不输入函数名则直接调用main方法调试
    def javar_l(self=None,get=[]):
        get=get[1:]
        return jv(get)
    #使用cmd运行javar
    def javarun_l(self=None,get=[]):
        tree,add_open=Ml.javae_l(get=[':','Text'])
        classs=tree.types[0]#解析类方法
        h=os.getcwd()
        os.chdir(add_open)
        print(os.popen(f'java {classs.name} -encoding UTF-8').read())
        os.chdir(h)
    #将字节码写入到文件 示例 filew -wb txt cs1.txt cs2.txt  ...
    def filew_l(self=None,get=[]):
        get=get[1:]
        txt=get[0]
        #print(txt,get)
        s,get,o=(Diy_to_code_or_str(get[1],
                local=globals()),map(lambda i:Diy_to_code_or_str(i,local=globals()),
                get[2:]),
                 get[0].strip('-')) if txt[0]=='-' else (Diy_to_code_or_str(get[0],local=globals()),
                                                         map(lambda i:Diy_to_code_or_str(i,local=globals()),get[1:]),
                                                         '')
        #print(s,get,o)
        return [Write_To_file_Return(i,s=s,o=o) for i in get]
    def _filer(ot:(str,list,set),o:str='rb')->str:
        lis=[]
        i=ot
        #print('_filer',o)
        try:
            for i in ot:
                #print(type(i))
                path=Diy_to_code_or_str((Ml._filer(i,o=o) if Type_in_iter(i) else i),local=globals())
                #print(path)
                lis.append(path if Type_in_iter(path) else Read_To_Retuern(path,o=o))
        except:
            print(f'path: {i} 不是一个有效目录')
        return lis
    #将文件中的字符串返回相应文件的字节码列表 fileb [路径] [路径] ...
    def filer_l(self=None,get=[]):
        get=get[1:]
        o='rb'
        if get:
            get,o=(get[1:],get[0].strip('-')) if get[0][0]=='-' else (get,o)
        #print(get)
        return Ml._filer(map(lambda i:diy(i),get),o=o)
            
    #fileb的载体
    def loop_file_codec(pat:('path',list,tuple,set,),sin='\n'):
        #循环解码直到能解出
        als=Codec_tuple
        i=0
        byte=als[i]
        while 1:
            try:
                #print(byte)
                return Boot_file_path_dir_exp_bool_func(pat,sin,byte=byte)
            except:
                i+=1
                try:
                    byte=als[i]
                except:
                    return print('无法解码目录')
    #将文件中的字符串编译为命令行命令并返回fileb [路径] [路径] ...
    def fileb_l(self=None,get=[]):
        get=get[1:]
        txt=Ml.loop_file_codec(get,';')
        #print(txt)
        return compile(txt,'','single')
    #快捷以命令行运行外部脚本文件 run [path] [path] ...
    def run_l(self=None,get=[]):
        #print(get)
        get=map(lambda i:str(Diy_to_code_or_str(i,local=globals())),get[1:])
        gets=' '.join(get)
        gtxt=diy(f"""fileb {gets}""")
        return exec(gtxt)
    #设置线程池的线程数 threads [int]
    def threads_l(self=None,get=[]):
        get=get[1:]
        if get:
            Ml.nt=int(get[0])
            pl_m(Ml.nt)
        else:
            pl_m(Ml.nt)
    #强制单线程single_thread [什么都不写]-->False ;else; -->True
    def single_thread_l(self=None,get=[]):
        get=get[1:]
        Ml.Single_thread=Single_thread_bool(bool(get))

    #调用cmd命令窗口
    def sys_l(self=None,get=[]):
        get=get[1:]
        os.system(' '.join(get))
    #清空文本 cls [./r(文本)]
    def cls_l(self=None,get=[]):
        try:
            if get[1]=='r':
                lb.delete('1.0','end')
        except:
            os.system('cls')
        print('清空')
    #整理字节文本 byte 
    def bytes_l(self=None,get=[]):#open rb;byte
        kk=text.get('1.0', tk.END)
        bp=('%s' % kk)[2:-2].replace(r'\x',' ')
        print(bp)
        bp=bp[:-1].strip('.')
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,bp)
    #ascii编译文本内容
    def ord_l(self=None,get=[]):
        get=get[1:]
        np_type=np.uint8
        if get:
            if get[0] in ("-h","-help","-H"):
                np_dict=np.__dict__
                np_type_str='\n'.join(filter(lambda i:"dtype" in dir(np_dict[i]),np_dict))
                print("ord/chr后面可加np类型作为编译对象,常见的np类型:\n",np_type_str)
                return
            try:
                np_type=np.__dict__[get[0]]
            except:
                np_type=np.uint8
        kk_b=text.get('1.0', tk.END).strip().encode()
        #批量转换为uint8编号 
        np_on=np.frombuffer(kk_b,dtype=np_type)
        kk=' '.join(np_on.astype(str))
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,kk)
        return np_on
    #ascii翻译文本内容
    def chr_l(self=None,get=[]):
        np_type=np.uint8
        if get:
            if get[0] in ("-h","-help","-H"):
                np_dict=np.__dict__
                np_type_str='\n'.join(filter(lambda i:"dtype" in dir(np_dict[i]),np_dict))
                print("ord/chr后面可加np类型作为编译对象,常见的np类型:\n",np_type_str)
                return
            try:
                np_type=np.__dict__[get[0]]
            except:
                np_type=np.uint8
        sss_list=text.get('1.0', tk.END).strip().split(' ')
        #这里可以将编码类型dtype=np.uint8改为可选项 
        np_on=np.array(sss_list,dtype=np_type).tobytes()
        kk=np_on.decode()
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,kk)
        return np_on
    #二进制翻译文本内容 bin
    def bin_l(self=None,get=[]):
        kk=Lins.encode(text.get('1.0', tk.END).strip())
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,kk)
        return kk
    #二进制反译文本内容 rbin
    def rbin_l(self=None,get=[]):
        kk=Lins.decode(text.get('1.0', tk.END))
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,kk)
        return kk
    #用摩斯密码翻译文本框 ms [-r,-rn,]
    def ms_l(self=None,get=[]):
        get=get[1:]
        try:
            jm='/jn ' if get[0][2:]=='n' else '' if get[0][1]=='r' else '/j '
            get=get[1:]
        except:
            jm='/j '
        kk=' '.join(get) if get else text.get('1.0', tk.END).replace('\n','')
        kk=摩斯.msing(jm+kk)
        if rd:
            lb.delete('1.0','end')
        lb.insert(tkinter.END,kk)
    #写入ce.json 文件 jsonw [命令/...] [命令] ...
    def jsonw_l(self=None,get=[]):
        get=get[1:]
        lin()
        st= str(globals()) if not get[1:] else str([diy(i) for i in get[1:]])
        rs= '..' if not get else askopenfilename(title=u'写入js') if get[0]=='open' else get[0]
        with open(rs+'\ce.json','w',encoding='utf-8') as file:
            file.write(json.dumps(st,indent=2,ensure_ascii=False))
    #读取ce.json 文件 
    def jsonr_l(self=None,get=[]):
        get=get[1:]
        lin()
        st= globals() if not get[1:] else str([diy(i) for i in get[1:]])
        rs= '..' if not get else askopenfilename(title=u'读取js') if get[0]=='open' else get[0]
        with open(rs+r'\ce.json','r',encoding='utf-8') as file:
            data = json.loads(file.read())
        st=st.update(data)
    #开始多行运行
    def new_l(self=None,get=[]):
        Tr.long=True
        try:
            t=' '.join(get)
            diy(t)
        except:
            print('报错')
            Tr.long=False
    #结束多行运行
    def end_l(self=None,get=[]):
        Tr.long=False
    #设置命令栏窗口变量环境(作用域) exec<空格>[输入环境(一般是字典)]<空格>[输出环境(一般是输入环境)]
    def exec_l(self=None,get=[]):
        get=[eval(i) for i in get[1:]]
        dip=(type(get[0])==dict),(type(get[1])==dict)
        Clsr.glo,Clsr.loc=tuple(map(lambda d:get[d] if dip[d] else globals(),range(len(dip))))
        print(dip)
    #返回exec当前作用域 look_exec ->(输入环境 输出环境)
    def look_exec_l(self=None,get=[]):
        return Clsr.glo,Clsr.loc
    #echo == print 可以打印任何命令的返回值(包含Ml关键字)
    def echo_l(self=None,get=[],end='\n'):
        try:
            get=[eval(i,Clsr.glo,Clsr.loc) for i in get[1:]]
        except:
            try:
                get=diy(' '.join(get[1:]))
            except:
                get=get[1:]
                #get=' '.join(get[1:])
        print(*get if get else (get,),end=end)
    #快捷导入模块 import==import or import [模块]<空格>[模块]<空格>[模块]....
    def import_l(self=None,get=[]):
        get=','.join(get[1:])
        exec(f"import {get}",Clsr.glo,Clsr.loc)
    #快捷获取root上级环境变量 如 use fff 相当于 fff=root.root.fff
    def use_l(self=None,get=[]):
        get=get[1:]
        congzai_Ml()
        for i in get:
            try:
                Clsr.glo[i]=eval(i)
            except BaseException as e:
                print(f'获取 {i} 失败:',e)
    #修改着色器状态codeStatus 可bool对象 可bool对象 ...
    def codeStatus_l(self=None,get=[]):
        get=get[1:]
        if not get:
            return next(code_color_Dio)()
        bools={True:code_color_Dio.l[0],False:code_color_Dio.l[1]}
        #如果传入的参数有一个bool为False 则结果为False(以后专门写一个判别器可以自定义逻辑门路)all()或any()达到同样效果
        return all(get)#bools[not bool(tuple(filter(lambda i:not bool(eval(i)),get)))]()
    #修改菜单栏状态codeStatus 可bool对象 可bool对象 ...
    def menuStatus_l(self=None,get=[]):
        get=get[1:]
        if not get:
            return next(menu_bool_call)()
        bools={True:menu_bool_call.l[0],False:menu_bool_call.l[1]}
        #如果传入的参数有一个bool为False 则结果为False(以后专门写一个判别器可以自定义逻辑门路)all()或any()达到同样效果
        return all(get)#bools[not bool(tuple(filter(lambda i:not bool(eval(i)),get)))]()
    #将文本框[大]中的文本初始化为代码函数并返回 compile -e/-r -t 
    def compile_l(self=None,get=[]):
        get=get[1:]
        stt=text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        st={stt:stt,'':text.get('1.0', tk.END)}[stt]
        sbp,gea='exec',['']
        sbp='eval' if get.count('-r') else 'exec' if get.count('-e') else sbp
        if get.count('-t'):#设置代码文件名
            ind=get.index('-t')
            gea=get[ind+1:ind+2]
            print(gea)
        return compile(st,gea[0],sbp)
    #将文本框[大]中的文本(也可以是选中文本)初始化为原始代码compile对象并返回
    def single_l(self=None,get=[]):
        get=get[1:]
        txt=text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        txt={txt:txt,'':text.get('1.0', tk.END)}[txt]
        gea=['']
        if get.count('-t'):#设置代码文件名
            ind=get.index('-t')
            gea=get[ind+1:ind+2]
        return compile(txt.replace('\n',';'),gea[0],'single')
    #运行选中的代码
    def callr_l(self=None,get=[]):
        get=get[1:]
        txt=diy('Text')
        #txt=txt if txt else 
        try:
            return exec(txt,Clsr.glo,Clsr.loc)
        except BaseException as e:
            return f'Err: {e}'
    #直接用py运行文本框[F5]
    def cal_l(self=None,get=[]):
        get=get[1:]
        get=Ml.compile_l(get=get)
        return eval(get,Clsr.glo,Clsr.loc)
    #批量调用[命令栏的cmd]命令[函数优先] 可以配合compile使用>>>call compile;单独使用时同直接输入>>call l=0;等同>>l=0;
    def call_l(self=None,get=[]):
        get=get[1:]
        if get:
            get=Ml.compile_l(get=get) if get[0]=="compile" else get
        try:
            return eval(get,Clsr.glo,Clsr.loc)
        except:
            '''
            try:
                print(1)
                return eval(' '.join(get),Clsr.glo,Clsr.loc)
            except:
                try:
                    raise
                    print(2)
                    return [eval(i,Clsr.glo,Clsr.loc) for i in get]
                except:
                    try:
                        raise
                        print(3)
                        return exec(' '.join(get),Clsr.glo,Clsr.loc)
                    except:
            
            try:
                print(4)
                din=diy(' '.join(get))
                return eval(str(din),Clsr.glo,Clsr.loc)
            except:
            '''
            try:
                raise
            except:
                try:
                    return [diy(i) if i not in ['',' ']else i for i in(i+' ' for i in diy(' '.join(get)).split('\n'))]
                except BaseException as e:
                    try:
                        return diy((diy(' '.join(get))).replace('\n',' \n')+' ')
                    except IndexError as e:
                        pass
                    except BaseException as e:
                        #print(e)
                        try:
                            return [diy(i) if i not in ['',' ']else i for i in(i+' ' for i in get)]
                        except:
                            return Ml.__err_on(get=get,e=e)
        
    #内部函数用于打印报错信息
    def __err_on(get=[],e=None):
        try:
            gn='\n'
            ej_str=str(diy(' '.join(get))).replace(gn,' \n')+' '
            int_ej=ej_str.find(e.name)
            ej1=ej_str[:int_ej];
            ej2=ej_str[int_ej+len(e.name)+1:]
            inx1= ej1[ej1.rfind(gn,2):] if ~ej1.rfind(gn,2) else gn
            inx2=ej2[:ej2.find(gn,1)] if ~ej2.find(gn,1) else gn
            ff=f"{inx1}lin:{ej1.count(gn)+1}-->{e.name}"+inx2+'\t'
            print('...\n✘:',ff,'\n....\n',' ↘无法直接调用已放弃该调用方法:',e,'\n')
        except IndexError as e:
            pass
        except:
            raise e
    #逐行运行Text脚本不进行解释报错则返回报错以后命令的迭代器 callt [./-x(跳过报错)]
    def callt_l(self=None,get=[]):
        get=get[1:]
        if get:
            txter=0 if get[0]=='-x' else 1
        else:
            txter=1
        tx=diy('Text')
        #print('调用',tx,type(tx))
        gtta=(tx).split('\n')
        for i in range(len(gtta)):
            try:
                diy(gtta[i])
                #yield ''
            except:
                try:
                    if txter:
                        for j in gtta[i:]:
                            yield j
                    raise
                except:
                    continue
    #nt==next
    def next_l(self=None,get=[]):
        get=get[1:]
        return [eval(f'next({i})',Clsr.glo,Clsr.loc) for i in get]
    #删除文本框中的指定文本
    def delete_l(self=None,get=[]):
        get=get[1:]
        print(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        #[if diy(i)==text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST) for i in get]
        #text.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    #创建一种字体并返回 font [参数]:[值] [参数]:[值]... 如 font family:'微软雅黑' size:10
    def font_l(self=None,get=[]):
        import tkinter.font
        get=get[1:]#.split(';')
        if not get:
            return tkinter.font.names()
        ge=(",".join(get)).replace(':','=')
        se=f"""tkinter.font.Font({ge})"""
        print(se)
        return eval(se,dict(Clsr.glo,**globals()),Clsr.loc)
    #设置默认的root.tag_config的参数 tag_config [位置(默认是选中区域)/-r(重置)] [参数]=[值]...如tag_config foreground='red' font=ft
    def tag_config_l(self=None,get=[]):
        get=get[1:]
        if get:
            if get[0]=='-r':
                Ml.tag=''
                return Ml.tag
            if '=' not in get[0]:
                text.tag_add('tag',get[0])
                get=get[1:]
            else:
                text.tag_add('tag',tkinter.INSERT)
        ge=",".join(get)
        eval(f"""text.tag_config('tag',{ge})""",dict(Clsr.glo,**globals()),Clsr.loc)
        Ml.tag='tag'
        return Ml.tag
    #将变量插入文本框[大],如果不能识别则会直接插入原文 input [变量/-r(不检测变量直接插入所输文字)]<空格>[变量]...注意:如果使用';'前面加空格则是返回数组
    def input_l(self=None,get=[]):
        get,bol=(get[2:],True)if len(get)>1 and get[1]=='-r' else (get,False)
        try:
            if bol:
                text.insert(tkinter.INSERT,' '.join(get).replace('\\n', '\n'),Ml.tag)
            else:
                text.insert(tkinter.INSERT,Ml.call_l(get=get),Ml.tag)
        except:#如果call不行就变为字符串
            get=' '.join([i.replace(';;',';') for i in get[1:]]) if get[-1]!=';' else get[1:-1]
            text.insert(tkinter.INSERT,get,Ml.tag)
    #向ChatBot发送信息并返回 CB [参数]      
    def CB_l(self=None,get=[]):
        try:
            try:
                txt=call_CB.run(str(diy(' '.join(get[1:]))),config=call_CB.cook)
            except NameError:
                txt=call_CB.run(' '.join(get[1:]),config=call_CB.cook)
            return txt.strip()
        except BaseException as e:
            return print('运行失败:',e)
    #向openai发送信息并返回 openai [参数]
    def openai_l(self=None,get=[]):#set tt=openai 正弦交流电的原理是什么
        try:
            try:
                txt=openAI.run_openai(str(diy(' '.join(get[1:]))),Ml.openAi_engine,'正在思考\n','传输完成\n',**Ml.openAi_dict)
            except NameError:
                txt=openAI.run_openai(' '.join(get[1:]),Ml.openAi_engine,'正在思考\n','传输完成\n',**Ml.openAi_dict)
            return txt["choices"][0]["text"].strip()
        except BaseException as e:
            return print('运行失败,你可能没有使用engine设置使用型号或其他原因输入不合法:',e)
    #设置openai的型号/登录/查看 openai [mods/-r] [-r/mods] [-r要添加的参数]
    def engine_l(self=None,get=[]):
        mods=["text-ada-001",'text-curie-001','text-babbage-001',
              'text-davinci-001','text-davinci-002','text-davinci-003',
              'code-cushman-001','code-davinci-002']
        if not get[1:]:
            print('额外参数:',Ml.openAi_dict,mods,'以上是常用的模型更多模型请使用 openai --list/??')
        elif get[1] in mods:
            openAI.login()
            Ml.openAi_engine=get[1]
            return Ml.openAi_engine
        elif '-r' in get[1]:
            ge=tuple(filter(lambda i:i not in mods,get[1:][get.index('-r'):]))
            dic={}
            call=';'.join(ge)
            exec(call,Clsr.glo,dic)
            Ml.openAi_dict=dic
        if Ml.openAi_engine:
            openAI.login()
    
    help_dict={'-a':lambda get:tuple(filter(None,(dir_exp.fd.find_set(ds_key,i) for i in get[1:]))) if get[1:] else ds_key,
               '-f':lambda get:tuple(filter(None,(dir_exp.fd.find(ds_key,i) for i in get[1:]))) if get[1:] else ds_key,
               '-l':lambda get:tuple(filter(None,(dir_exp.fd.find(ds_key,i) for i in get[1:]))) if get[1:] else ds_key,
               '-d':lambda get:'\n\n'.join((get_doc.try_code_doc(eval(f"{Ml._mro[0]}.{i}_l")) for i in get[1:])),
               '-h':lambda get:[get_doc.try_code_doc(eval(f"{Ml._mro[0]}.{i}_l")) for i in get[1:]],
               '-c':lambda get:[get_doc.cond_doc(eval(f"{Ml._mro[0]}.{i}_l")) for i in get[1:]],
               '-r':lambda _:None,
               '-t':lambda _:None}
    #帮助
    def help_l(self=None,get=[]):
        get=get[1:]
        try:
            if not get:
                print(lin_dic.keys())
                print('文本框附加快捷键:',lin_dic.keys(),
                    '\n','输入help -a [搜索包含的字符(可空)] 查看所有命令',
                      '\n','输入"help 命令"查看对命令的简单说明','\n',
                      '命令框支持所有py模块并输出等同idle的内容,','\n',
                      '输入cmd [要执行的py命令] 进行测试','\n',
                      '默认执行是全局环境下可能会出现变量名冲突','\n',
                      '使用exec [输入环境(一般是字典变量)] [输出环境(一般是输入环境)]',
                      '改变运行环境','\n','如果动态添加命令时出现问题请在默认的全局环境下键入reformat()格式化类命令',
                      '\n','如果在UI界面可以试着将文件直接拖入文本框或命令框快捷写入'
                      '\n','Ctrl+l区域截图到调用路径 Alt+l区域截图到当前路径 Ctrl+k 截图并取词插入到文本框 \n Ctrl+u开关继承保存 Ctrl+p开关导入覆盖'
                      '\n','"变量就是命令,命令就是字符串"'
                      )
            #print(get)
            print('Ml[命令存储类]:',Ml.help_dict[get[0]](get) if get[0] in Ml.help_dict else
                  [help(eval(f"{Ml._mro[0]}.{i}_l")) for i in get])
        except:
            try:
                [help(eval(Ml._mro[1]+i)) for i in get]
            except:
                [help(eval(i,*eval(Ml._mro[2]))) for i in get]
    #输出help的调用顺序#"""可以通过输入 Ml._Ml_mro 起到同样效果"""
    def mro_l(self=None,get=[]):
        print(Ml._mro)
    #需要提前赋值的变量加在Ml末尾(只在Ml中的规范)
    _mro=('Ml','','Clsr.glo,Clsr.loc')
    m=locals();Clsr.glo,Clsr.loc=globals(),globals();encoding,errors='UTF-8','ignore';add_open='.'
    nt=4;tag='';openAi_engine="text-davinci-003";openAi_dict={}
    #m[' ']=m['_l'] encoding='gb18030'/'gbk';'UTF-8','ignore'
    
#重置环境
def reformat(*v):
    return Ds_(Ml)
#将主程序环境变量传递过来
def fff(ld=None,go=globals(),*n:'func'):
    gol=globals()
    gol.update(go)
    global lin_dic
    lin_dic=ld
    try:
        for i in n:
            go[i.__name__]=i
    except:
        pass
    
