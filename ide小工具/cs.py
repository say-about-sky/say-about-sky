#-*- coding:utf-8 -*-

#from progress.bar import Bar
import USE,os,psutil

import_pub_tuple=({'np': 'numpy'},'echo',
                  'engapi', 'M_t', '扫图', '截屏', '腾讯识图', 'clk', '保存全局变量', 'tkinter', 'os', 'sys', 'json', 'jsonlines', 'javalang',
                  'requests', 'pickle', 'ctypes', 'windnd', 'multiprocessing', 'compileall', 'dir_exp', 'newts', '类', 'openAI','call_CB',
                  ('tkinter', 'tk'),
                  {'concurrent.futures': ('ThreadPoolExecutor',), 'threading': ('Thread', 'current_thread'),
                   'tkinter.filedialog': ('askdirectory', 'askopenfilename', 'asksaveasfilename'), 'queue': ('Queue',),
                   'tkinter.messagebox': ('showinfo', 'askyesno')})
try:
    #判断如果在idle中运行则跳过进度条
    print_bool =False if psutil.Process(os.getppid()).name()=="pythonw.exe" else True 
    #执行批量导入
    USE.use(*import_pub_tuple,glo=globals(),print_bool=print_bool)
    #无法批量导入的模块:
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
inherit_bool_dict={False:lambda *v,**k:None,True:保存全局变量.run_dump}
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
#标准输出(copy)
class myStdout():
    def __init__(self):
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def write(self,info):
       #info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
       str = info.rstrip("\r\n")
       if len(str):self.processInfo(str)  #对输出信息进行处理的方法

    def processInfo(self,info):
        #os.popen(f"echo {info}")
        #echo.cmd_print(info)
        os.system(f'echo "{info}"')
        #self.stdoutbak.write(info+"\n") #可以将信息再输出到原有标准输出，在定位问题时比较有用

    def restoreStd(self):
        print("准备恢复标准输出")
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak
        print("恢复标准输出完成")

    def __del__(self):
       self.restoreStd()
       
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
    #@staticmethod 一次批量添加子菜单并绑定主菜单
    def add_Submenu_bat(self:'主菜单对象',name:'菜单名',dic:dict):
        menu=Me(self, tearoff=False)
        [menu.add_command(label=l[0],**l[1]) for l in dic.items()]
        self.add_cascade(label=name,menu=menu)
    #@staticmethod 批量添加子菜单
    def add_command_bat(self,dic:dict):
        return [self.add_command(label=l[0],**l[1]) for l in dic.items()]
    #@staticmethod 批量绑定选项
    def add_cascade_bat(self,dic:dict):
        return [self.add_cascade(label=l[0],**l[1]) for l in dic.items()]
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
        pd_bool=('__iter__' in dir(pat))and(len(pat)>1)
        if pd_bool:
            if askyesno('批处理','当前拖入[输入]多个文件,是否开辟新进程打开?'):
                pdl=[(f"python tk.py cmd [roo_open_file({i})]") for i in pat]
                Tr.akn((*eval("cmd_popen,"*len(pdl)),j.mainloop),[*pdl,()],pool=pool_Ml)
            else:
                roo_open_file(pat[-1],rsr,rd)
        else:
            roo_open_file(pat[-1],rsr,rd)
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
def diy(get:str):#检测并执行Ml命令
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
            print('构造函数','ok!!!:')
            print(Tr.fun,Tr.lois,Tr.dicp)
            Ds_(Ml);congzai_Ml()
        #[newts.stat[Tr.fun][1](n=psvm[0][i][0],i=pd[i],l=Clsr) for i in range(len(pd))]
        else:
            #print('>>>',gee)
            pass
        #diy(gee[0])
            

#接收回车并执行diy命令
def ent(event=None):#接收回车并执行diy命令
    global rr
    try:
        md=cmd.get()
        (j_lins.append(md) if md not in j_lins else 0)
        diy(md)#执行diy
        rr=Dio(range(len(j_lins))[::-1])
        cmd.delete(0, 'end')
    except BaseException as e:
        print('ent出错',e)

#同步快捷键和命令
def lin(self=None,dic:dict={}):
    fff(dic,go=globals())
    return [text.bind(k,v) for k,v in dic.items()]#表达式循环快速绑定快捷键

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
    global rd,root,j,jp,cmd,sb,text,lb
    jp=tk.PanedWindow(orient=tk.VERTICAL,width=800,height=600)
    cmd=tk.Entry(jp,bd=3,width=20)
    sb = tk.Scrollbar(j,width=20,orient=tk.VERTICAL)
    #sb.resizable(20,1000)
    text=lb = tk.Text(jp,yscrollcommand=sb.set,undo = True)
    sb.config(command=lb.yview)
    #绑定拖拽功能
    als=("utf-8","GBK","GB18030 ","UTF-16","ISO-8859-1")
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
    windnd.hook_dropfiles(cmd,func=lambda bat:cmd.insert(tkinter.INSERT,pand(bat)))
#添加界面 3
def tan_ide_ui():
    global rd,root,j,jp,cmd,sb,text,lb
    j.add(jp)
    jp.add(lb,width=780,height=560)
    jp.add(cmd,width=780,height=40,minsize=30)
    j.add(sb,width=20,minsize=20)
    j.pack(fill=tk.BOTH,expand=1)

#设置内建操作

"""
rtaerr=tk.Tk()
rtaerr.title('捕获')
err=tk.Text(rtaerr)
err.pack()
"""
#获取pool
def pool_ml():
    global pool_Ml
    return pool_Ml
#预分配一个线程池
def pl_m(nt=3):
    global pool_Ml
    pool_Ml=Tr.pool(nt)
def Single_thread_bool(add=True,call=Ml.call_l):#重写
    if add:
        if sys.argv[-1]!=';':
            print('单线')
        return lambda event=None:(call(event,get=(':',"compile" ,)),print('《执行》'))
    if sys.argv[-1]!=';':
        print('多线')
    return lambda event=None:Tr.akn((call,j.mainloop),[(),()],pool=pool_Ml)
#设置F5执行方式 4
def set_ide_ui(): 
    global popupment
    Ml.Single_thread=Single_thread_bool()
    pl_m(Ml.nt)
    click_r()
    popupment = tkinter.Menu(lb, tearoff=False)
    [popupment.add_command(label=i[0], command=i[1]) for i in click_dic.items()]
#重载click_dic
def click_r():
    global click_dic
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
    #可以通过click_dic添加右键命令
    #创建循环开关
    menu_bool_call=Dio([lambda *e:root.config(menu=mainmenu),
                        lambda *e:root.config(menu='')])  
    click_dic={
        '菜单栏开关':lambda *e:next(menu_bool_call)(),
        #'全选':lambda x=0:print(x),
        '说/say':Tr.aknt(None,(diy,j.mainloop),[('say Text'),()],pool=pool_Ml),
        '翻译/translate->input':translate_input,
        '翻译并说译文':translate_input_say,
        '登入/engine':lambda *e:openAI.login(),
        '问/openai':Tr.aknt(None,(fid,j.mainloop),[(),()],pool=pool_Ml),
        '问/ChatBot':Tr.aknt(None,(run_ChatBot,j.mainloop),[(),()],pool=pool_Ml),
        'cs':Tr.aknt(None,(fff,j.mainloop),[(),()],pool=pool_Ml),
        }
#重载lin_dic
def lin_r():
    global lin_dic
    #可以通过lin_dic添加快捷键命令
    lin_dic={
         '<3>':lambda event:popupment.post(event.x_root,event.y_root),
         '<Control-s>':soo,'<Control-o>':roo,'<Control-p>':zhr,
         '<F5>':lambda *e:Ml.call_l(e,get=(':',"compile" ,)),#用队列线程比较好Tr.aknt(None,(Ml.Single_thread,j.mainloop),[(),()])
         '<Control-q>':sys.exit,'<Control-l>':lambda e=None:截屏.run(),
         '<Alt-l>':lambda e=None:截屏.run(os.path.split(Ml.add_open)[0]if os.path.split(Ml.add_open)[1]!=Ml.add_open else Ml.add_open+r'\sept.png'),#text.insert
         '<Control-k>':Tr.aknt(None,(clkn,j.mainloop),[('bd'),()],pool=pool_Ml),
         '<Alt-k>':Tr.aknt(None,(clkn,j.mainloop),[('tx'),()],pool=pool_Ml),
         '<Control-u>':roo_bool,
         #'<Key>':lambda e=None:print(e)
         #lambda *e:Ml.Single_thread(e)#用队列线程比较好
             }
#运行ide 5
def run_ide_ui():
    global run_loop,inherit_bool,lod,mainmenu
    lin_r()
    lin(dic=lin_dic)
    #设置环境变量备份
    log=M_t.Mortise(Log)
    log.dict={}
    Clsr.glo,Clsr.loc=log.dict,log.dict
    #检测是否导入环境变量
    """
    ddt=os.path.split(lod)[0]
    st=os.path.split(lod)[1]
    if st in os.listdir(ddt):
    """
    Clsr.glo.update(bianl)
    #传入diy
    root.diy,root.text=diy,text
    #运行初始命令
    run_loop();del run_loop
    #inherit_bool_dict[inherit_bool](lop=Clsr.loc,lod=lod)
    if sys.argv[-1]==';':
        try:
            quit()
        except:
            sys.exit()
    #绑定命令窗口快捷键
    lb.bind('<3>',lambda event:popupment.post(event.x_root,event.y_root))
    cmd.bind('<Return>',lambda *e:Tr.aknt(None,(M_t.Mortise(ent),j.mainloop),[(),()],pool=pool_Ml)());cmd.bind('<Up>',cmds);cmd.bind('<Down>',cmds)
    cmd.bind('<Control-z>',lambda *e:Tr.aknt(None,(sys.exit,j.mainloop),[(),()],pool=pool_Ml)())#quit 
    #设置图标
    root_image = tk.PhotoImage(file=os.path.split(lod)[0]+r'\logo\Ms.png')
    root.tk.call('wm', 'iconphoto', root._w, root_image)
    #运行UI前添加自身作为最高权限
    Clsr.glo['root']=root
    #绑定菜单
    cal=lambda *e:print('测试')
    menu_dict={'openai':{'command':openAI.login},
               'ChatGPT':{'command':login_ChatBot}
               }
    mainmenu=Me(root)
    mainmenu.add_Submenu_bat('登录',menu_dict)
    j.mainloop()
class Log:
    pass
#运行ide 6
#@M_t.Mortise
def run_ide():#ksh_ide_ui();daj_ide_ui();tan_ide_ui()
    ksh_ide_ui()
    daj_ide_ui()
    tan_ide_ui()
    set_ide_ui()
    #diy('exec log() log()')
    run_ide_ui()


#自定义捕获命令行调用
'''
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
    '''
echo.cmd_println("测试")
j_lins=Lins(length=10)
#multiprocessing.freeze_support()
#diy("echo 123")
mystd = myStdout()
run_ide()

