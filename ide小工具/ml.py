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
        get=' '.join(get[1:]).split(';')
        ge=tuple((i.split('=') for i in get))
        bt=Byte(0)
        try:
            [(exec(f"{i[0]}=diy(i[1])",locals(),Clsr.loc),++bt) for i in ge]
        except:#下面这句不是抄的就是写着玩
            print('The parameter was not found in the commands/scope:',ge[int(bt.byte())][-1])
            try:
                diy(' '.join(get))
            except:
                [eval(i,Clsr.glo,Clsr.loc) for i in get]
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
    #可设置结束符的echo print [变量/end='结束字符'(默认是空字符'')]...[变量]
    def print_l(self=None,get=[]):
        end='\n' if not get[1:] else get[2] if get[1] =='end' else ''
        get= get[2:] if not end in ('\n','') else get
        Ml.echo_l(self,get=get,end=end)
    #直接输入目录打开文件 open [目录/网址(如果是网址则返回requests.get对象)] [目录]...
    def open_l(self=None,get=[]):
        try:
            return roo_d(get[1:])
        except:
            if len(get[1:])==1:
                return requests.get(get[1])
    #设置文件读取方式 open 'rb'[\...]或者open read [int](读取长度) 
    def set_open_l(self=None,get=[]):
        global rsr,reado
        if get[1] in ['read',]:
            reado=int(get[2])
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
            return text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except:
            return text.get('1.0', tk.END)
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
    
    def __say_api_ce(get,lang='zh'):
        try:
            return [engapi.txchemp(str(diy(i)),lang) for i in get[1:]]
        except:
            return engapi.txchemp(' '.join(get[1:]),lang)
    #字符串转音频并播放 say [eng/.] [变量]
    def say_l(self=None,get=[]):
        get=get[1:]
        if get:
            if get[0]=='eng':
                try:
                    return [engapi.txengmp(str(diy(i))) for i in get[1:]]
                except:
                    return engapi.txengmp(' '.join(get[1:]))
            #elif get[0]=='ce':
                #Ml.__say_api_ce(get)
            elif get[0] in engapi.yd_lang:
                Ml.__say_api_ce(get,get[0])
            else:
                Ml.__say_api_ce([':']+get)
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
        if Ml.add_open.endswith(".py"):
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
    #快捷调用字典[一般是模块组成的字典]中的对照,默认给定的字典中的元素是py程序包
    def run_l(self=None,get=[]):
        pass
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
    def jsonw_l(self=None,get=[]):
        get=get[1:]
        lin()
        st= str(globals()) if not get[1:] else str([diy(i) for i in get[1:]])
        rs= '..' if not get else askopenfilename(title=u'写入js') if get[0]=='open' else get[0]
        with open(rs+'\ce.json','w',encoding='utf-8') as file:
            file.write(json.dumps(st,indent=2,ensure_ascii=False))
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
    #将文本框[大]中的文本初始化为代码函数并返回 compile -e/-r -t 
    def compile_l(self=None,get=[]):
        get=get[1:];st=text.get('1.0', tk.END)
        sbp,gea='exec',['']
        sbp='eval' if get.count('-r') else 'exec' if get.count('-e') else sbp
        if get.count('-t'):#设置代码文件名
            ind=get.index('-t')
            gea=get[ind+1:ind+2]
            print(gea)
        return compile(st,gea[0],sbp)
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
        gtta=(tx).split('\n')
        for i in range(len(gtta)):
            try:
                diy(gtta[i])
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
    #将变量插入文本框[大],如果不能识别则会直接插入原文 input [变量/-r(不检测变量直接插入所输文字)]<空格>[变量]...注意:如果使用';'前面加空格则是返回数组
    def input_l(self=None,get=[]):
        get,bol=(get[2:],True)if len(get)>1 and get[1]=='-r' else (get,False)
        try:
            if bol:
                text.insert(tkinter.INSERT,' '.join(get).replace('\\n', '\n'))
            else:
                text.insert(tkinter.INSERT,Ml.call_l(get=get))
        except:#如果call不行就变为字符串
            get=' '.join([i.replace(';;',';') for i in get[1:]]) if get[-1]!=';' else get[1:-1]
            text.insert(tkinter.INSERT,get)
    #帮助
    def help_l(self=None,get=[]):
        get=get[1:]
        try:
            print(lin_dic.keys())
            if not get:
                print('文本框附加快捷键:',lin_dic.keys(),
                    '\n','输入help<空格>-a查看所有命令',
                      '\n','输入"help<空格>命令"查看对命令的简单说明','\n',
                      '命令框支持所有py模块并输出等同idle的内容,','\n',
                      '输入cmd<空格>[要执行的py命令] 进行测试','\n',
                      '默认执行是全局环境下可能会出现变量名冲突','\n',
                      '使用exec<空格>[输入环境(一般是字典变量)]<空格>[输出环境(一般是输入环境)]',
                      '改变运行环境','\n','如果动态添加命令时出现问题请在默认的全局环境下键入reformat()格式化类命令',
                      '\n','"变量就是命令,命令就是字符串"'
                      )
            print('Ml[命令存储类]:',ds_key if get[0]=='-a'else
                  [help(eval(f"{Ml.__mro[0]}.{i}_l")) for i in get])
        except:
            try:
                [help(eval(Ml.__mro[1]+i)) for i in get]
            except:
                [help(eval(i,*eval(Ml.__mro[2]))) for i in get]
    #输出help的调用顺序#"""可以通过输入 Ml._Ml__mro 起到同样效果"""
    def mro_l(self=None,get=[]):
        print(Ml.__mro)
    #需要提前赋值的变量加在Ml末尾(只在Ml中的规范)
    __mro=('Ml','','Clsr.glo,Clsr.loc')
    m=locals();Clsr.glo,Clsr.loc=globals(),globals();encoding,errors='UTF-8','ignore';add_open='.'
    nt=4;
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
    
