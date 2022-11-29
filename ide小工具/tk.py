#-*- coding:utf-8 -*-
try:
    import requests
    import tkinter,os,sys,json,javalang#javalang是py自带的语法解析器可以将java代码字符串中的代码语法解释为类
    import tkinter as tk
    import engapi,M_t
    from concurrent.futures import ThreadPoolExecutor
    from threading import Thread,current_thread
    from tkinter.filedialog import askdirectory,askopenfilename,asksaveasfilename
    #from jpype import *
    from queue import Queue
    import pickle,ctypes #as kraut
    from ml import *
    import windnd
    from tkinter.messagebox import  showinfo,askyesno
    import compileall,newts,类
    sys.path.append('..')
    import 摩斯
    import 整活.byte_
    import 爬虫.翻译
    text_Translation=爬虫.翻译.tetr
    Byte=整活.byte_.Byte
    Css=类.Css
    #Ml=Ml(name='工作空间')
except BaseException as e:
    print('模块导入异常:',e)
#打包时的额外参数
with open(sys.argv[0].rsplit('\\',1)[0]+r'\help','rb') as f:
    help=pickle.load(f)
#必要的全局参数
rsr='r';wsr='w';reado=None
run_loop=lambda x=None:x
#自定义线程添加类
class Tr(Thread):
    def __init__(self,fun:'func',ag:'ages'):
        self.func=fun
        self.age=ag
        super().__init__(target=fun, args=ag)
    def rn(self):
        self.func(*self.age)
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
class Lins(list):#定长列表
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
        pat = asksaveasfilename(title=u'保存文件')
        with open(pat,wsr,encoding=Ml.encoding,errors=Ml.errors) as f:
            f.write(text.get('1.0', tk.END))
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
        lb.insert(tkinter.END,sot[:sot.rfind('\n')])
        #保存打开的文件路径(方便了操作文件目录的命令)
        Ml.add_open=pat
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
            Tr.fun=gp[1]
            Tr.lois=gee[:]
            Tr.dicp=newts.stat[Tr.fun]
        elif 'end' in gee[0]:
            Ml.end_l()
            psvn='\n'.join(Tr.lois)
            psvm=newts.parse(psvn,newm=Tr.fun)
            pd=Tr.dicp(psvm=psvm)
            Tr.lois=[]
            if Tr.fun=='func':
                l={}
                [exec(i,Clsr.glo,l) for i in pd]
                [Ml.self_examination(i) for i in l.values()]
            elif Tr.fun=='cmd':
                l={}
                [exec(i,Clsr.glo,l) for i in pd]
                [Ml.self_examination(i) for i in l.values()]
            elif Tr.fun=='def':
                [exec(i,Clsr.glo,Clsr.loc) for i in pd]
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
    return [text.bind(k,v) for k,v in dic.items()]

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

#可视化ide_ui设定 1
def ksh_ide_ui():
    global rd,root,j
    rd=1
    root = tk.Tk()
    root.title('查看器')
    j=tk.PanedWindow(root)
    #绑定拖拽功能
    windnd.hook_dropfiles(root,func=lambda bat:roo_d(bat))
    
#搭建界面 2
def daj_ide_ui():
    global rd,root,j,jp,cmd,sb,text,lb
    jp=tk.PanedWindow(orient=tk.VERTICAL)
    cmd=tk.Entry(jp,bd=3,width=20)
    sb = tk.Scrollbar(j)
    text=lb = tk.Text(jp,yscrollcommand=sb.set,undo = True)
    sb.config(command=lb.yview)
#添加界面 3
def tan_ide_ui():
    global rd,root,j,jp,cmd,sb,text,lb
    j.add(jp)
    jp.add(lb)
    jp.add(cmd)
    j.add(sb)
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
    popupment = tkinter.Menu(lb, tearoff=False)
    popupment.add_command(label='全选', command=lambda x=0:print(x))
#重载lin_dic
def lin_r():
    global lin_dic
    #可以通过lin_dic添加快捷键命令
    lin_dic={
         '<3>':lambda event:popupment.post(event.x_root,event.y_root),
         '<Control-s>':soo,'<Control-o>':roo,'<Control-p>':zhr,
         '<F5>':lambda *e:Ml.call_l(e,get=(':',"compile" ,)),#用队列线程比较好Tr.aknt(None,(Ml.Single_thread,j.mainloop),[(),()])
         '<Control-q>':lambda *e:quit()
         #lambda *e:Ml.Single_thread(e)#用队列线程比较好
             }
#运行ide 5
def run_ide_ui():
    global run_loop
    lin_r()
    lin(dic=lin_dic)
    lb.bind('<3>',lambda event:popupment.post(event.x_root,event.y_root))
    cmd.bind('<Return>',lambda *e:Tr.aknt(None,(M_t.Mortise(ent),j.mainloop),[(),()],pool=pool_Ml)());cmd.bind('<Up>',cmds);cmd.bind('<Down>',cmds)
    cmd.bind('<Control-z>',lambda *e:Tr.aknt(None,(sys.exit,j.mainloop),[(),()],pool=pool_Ml)())#quit
    run_loop();del run_loop
    if sys.argv[-1]==';':
                quit()
    j.mainloop()
class Log:
    def __new__(cls):
        self=super().__new__(cls)
        self.__dict__.update(globals())
        return self.__dict__
#运行ide
@M_t.Mortise
def run_ide():
    ksh_ide_ui()
    daj_ide_ui()
    tan_ide_ui()
    set_ide_ui()
    #设置环境变量备份
    log=M_t.Mortise(Log)
    Clsr.glo,Clsr.loc=Log(),Log()
    #diy('exec log() log()')
    run_ide_ui()
#自定义捕获命令行调用
if __name__ =='__main__':
    #命令后面有分号' ; '表示结束运行,如果没有分号' ; '则表示继续运行
    if sys.argv[-1]!=';':
        print('run:',end=' ')
    if len(sys.argv)>1:
        #命令前面有冒号' : '表示运行命令后退出,用于不能在命令后面使用分号的场合
        if ':' in sys.argv[1] :
            sys.argv[1]=sys.argv[1].strip(':')
            def run_loop(get=sys.argv[1:]):
                diy(' '.join(get))
                sys.exit()
        elif sys.argv[1] !='-help':
            def run_loop(get=sys.argv[1:]):
                diy(' '.join(get))
        else:
            print(sys.argv[0],'[要执行的脚本命令]')
            print('或者',sys.argv[0])
            print('在命令前面加":"或在命令后面加(要有空格)" ; "表示运行命令后退出编辑器')
            print('可以试着直接输入 tk :help 查看基层脚本的帮助')
            sys.exit()
            
    j_lins=Lins(length=10)
    run_ide()
    
    
