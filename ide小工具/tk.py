#-*- coding:utf-8 -*-

#from progress.bar import Bar
import USE,os,sys,psutil

if 'linux' in sys.platform:
    USE.pip_install=f"python{sys.version_info.major}.{sys.version_info.minor} -m pip install "+"{mod}"
    
USE.pip_dict={}
import_pub_tuple=({'np': 'numpy'},
                  'engapi', 'M_t', '扫图', '截屏', '腾讯识图', 'clk', '保存全局变量', 'tkinter', 'json', 'jsonlines', 'javalang',
                  'requests', 'pickle', 'ctypes', 'windnd', 'multiprocessing', 'compileall', 'dir_exp', 'newts', '类', 'openAI','call_CB','tab_list',
                  'get_doc',
                  ('tkinter', 'tk'),
                  {'BOOT':('*',),'idlelib':('searchengine',),'idlelib.search':('SearchDialog',),
                    'concurrent.futures': ('ThreadPoolExecutor',), 'threading': ('Thread', 'current_thread'),
                   'tkinter.filedialog': ('askdirectory', 'askopenfilename', 'asksaveasfilename'), 'queue': ('Queue',),
                   'tkinter.messagebox': ('showinfo', 'askyesno')})
try:
    #判断如果在idle中运行则跳过进度条
    print_bool =False if psutil.Process(os.getppid()).name()=="pythonw.exe" else True
    #执行批量导入
    USE.use(*import_pub_tuple,glo=globals(),print_bool=print_bool)
    #无法批量导入的模块:
    from idlelib.multicall import MultiCallCreator
    import idlelib.colorizer as idc
    import idlelib.percolator as idp
    import idlelib.autocomplete as aut
    from ml import *
    print('',end='-')
    import 摩斯
    print('',end='-')
    import byte_
    print('',end='-')
    import 翻译
    print('',end='>')
    text_Translation=翻译.tetr
    Byte=byte_.Byte
    Css=类.Css
    #Ml=Ml(name='工作空间')
except BaseException as e:
    print('模块导入异常:',e)
#打包时的额外参数
try:
    with open(os.path.split(sys.argv[0])[0]+r'\help.help','rb') as f:
        help=pickle.load(f)
except:
    with open(sys.path[3].rsplit('\\',1)[0]+r'\help.help','rb') as f:
        help=pickle.load(f)
#必要的全局参数
rsr='r';wsr='w';reado=None;
run_loop=lambda x=None:x
roo_soo_bool=True
inherit_bool=False
Test_bool=False
inherit_bool_dict={False:lambda *v,**k:None,True:保存全局变量.run_dump}
Type_in_iter=lambda d:type(d) in (set,list,tuple,dict,)

#启动自动运行调用配置Boot_Start,Boot_Ing,Boot_End =(初始化窗口前,启动窗口时,窗口关闭后):type(compile) 
Boot_file_path_dir_exp=dir_exp.Mou(os.path.dirname(__file__))
if Boot_file_path_dir_exp/'Boot':
    Boot_path_tuple=(Boot_file_path_dir_exp['Boot']['Boot_Start*'],Boot_file_path_dir_exp['Boot']['Boot_Ing*'],Boot_file_path_dir_exp['Boot']['Boot_End*'])
    (Boot_Start,Boot_Ing,Boot_End)=(
compile(Boot_file_path_dir_exp_bool_func([Boot_path_tuple[0]]) if type(Boot_path_tuple[0])!=list else Boot_file_path_dir_exp_bool_func(Boot_path_tuple[0]),'','exec'),
compile(Boot_file_path_dir_exp_bool_func([Boot_path_tuple[1]]) if type(Boot_path_tuple[1])!=list else Boot_file_path_dir_exp_bool_func(Boot_path_tuple[1]),'','exec'),
compile(Boot_file_path_dir_exp_bool_func([Boot_path_tuple[2]]) if type(Boot_path_tuple[2])!=list else Boot_file_path_dir_exp_bool_func(Boot_path_tuple[2]),'','exec'),
)
else:
    Boot_Start,Boot_Ing,Boot_End=(compile('','','exec'),compile('','','exec'),compile('','','exec'))
#screenshots C:\Users\saysky\Desktop\pyLi\1.png C:\Users\saysky\Desktop\pyLi\2.png
try:
    try:
        lod=sys.path[3].rsplit('\\',1)[0]+'\\'+'global.log'
        bianl=dict(保存全局变量.run_load(lod=lod))
    except:
        lod=os.path.split(sys.argv[0])[0]+'\\'+'global.log'
        bianl=dict(保存全局变量.run_load(lod=lod))
except EOFError as e:
    bianl=dict()
    os.unlink(lod)
except BaseException as e:
    bianl=dict()
    print('外置环境导入错误:',e)
    try:
        保存全局变量.run_dump({},lod=lod)
    except:
        bianl=dict()
        os.unlink(lod)

#自定义线程添加类
class Tr(Thread):
    def __init__(self,fun:'func',ag:'ages'):
        self.func=fun
        self.age=ag
        super().__init__(target=fun, args=ag)
    def rn(self):
        self.func(*self.age)
        
    #队列put装饰器将函数转换为运行后发送get的方法
    @staticmethod
    def putr(q:'Queue'=Queue()):
        def qus(sf):
            return lambda *v,**k:q.put(sf(*v,**k))
        return qus
    
    #队列get装饰器将函数转换为运行前接收put的方法 put传递的参数会自动传递到函数的第一个形参
    @staticmethod
    def getr(q:'Queue'=Queue()):
        def qus(sf):
            return lambda *v,**k:sf(q.get(),*v,**k)
        return qus
    #这里可以异步创建线程在等待返回值时协程创建其他线程,也可以创建一个列表打包操作
    def st(self=None):
        self.start()
        return self
    #创建一个线程池(异步并发)
    def pool(workers=3,works_name='None'):
        pool=ThreadPoolExecutor(max_workers=workers, thread_name_prefix=works_name)
        return pool
    #返回一个已经创建好的临时函数用于非直接调用
    def aknt(self=None,*vg,**sk):
        try:
            self.akn
            return lambda *eve:self.akn(*vg,**sk)
        except AttributeError:
            return lambda *eve:Tr.akn(*vg,**sk)
    #批量实例添加并运行线程函数[适合用于分段执行的中量请求数据](这里可以使用异步)
    @staticmethod#使用静态装饰器声明为类的'工具包'
    def akn(func_tp:[list,tuple,iter]=(),ages:[list,tuple,iter]=[(None,),],join_ont:bool=True,pool:'线程池'=None):
        if bool(pool):
            [pool.submit(func_tp[i],ages[i]) for i in range(len(func_tp))]
        else:
            if len(func_tp)!=len(ages):
                #raise '函数与实参长度不匹配'
                print('函数与实参长度不匹配')
                ages=ages[:len(func_tp)]
            tc=[Tr(func_tp[i],ages[i]).st() for i in range(len(func_tp))]
            if join_ont:
                Tr.in_join(tc)
    @staticmethod
    def in_join(tc):
        return [i.join() for i in tc]
    long=False
    fun,lois=None,[]
#自定义菜单添加类
class Me(tk.Menu):
    add_arg_tuple=tuple(filter(lambda i:i!='add',(i.split('_',maxsplit=1)[-1] for i in dir_exp.rust_find_dir(tk.Menu,'add'))))
    #@staticmethod 一次批量添加子菜单并绑定主菜单
    def add_Submenu_bat(self:'主菜单对象',name:'菜单名_{类型}',dic:dict):
        menu=Me(self, tearoff=False)
        name_list=name.rsplit('_',maxsplit=1)
        arg,name={True:name_list[-1] ,False:None}[name_list[-1]in self.add_arg_tuple],name_list[0]
        [(self.add(arg,label=name,**{type(l[-1]):{'command':l[-1]},dict:l[-1]}[type(l[-1])]))if arg else menu.add_bat(dict((l,)))for l in dic.items()]
        self.add_cascade(label=name,menu=menu)
    #@staticmethod 批量添加子菜单
    def add_command_bat(self,dic:dict)->list:
        return [self.add_command(label=l[0],**l[1]) for l in dic.items()]
    #@staticmethod 批量绑定选项
    def add_cascade_bat(self,dic:dict)->list:
        return [self.add_cascade(label=l[0],**l[1]) for l in dic.items()]
    #可选批量的操作类型
    def add_bat(self,dic:dict)->list:
        return [(self.add(i[0].rsplit('_',maxsplit=1)[-1],label=i[0].rsplit('_',maxsplit=1)[0],**{type(i[-1]):{'command':i[-1]},dict:i[-1]}[type(i[-1])]))
            if i[0].rsplit('_',maxsplit=1)[-1] in Me.add_arg_tuple else
            self.add_command(label=i[0],**{type(i[-1]):{'command':i[-1]},dict:i[-1]}[type(i[-1])])for i in dic.items()]
    #批量递归添加子菜单
    def add_recursion_bat(self,dic:dict)->list:
        menu=Me(self, tearoff=False)
        return [(menu.add_recursion_bat(i[-1]),self.add_cascade(label=i[0],menu=menu)) if type(i[-1])==dict else (self.add_bat(dict((i,))),self.add_cascade(label=i[0],menu=menu)) for i in dic.items()]
#定长列表
class Lins(list):
    le=5
    def __init__(self,length:int=5,*a,**k):
        """
        默认lenfth[长度]是5无论传入多少参数list长度保持一定
        """
        self.le=length if length else self.le
        super().__init__(*a,**k)
    def __repr__(self):
        self[:]
        return str(self.__reduce__()[1][2])
    def __getitem__(self,i):
        try:
            del self[:-self.le]
            return Lin(self.le,self.__reduce__()[1][2][i])
        except:
            return super().__getitem__(i)
    def encode(s):
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
    def decode(s):
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
    def code(s):
        return ' '.join([ord(c) for c in s])
    def rcode(s):
        return ''.join([chr(i) for i in s.split(' ')])

class Dio:#通用无限迭代器
    def __init__(self,lis:list):
        self.l=list(lis)
        self.col=0
    def __next__(self):
        try:
            return self.l[self.col]
        except:
            self.col=0
            return self.l[self.col]
        finally:
            self.col+=1
#全局变量的映射类
class Glo_port:
        def __new__(cls):
            self=super().__new__(cls)
            self.__dict__=globals()
            return self
        def update_Glo_port(self):
            self.__dict__=globals()
g_l=Glo_port()
#打印的os.popen方法
def cmd_popen(sys):
    cmd=os.popen(sys,buffering=1).read()
    print(cmd)

def lop(list_:[list,tuple]):#循环索引
    len_l=len(list_)-1
    li=0
    def lj(it:int):#索引跨度
        nonlocal li,len_l
        li=0 if li>=len_l or li+it>len_l else li+it
        return li#返回索引值
    return lj#闭包
#弹出保存文件窗口以保存文件
def soo(eve=None):
    try:
        pat=Ml.add_open if os.path.split(Ml.add_open)[1]!=Ml.add_open and roo_soo_bool else asksaveasfilename(title=u'保存文件')
        with open(pat,wsr,encoding=Ml.encoding,errors=Ml.errors) as f:
            f.write(text.get('1.0', tk.END))
        root.title(root_name+f': {pat}')
    except:
        print('soo出错',eve)
#打开文件:rsr在全局中指定
def roo_open_file(pat,rsr=rsr,rd=True):
    global reado
    try:#这里可以写成依次调用所有的编码直到解出或报错
        try:
            pat=str(pat,'utf-8')
        except:
            pat=pat.decode()
    except:
        try:
            pat=str(pat,encoding='gbk')
        except:
            pat=str(pat)
    with open(pat,rsr,encoding=Ml.encoding,errors=Ml.errors) as f:
        data=f.read(reado)
        if rd:
            lb.delete('1.0','end')
        sot=str(data)
        lb.insert(tkinter.END,sot.rstrip())
        #保存打开的文件路径(方便了操作文件目录的命令)
        Ml.add_open=pat
        root.title(root_name+f': {pat}')
#弹出打开文件窗口以打开文件
def roo(eve=None):
    try:
        global rd
        pat=askopenfilename(title=u'打开文件')
        roo_open_file(pat,rsr,rd)
    except BaseException as e:
        print('roo出错',e)
#以其他方式打开文件(如拖拽)
def roo_d(pat='.'):
    try:
        global rd
        #print(f"open: {pat}")
        pd_bool=Type_in_iter(pat) and len(pat)>1
        if pd_bool:
            if askyesno('批处理','当前拖入[输入]多个文件,是否开辟新进程打开?'):
                pdl=[(f"tk cmd [roo_open_file({roo_d(i) if Type_in_iter(i) else i})]") for i in pat]
                Tr.akn((*eval("cmd_popen,"*len(pdl)),j.mainloop),[*pdl,()],pool=pool_Ml)
            else:
                roo_open_file(roo_d(pat[-1]) if Type_in_iter(pat[-1]) else pat[-1],rsr,rd)
        else:
            roo_open_file(pat[-1] if Type_in_iter(pat) else pat,rsr,rd)
    except not OSError as e:
        print('roo出错',e)
#扫图写入
def clkn(api='bd'):
        global text
        plo=os.path.split(lod)[0]+r'\sept.png'
        try:
            txt=clk.run_q(plo,js=os.path.split(lod)[0]+'\\account.json',api=api)
        except BaseException as e:
            return print('非正常退出:',e)
        if txt!='&正常退出':
            lb.insert(tkinter.INSERT,txt)
        print(txt)
#设置是否继承保存(保存不用重选)
def roo_bool(*e):
    global roo_soo_bool
    roo_soo_bool=rd=False if roo_soo_bool else True
    result = tkinter.messagebox.showinfo(title = '提示',message=f'继承保存：{roo_soo_bool}')
#导入文件覆盖开关
def ro(eve=None):
    global rd
    rd=0 if rd else 1
    return bool(rd)
#设置导入文件是否覆盖
def zhr(eve=None):
    op=ro()
    result = tkinter.messagebox.showinfo(title = '提示',message=f'打开覆盖：{op}')
def cmds(eve=None):
    global rr
    try:
        rr.col=rr.col if eve.keysym=='Up' else rr.col-2
        cmd.select_clear()
        cmd.delete(0,tk.END)
        jjh=j_lins[next(rr)]
        cmd.insert('end',jjh)
    except:
        #print('动作无效',eve.keysym,end='')
        pass

#检测并执行Ml命令
def diy(get:str,test=False):#检测并执行Ml命令
    global rsr,wsr,reado
    gee=list(filter(lambda x:bool(x),get.split('; ')))
    if not gee:
        return None
    elif len(gee)>1:
        [diy(ge) for ge in gee]
    elif gee[0] and not Tr.long:#这里写的有问题
        ge=gee[0].split()
        if ge[0] in ds_key:
            return dds[ge[0]](get=ge)
        else:#diy('Text')
            try:
                return eval(get,Clsr.glo,Clsr.loc)
            except:
                return exec(get,Clsr.glo,Clsr.loc)
    elif Tr.long:#以后会大改
        Tr.lois +=gee if Tr.lois else []
        gp=gee[0].split(' ')
        if gp[0]=='new':
            try:
                Tr.fun=gp[1]
                Tr.lois=gee[:]
                Tr.dicp=newts.stat[Tr.fun]
            except KeyError:
                return 
        elif 'end' in gee[0]:
            Ml.end_l()
            psvn='\n'.join(Tr.lois)
            psvm=newts.parse(psvn,newm=Tr.fun)
            pd=Tr.dicp(psvm=psvm)
            Tr.lois=[]
            if Tr.fun=='func':
                l={}
                [exec(i,dict(Clsr.glo,**globals()),l) for i in pd]
                [Ml.self_examination(i) for i in l.values()]
            #cmd必须要有形参接受命令行参数!!
            elif Tr.fun=='cmd':
                l={}
                [exec(i,dict(Clsr.glo,**globals()),l) for i in pd]
                [Ml.self_examination(i) for i in l.values()]
            elif Tr.fun=='def':
                [exec(i,Clsr.glo,Clsr.loc) for i in pd]
            elif Tr.fun in newts.stat:
                import ming_language.code
                try:
                    psvm=newts.parsex(psvn,newm=Tr.fun)
                    value_dict=ming_language.code.Long.__dict__[Tr.fun](psvm)
                    Clsr.loc.update(dict(value_dict))
                except BaseException as e:
                    print(f"err: {e}")
            else:
                return
            if test:
                print('构造函数','ok!!!:')
                print(Tr.fun,Tr.lois,Tr.dicp)
            #刷新Ds_ (以后改为__get__动态获取)
            Ds_(Ml);congzai_Ml()
            #刷新着色器
            flushed_prog(user_keywords=Ds_.ds_key)
        #[newts.stat[Tr.fun][1](n=psvm[0][i][0],i=pd[i],l=Clsr) for i in range(len(pd))]
        else:
            #print('>>>',gee)
            pass
        #diy(gee[0])
            

#接收回车并执行diy命令
def ent(event=None):#接收回车并执行diy命令
    global rr,Error
    try:
        md=cmd.get()
        (j_lins.append(md) if md not in j_lins else 0)
        diy(md)#执行diy
        rr=Dio(range(len(j_lins))[::-1])
        cmd.delete(0, 'end')
    except BaseException as e:
        #获取异常记录
        err=sys.exc_info();Clsr.glo['Error']=Error=err[-1]
        print('ent出错',e,f'\n回调:\n\t Err:{err[0].__name__}(Error={Error})\n\t[可在全局变量中访问Error对象获取详情]')

#同步text快捷键和命令
def lin(self=None,dic:dict={}):
    fff(dic,go=globals())
    return [text.bind(k,v) for k,v in dic.items()]#表达式循环快速绑定快捷键
#同步cmd快捷键和命令
def cmd_lin(self=None,dic:dict={}):
    return [cmd.bind(k,v) for k,v in dic.items()]#表达式循环快速绑定快捷键
#同步text右键菜单
def click_lin(self=None,dic:dict={}):
    global popupment
    popupment = tkinter.Menu(lb, tearoff=False)
    return [(popupment.add(i[0].rsplit('_',maxsplit=1)[-1],label=i[0].rsplit('_',maxsplit=1)[0],**{type(i[1]):{'command':i[1]},dict:i[1]}[type(i[1])]))
    if i[0].rsplit('_',maxsplit=1)[-1] in Me.add_arg_tuple else
            popupment.add_command(label=i[0],**{type(i[-1]):{'command':i[-1]},dict:i[-1]}[type(i[-1])])for i in click_dic.items()]
#快速添加text右键菜单
def click_add(name='',func=lambda *e:None):
    return popupment.add_command(label=name,command=func)
#重新导入并同步快捷键和命令call Text
def congzai_Ml():
    exec('from ml import *',locals(),globals())
    fff(lin_dic,go=globals())
def jv(*g,**k):
    if len(g)>1:
        return 0
    get=[]
    tree,add_open=Ml.javae_l(get=[':','Text'])#获取java语法解析树和保存目录
    classs=tree.types[0]#解析类方法
    if not isJVMStarted():
        jvmArg = "-Djava.class.path=" + add_open
        try:
            startJVM(getDefaultJVMPath(),jvmArg)
        except:
            pass
    javaClass = JClass(classs.name)
    ldrn=[javaClass.__dict__[i] for i in get]  if get else javaClass.main(None)
    shutdownJVM()
    return ldrn
#登录ChatBot
def login_ChatBot():
    try:
        with open(os.path.split(lod)[0]+'\\login_ChatBot.json','r') as f:
            fid=json.loads(f.read())
            call_CB.cook=fid
    except BaseException as e:
        print('无法登陆ChatBot:',e)
#运行ChatBot并打印
def run_ChatBot():
    txt=diy('Text')
    print('请求中')
    print(call_CB.main(txt=txt,config=call_CB.cook))


#重载click_dic
def click_r():
    global click_dic,menu_bool_call
    def translate_input(*e):
        txt=diy('translate Text')
        diy('input '+txt)
        try:
            lb.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except:
            pass
        return txt
    def translate_input_say(*e):
        txt=translate_input()
        say=lambda txt:diy('say '+txt)
        Tr.akn((say,j.mainloop),[(txt),()],pool=pool_Ml)
    def fid(*e):
        try:
            print(openAI.run_openai(diy('Text'),Ml.openAi_engine,'处理中\n','完成\n',**Ml.openAi_dict)["choices"][0]["text"].strip())
        except:
            print('运行失败,你可能没有使用engine设置使用型号/登录或其他原因输入不合法')
    def fff(*e):
        print('ok')
        import Dtb
        Qu=Dtb.Qu
        fen=Qu(fid)
        print(fen)
        fen()
    def callr_func(*e):
        op=diy('callr')
        op={op:op,None:''}[op]
        print(op)
    #可以通过click_dic添加右键命令
    #创建动态获取bool用于按钮(复选框)同步
    demoStatus = tk.BooleanVar()
    demoStatus.set(False)
    #创建循环开关
    menu_bool_call=Dio([lambda *e:(root.config(menu=mainmenu),demoStatus.set(True)),
                        lambda *e:(root.config(menu=''),demoStatus.set(False))])
    #menu_cs=tk.Checkbutton(text='cs')
    #右键菜单 格式:{'菜单名_{类型(默认是"command")}':options参数字典或可调用对象}
    click_dic={
        '菜单栏开关<F1>_checkbutton':{'command':lambda *e:next(menu_bool_call)(),'variable':demoStatus},
        #'全选':lambda x=0:print(x),
        '说/say':Tr.aknt(None,(diy,j.mainloop),[('say Text'),()],pool=pool_Ml),
        '翻译/translate->input':translate_input,
        '翻译并说译文':translate_input_say,
        #'登入/engine':lambda *e:openAI.login(),
        #'问/openai':Tr.aknt(None,(fid,j.mainloop),[(),()],pool=pool_Ml),
        #'问/ChatBot':Tr.aknt(None,(run_ChatBot,j.mainloop),[(),()],pool=pool_Ml),
        'run/callr<F5>':Tr.aknt(None,(callr_func,j.mainloop),[(),()],pool=pool_Ml),
        'run_cmd/echo callt<F6>':Tr.aknt(None,(lambda *e:diy('echo callt'),j.mainloop),[(),()],pool=pool_Ml),
        #'cs_cascade':{'menu':menu_cs}
        }
#重载lin_dic
def lin_r():
    global lin_dic
    #可以通过lin_dic添加text快捷键命令
    lin_dic={
         '<3>':lambda event:popupment.post(event.x_root,event.y_root),
         '<Control-s>':soo,'<Control-o>':roo,'<Control-p>':zhr,
         '<F1>':lambda *e:next(menu_bool_call)(),
         '<F5>':lambda *e:Ml.call_l(e,get=(':',"compile" ,)),#用队列线程比较好Tr.aknt(None,(Ml.Single_thread,j.mainloop),[(),()])
         '<F6>':Tr.aknt(None,(lambda *e:diy('echo callt'),j.mainloop),[(),()],pool=pool_Ml),
         '<Control-q>':sys.exit,'<Control-l>':lambda e=None:截屏.run(),
         '<Alt-l>':lambda e=None:截屏.run(os.path.split(Ml.add_open)[0]if os.path.split(Ml.add_open)[1]!=Ml.add_open else Ml.add_open+r'\sept.png'),#text.insert
         '<Control-k>':Tr.aknt(None,(clkn,j.mainloop),[('bd'),()],pool=pool_Ml),
         '<Alt-k>':Tr.aknt(None,(clkn,j.mainloop),[('tx'),()],pool=pool_Ml),
         '<Control-u>':roo_bool,'<Tab>':tab_list.printaf,"<<autocomplete>>":tab_list.af.autocomplete_event,
         '<Control-f>':find_tk,
         #'<Key>':lambda e=None:print(e)
         #lambda *e:Ml.Single_thread(e)#用队列线程比较好
             }
#重新同步tab_list环境变量
def lin_tab_list():
    #Clsr.glo.update(Ds_.dds)
    tab_list.af_cmd.main=tab_list.af.main=Clsr.glo
    tab_list.af_cmd.root_dict=tab_list.af.root_dict=Clsr.loc
    tab_list.af_cmd.extra_dict=tab_list.af.extra_dict=Ds_.dds
#获取pool
def pool_ml():
    global pool_Ml
    return pool_Ml
#预分配一个线程池
def pl_m(nt=3):
    global pool_Ml
    pool_Ml=Tr.pool(nt)
#使用idlelib 的搜索
def _setup(text):
    root = text._root()
    engine = searchengine.get(root)
    if not hasattr(engine, "_searchdialog"):
        engine._searchdialog = SearchDialog(root, engine)
    return engine._searchdialog
#使用idlelib 的查找(搜索框)
def find_tk(*e):
    global text
    text.tag_add('sel', '1.0', 'end')
    _setup(text).open(text)
    text.tag_remove('sel', '1.0', 'end')
def Single_thread_bool(add=True,call=Ml.call_l):#重写
    if add:
        if sys.argv[-1]!=';':
            print('单线')
        return lambda event=None:(call(event,get=(':',"compile" ,)),print('《执行》'))
    if sys.argv[-1]!=';':
        print('多线')
    return lambda event=None:Tr.akn((call,j.mainloop),[(),()],pool=pool_Ml)

"""准备启动ide"""

#可视化ide_ui设定 1
def ksh_ide_ui():#lod
    global rd,root,j,root_name
    root_name='查看器'
    rd=1
    root = tk.Tk(className=root_name)
    j=tk.PanedWindow(root)
    #j.geometry("1600x900+500+500")
    #绑定拖拽功能
    windnd.hook_dropfiles(root,func=lambda bat:roo_d(bat))
    
#搭建界面 2
def daj_ide_ui():
    global rd,root,j,jp,cmd,sb,text,lb,put_text,diy_text,flushed_prog,put_cmd
    jp=tk.PanedWindow(orient=tk.VERTICAL,width=800,height=600)
    cmd=MultiCallCreator(tk.Entry)(jp,bd=3,width=20)
    sb = tk.Scrollbar(j,width=20,orient=tk.VERTICAL)
    #sb.resizable(20,1000)
    text=lb = MultiCallCreator(tk.Text)(jp,yscrollcommand=sb.set,undo = True,inactiveselectbackground='gray')
    text.configure(bg=root.cget('bg'))
    sb.config(command=lb.yview)
    #添加代码高亮功能
    idc.color_config(text)
    #idc.color_config(cmd)
    text.focus_set()
    #cmd.focus_set()
    put_cmd = idp.Percolator(cmd)
    put_text = idp.Percolator(text)
    diy_text = idc.ColorDelegator()#设置重新生成对照
    #更新idlelib.colorizer.ColorDelegator对象的prog
    def flushed_prog(self:'ColorDelegator对象'=diy_text,user_keywords:list=Ds_.ds_key):
        import idlelib.colorizer_user_material as colorizer
        colorizer.user_keywords=user_keywords
        colorizer.Define_object_set={*colorizer.Define_object_set}|{*newts.stat.keys()}
        self.prog=idc.make_pat()
    #同步关键字上色
    flushed_prog(diy_text)
    #diy_text.init_state()
    #put_cmd.insertfilter(diy_text)
    #添加代码tab键自动补偿
    tab_list.rden=tab_list.root_dang(text=text,tk=tk,root=root)
    tab_list.af=tab_list.aut.AutoComplete(tab_list.rden)
    #cmd
    tab_list.rden_cmd=tab_list.root_dang(text=cmd,tk=tk,root=root)
    tab_list.af_cmd=tab_list.aut.AutoComplete(tab_list.rden_cmd)
    #加入tab事件连锁(因为事件少所以暂时不做批量处理)
    text.event_add('<<autocomplete>>', '<Key-Tab>')
    #绑定拖拽功能
    als=Codec_tuple
    #循环解码直到能解出
    def pand(bat,l=0):
        try:
            print(als[l])
            return ' '.join((str(i,encoding = als[l]) for i in bat))
        except:
            try:
                return pand(bat,l=l+1)
            except:
                return print('无法解码目录')
    #加载拖拽功能
    windnd.hook_dropfiles(cmd,func=lambda bat:cmd.insert(tkinter.INSERT,pand(bat)))
#添加界面 3
def tan_ide_ui():
    global rd,root,j,jp,cmd,sb,text,lb
    j.add(jp)
    jp.add(lb,width=780,height=560)
    jp.add(cmd,width=780,height=40,minsize=30)
    j.add(sb,width=20,minsize=20)
    j.pack(fill=tk.BOTH,expand=1)

#设置F5执行方式 4
def set_ide_ui(): 
    Ml.Single_thread=Single_thread_bool()
    pl_m(Ml.nt)
    click_r()
    click_lin()
#加载预处理配置 5
def load_ide_config():
    global cmd_bind_dict,code_color_Dio,menu_dict,code_dict
    #加载txt快捷键功能
    lin_r()
    #设置环境变量备份
    log=M_t.Mortise(Log)
    log.dict={}
    Clsr.glo=Clsr.loc=log.dict
    #检测是否导入环境变量
    Clsr.glo.update(bianl)
    #同步tab_list变量
    lin_tab_list()
    #传入diy#将当前环境引入root权限globals接口(可以访问内部环境)
    root.diy,root.text,root.cmd,root.globals,root.root=diy,text,cmd,globals(),g_l
    #绑定命令窗口快捷键
    lb.bind('<3>',lambda event:popupment.post(event.x_root,event.y_root))
    cmd_bind_dict={
        '<2>':lambda *e:print("在鼠标旁添加一个帮助展示窗口当鼠标脱离该窗口后关闭(或隐藏)窗口"),
        '<Return>':lambda *e:Tr.aknt(None,(M_t.Mortise(ent),j.mainloop),[(),()],pool=pool_Ml)(),
        '<Up>':cmds,'<Down>':cmds,'<Control-z>':lambda *e:Tr.aknt(None,(sys.exit,j.mainloop),[(),()],pool=pool_Ml)(),#这个要改成撤销上次输入
        '<Tab>':tab_list.af_cmd.autocomplete_event,"<<autocomplete>>":tab_list.af_cmd.autocomplete_event,
        '<Control-x>':lambda *e:print("快速剪切命令栏里的内容"),'<Control-i>':lambda *e:print('快速将当前内容插入(覆盖)文本框指针位置(选中位置)'),
        '<Control-q>':lambda *e:print('快速将当前内容插入(覆盖)文本框指针位置(选中位置)')
        }
    #运行UI前添加自身作为最高权限
    Clsr.glo['root']=root
    #绑定菜单配置
    cal=lambda *e:print('测试')
    def hule(func=lambda x:x):
        def call(*v,**k):
            try:
                return func(*v,**k)
            except:
                pass
                #print("忽略错误")
        return call
    #put_text,diy_text
    def code_open(*v,**k):
        diy_text.init_state()
        put_text.insertfilter(diy_text)
        code_color_demoStatus.set(True)
    def code_close(*v,**k):
        diy_text.close()
        put_text.insertfilter(diy_text)
        code_color_demoStatus.set(False)
    #这方面自己也忘了我记得能更好的批量添加菜单 还能写成json 先这样了
    menu_dict={'openai':{'command':openAI.login},
               'ChatGPT':{'command':login_ChatBot}
               }
    code_color_Dio=Dio([hule(code_open),hule(code_close)])
    code_color_demoStatus = tk.BooleanVar()
    code_color_demoStatus.set(False)
    code_dict={
        '着色器_checkbutton':{'command':lambda *e:next(code_color_Dio)(),'variable':code_color_demoStatus},
               }
    #加载txt快捷键功能
    lin(dic=lin_dic)
#运行ide 6
def run_ide_ui(test=False):
    global run_loop,inherit_bool,lod,mainmenu
    #运行命令行命令
    run_loop();del run_loop
    #判断尾部是否有分号如果有则退出程序
    if sys.argv[-1]==';':
        try:
            quit()
        except:
            sys.exit()
    #加载命令窗口快捷键
    cmd_lin(dic=cmd_bind_dict)
    #设置图标
    root_image = tk.PhotoImage(file=os.path.split(lod)[0]+r'\logo\Ms.png')
    root.tk.call('wm', 'iconphoto', root._w, root_image)
    #Me可能会优先创建一个空窗口
    mainmenu=Me(root)
    mainmenu.add_Submenu_bat('登录',menu_dict)
    mainmenu.add_Submenu_bat('代码',code_dict)
    congzai_Ml()
    if not test:#判断是否启用调试
        j.mainloop()#等待
    #运行结束后命令
    exec(Boot_End,{**globals(),**Clsr.glo},Clsr.loc)
    
class Log:
    pass
#运行ide 7
#@M_t.Mortise
def run_ide(test=Test_bool):#ksh_ide_ui();daj_ide_ui();tan_ide_ui()
    global run_loop
    #运行初始化前命令
    try:
        exec(Boot_Start,{**globals(),**Clsr.glo},Clsr.loc)
    except BaseException as e:
        print('运行初始化前命令失败 \n\tErr:',e)
    #如果不存在run_loop则创建一个代替品
    try:
        run_loop
    except:
        run_loop=lambda x=None:x
    #创建ide
    ksh_ide_ui()# 1
    daj_ide_ui()# 2 
    tan_ide_ui()# 3 
    set_ide_ui()# 4
    load_ide_config()# 5
    #刷新环境变量
    g_l.update_Glo_port()
    #运行启动时命令
    exec(Boot_Ing,{**globals(),**Clsr.glo},Clsr.loc)
    #运行ide
    run_ide_ui(test=test|Test_bool)# 6
#自定义捕获命令行调用
#print(__name__)
if __name__ =='__main__':
    multiprocessing.freeze_support()
    #命令后面有分号' ; '表示结束运行,如果没有分号' ; '则表示继续运行
    if sys.argv[-1]!=';':
        print('run:',end=' ')
    if len(sys.argv)>1:
        #命令前面有冒号' : '表示运行命令后退出,用于不能在命令后面使用分号的场合
        if '-' in sys.argv[1] and '--'not in sys.argv[1]:
            sys.argv[1]=sys.argv[1].strip('-')
            inherit_bool=True
        if ':' in sys.argv[1] :
            sys.argv[1]=sys.argv[1].strip(':')
            def run_loop(get=sys.argv[1:]):
                diy(' '.join(get))
                inherit_bool_dict[inherit_bool](lop=dict(bianl,**Clsr.loc),lod=lod)
                sys.exit()
        elif sys.argv[1] !='--help':
            def run_loop(get=sys.argv[1:]):
                diy(' '.join(get))
                inherit_bool_dict[inherit_bool](lop=Clsr.loc,lod=lod)
        else:
            print(sys.argv[0],'[要执行的脚本命令]')
            print('或者',sys.argv[0])
            print('在命令前面加":"或在命令后面加(要有空格)" ; "表示运行命令后退出编辑器')
            print('在命令前加"-"表示缓存新增变量')
            print('启动与命令优先级: Boot_Start>命令行命令>')
            print('可以试着直接输入 tk :help 查看基层脚本的帮助')
            sys.exit()
    
    j_lins=Lins(length=10)
    run_ide()
    #在运行结束后移除root
    if text in Clsr.loc.values():
        try:
            Clsr.loc=dict(filter(lambda i:i[1]!=text,Clsr.loc.items()))
        except BaseException as e:
            print('找到root但在结束运行后无法删除缓存:',e)
    #如果是缓存运行则在结束后缓存
    inherit_bool_dict[inherit_bool](lop=dict(bianl,**Clsr.loc),lod=lod)
    
def run_impurt_mod():
    try:
        '''
        err_ok="engapi,M_t,扫图,截屏,腾讯识图,clk,保存全局变量"
        __import__(err_ok)
        from BOOT import *
        '''
        import numpy as np
        print('',end='-')
        import engapi,M_t,扫图,截屏,腾讯识图,clk,保存全局变量,get_doc
        print('',end='-')
        import tkinter,os,sys,json,jsonlines,javalang#javalang是py自带的语法解析器可以将java代码字符串中的代码语法解释为类
        print('',end='-')
        import requests,tkinter as tk
        print('',end='-')
        from concurrent.futures import ThreadPoolExecutor
        print('',end='-')
        from threading import Thread,current_thread
        print('',end='-')
        from tkinter.filedialog import askdirectory,askopenfilename,asksaveasfilename
        print('',end='-')
        #from jpype import *
        from queue import Queue
        print('',end='-')
        import pickle,ctypes #as kraut
        from idlelib import searchengine
        from idlelib.search import SearchDialog
        print('',end='-')
        #无法自动导入
        #from ml import *
        import idlelib.colorizer as idc
        import idlelib.percolator as idp
        from idlelib.multicall import MultiCallCreator
        print('',end='-')
        import windnd,multiprocessing
        print('',end='-')
        from tkinter.messagebox import showinfo,askyesno
        print('',end='-')
        import compileall,dir_exp,newts,类,openAI,call_CB,tab_list
        print('',end='-')
        sys.path.append('..')
        print('',end='-')
        import 摩斯
        print('',end='-')
        import 整活.byte_
        print('',end='-')
        import 爬虫.翻译
        print('',end='>')
        import BOOT
        text_Translation=爬虫.翻译.tetr
        Byte=整活.byte_.Byte
        Css=类.Css
        #Ml=Ml(name='工作空间')
    except BaseException as e:
        print('模块导入异常:',e)
