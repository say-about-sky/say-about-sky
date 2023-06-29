if __name__=='__main__'or 1:
    import sys
    sys.path.append(r'../数控命令解释')
    import 类
    Css=类.Css
import re#用正则表达式解析字符串更方便
import regex#嵌套匹配解析引擎

#import ming_language.rust.cs
#一个类装饰器,它可以改变定义类时的元类
def cas(*v,meta=type):
    def add(cls):
        nonlocal meta
        return meta(cls.__name__,v,dict(cls.__dict__))
    return add

#自定义一个元类
class Add_stat(type):
    def __new__(cls,*v,**k):
        cls_dict=v[2]
        cls_dict=dict(filter(lambda i:"_mains" in i[0],cls_dict.items()))
        return cls_dict #返回类的函数列表
        
#re.findall('\([^()]*\)',string)#匹配所有括号
#re.search('(\(.*\))', string)#匹配最外层括号
#嵌套分析:
#regex.search("(?<rec>\\((?:[^()]++|(?&rec))*\\))",str,flags=regex.VERBOSE).captures('rec')#如果解析只有一层或解析不到captures会报错
'''
re.findall(r'(([$].??)([^$]+.*?))','$$hjkhkhjk$aaammmp$adfff**kkk')#匹配$后接字符串
re.findall(r'((?P<len>[$](.*?))([^$]+.*?))','$$hjkhkhjk$$$aaammmp$adfff**kkk')#区分是否转义
#匹配最外层大括号
regex.search("(?<rec>\\{(?:[^{}]++|(?&rec))*\\})",'func{}',flags=regex.VERBOSE).group()
re.search('(\{.*\})','func{a{99{}}c}').group()[1:-1]
#提取名字
re.search('(.*?)[{]','func{a{99{}}c}').group()[0:-1]
'''
@cas(meta=Add_stat)
class stat:
    #将自定义函数语法编译为py代码
    def def_mains(name='main',psvm=None):
        main=Css(name)
        psvm=psvm
        lsp=[f"""
def {psvm[0][i][0]}({','.join(psvm[0][i][1])}):
    {psvm[1][i]}""" for i in range(len(psvm[0]))]
        #[print(i) for i in lsp]
        sp=[compile(i,'_main_',mode='exec')for i in lsp]
        return sp
    def func_mains(name='fun',psvm=None):
        return stat['def'](name=name,psvm=psvm)
    def cmd_mains(name='cm',psvm=None):
        main=Css(name)
        psvm=psvm
        psvm_l=['\n    '.join(map(lambda x:f"""diy('''{x.strip()}''')""" if x.strip()[0]!='#' else x.strip(),i.split('\n'))) for i in psvm[1]]
        lsp=[f"""
def {psvm[0][i][0]}_l(get=[]):
    loc_l=locals()
    exec("{psvm[0][i][1][0]},*v=get",loc_l,loc_l)
    Clsr.glo.update(loc_l)
    {psvm_l[i]}""" for i in range(len(psvm[0]))]
        sp=[compile(i,'_main_',mode='exec')for i in lsp]
        [print(i) for i in lsp]
        return sp
    def rust_mains(name='rs',psvm=None):
        main=Css(name)
        psvm=psvm
    
#stat={'def':stat.py_mains,'func':stat.py_mains,'cmd':stat.cmd_mains}
#2次加工函数列表
stat={i.replace("_mains",''):stat[i] for i in stat}

#将文本中的自定义函数语法解析为变量组成的元组 返回:([(函数名),(参数[形参])],[代码片段],[过滤后的字符串])
def parse(strmn:str,bb=re.compile(r"[{](.*?)[}]",re.DOTALL),newm='def'):    
    if f'new {newm} ' in strmn:
        nvs,pom=(),()
        for i in filter(lambda x:x and '\n'!= x,strmn.split(f'new {newm} ')):
            try:
                nv=re.findall(r'(.*?)[{]',i)[0]
                name=re.findall(r'(.*?)[(]',nv)[0]
                nvs+=((name,re.findall(r'[(](.+?)[)]',nv)),)
                lt=re.findall(bb,i[i.find('{'):i.find('}')+1])[0].strip().replace('\n','\n    ')
                pom+=(lt,)
            except BaseException as e:
                print('->parse:',e)
        pattern = re.compile(r'[(new '+newm+' )](.*?)[}]',re.DOTALL)
    return nvs,pom,re.sub(pattern,'',strmn)

#智能解析版parse 可以将call设置为findall等调用方法 默认是嵌套解析search
def parsex(strmn:str,bf:'匹配符'=('{','}'),newm:'类型'='def',call:'regex调用的方法[findall,search]'='search')->{tuple:((('函数名0','形参0'),('函数名..n','形参..n')),('嵌套推导列表'))}:
    #bb=re.compile(f"[{bf[0]}](.*?)[{bf[1]}]")
    retx="(?<rec>\\"+bf[0]+f"(?:[^{bf[0]}{bf[1]}]++|(?&rec))"+"*\\"+bf[1]+")"
    calld=eval(f"regex.{call}")
    cald=(lambda jx:(jx.captures('rec'),)) if call=='search' else (lambda jx:tuple((i[1:-1] for i in jx)))
    if f'new {newm} ' in strmn:
        nvs,pom=(),()
        for i in filter(lambda x:x and '\n'!= x,strmn.split(f'new {newm} ')):
            jx=calld(retx,i,flags=regex.VERBOSE)
            try:
                #print(i,':',re.findall(r'(.*?)[{]',i))
                nv=re.findall(r'(.*?)[{]',i)[0]
                name=re.findall(r'(.*?)[(]',nv)[0]
                nvs+=((name,re.findall(r'[(](.+?)[)]',nv)),)
                pom+=cald(jx)
            except BaseException as e:
                print('->parse:',e)
                #pom+=(None,)
    else:
        return None
    return nvs,pom

if __name__=='__main__':
    cmd_strmn='''
111
new cmd 演示(a,b){
echo a b
echo a;b
#233 #233
}
222

'''

    strmn="""
233
new def 演示1(a,b){
a=0
b=1
#a= int 0
#b= int 1
}
123
new def 演示2(*c){
c=2
d=3
#c= int 2
#d= int 3
}
444
"""
    #解析语法
    psvm=parse(strmn)
    #print(parse(strmn))
    pd=stat['def'](psvm=psvm)
    #执行转义后的语法
    [exec(i,globals(),globals()) for i in pd]
    print(psvm[2])
    print(演示1,演示2)
    [print(i) for i in stat['cmd'](psvm=parse(cmd_strmn,newm='cmd'))]
