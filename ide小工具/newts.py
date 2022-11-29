if __name__=='__main__'or 1:
    import sys
    sys.path.append(r'../数控命令解释')
    import 类
    Css=类.Css
import re#用正则表达式解析字符串更方便

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
#将自定义函数语法编译为py代码
def py_mains(name='main',psvm=None):
    main=Css(name)
    psvm=psvm
    lsp=[f"""
def {psvm[0][i][0]}({','.join(psvm[0][i][1])}):
    {psvm[1][i]}""" for i in range(len(psvm[0]))]
    sp=[compile(i,'_main_',mode='exec')for i in lsp]
    #[print(i) for i in lsp]
    return sp
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
stat={'def':py_mains,'func':py_mains,'cmd':cmd_mains}


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
    pd=py_mains(psvm=psvm)
    #执行转义后的语法
    [exec(i,globals(),globals()) for i in pd]
    print(psvm[2])
    print(演示1,演示2)
    [print(i) for i in cmd_mains(psvm=parse(cmd_strmn,newm='cmd'))]
