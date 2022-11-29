#-*- coding:utf-8 -*-
try:
    import tkinter,os,sys,json,javalang#javalang是py自带的语法解析器可以将java代码字符串中的代码语法解释为类
    import tkinter as tk
    import engapi
    from concurrent.futures import ThreadPoolExecutor
    from threading import Thread,current_thread
    from tkinter.filedialog import askdirectory,askopenfilename,asksaveasfilename
    from jpype import *
    from queue import Queue
    import pickle #as kraut
    from ml import *
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
        print(self,vg)
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

def lop(list_:[list,tuple]):#循环索引
    len_l=len(list_)-1
    li=0
    def lj(it:int):#索引跨度
        nonlocal li,len_l
        li=0 if li>=len_l or li+it>len_l else li+it
        return li#返回索引值
    return lj#闭包

def soo(eve=None):
    try:
        pat = asksaveasfilename(title=u'保存文件')
        with open(pat,wsr,encoding=Ml.encoding,errors=Ml.errors) as f:
            f.write(text.get('1.0', tk.END))
    except:
        print('soo出错',eve)
def roo(eve=None):
    try:
        global rd
        pat=askopenfilename(title=u'打开文件')
        with open(pat,rsr,encoding=Ml.encoding,errors=Ml.errors) as f:
            data=f.read(reado)
            if rd:
                lb.delete('1.0','end')
            sot=str(data)
            lb.insert(tkinter.END,sot[:sot.rfind('\n')])
            Ml.add_open=pat
    except BaseException as e:
        print('roo出错',e)
def ro(eve=None):
    global rd
    rd=0 if rd else 1
    return bool(rd)
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
def diy(get):#检测并执行Ml命令
    global rsr,wsr,reado
    gee=list(filter(lambda x:bool(x),get.split('; ')))
    if not gee:
        return None
    elif len(gee)>1:
        [diy(ge) for ge in gee]
    elif gee[0]:#这里写的有问题
        ge=gee[0].split()
        if ge[0] in ds_key:
            return dds[ge[0]](get=ge)
        else:#diy('Text')
            try:
                return eval(get,Clsr.glo,Clsr.loc)
            except:
                return exec(get,Clsr.glo,Clsr.loc)

j_lins=Lins(None,[])
#接收回车并执行diy命令
def ent(event=None):#接收回车并执行diy命令
    global rr
    try:
        md=cmd.get()
        j_lins.append(md);
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

rd=1
root = tk.Tk()
root.title('查看器')
j=tk.PanedWindow(root)
jp=tk.PanedWindow(orient=tk.VERTICAL)
cmd=tk.Entry(jp,bd=3,width=20)
sb = tk.Scrollbar(j)
text=lb = tk.Text(jp,yscrollcommand=sb.set,undo = True)
sb.config(command=lb.yview)

j.add(jp)
jp.add(lb)
jp.add(cmd)
j.add(sb)

j.pack(fill=tk.BOTH,expand=1)

"""
rtaerr=tk.Tk()
rtaerr.title('捕获')
err=tk.Text(rtaerr)
err.pack()
"""

rsr='r';wsr='w';reado=None
popupment = tkinter.Menu(lb, tearoff=False)
popupment.add_command(label='全选', command=lambda x=0:print(x))
#可以通过lin_dic添加快捷键命令
lin_dic={
         '<3>':lambda event:popupment.post(event.x_root,event.y_root),
         '<Control-s>':soo,'<Control-o>':roo,'<Control-p>':zhr,
         '<F5>':lambda event:(Ml.call_l(event,get=(':',"compile" ,)),print('《执行》')),
         }

lin(dic=lin_dic)
lb.bind('<3>',lambda event:popupment.post(event.x_root,event.y_root))
cmd.bind('<Return>',ent);cmd.bind('<Up>',cmds);cmd.bind('<Down>',cmds)

j.mainloop()
