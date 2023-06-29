import inspect
#创造一个可合并迭代器的生成器类
#class 
#异常处理分支
def try_for(run:str,err:str,glo=locals()):
    try:
        exec(run,glo,glo)
    except:
        exec(err,glo,glo)
#简易粗暴解析函数(help伪实现)
def cond_doc(fn:type(lambda _:None)=lambda _:None)->'属性名<父属性(元类)>(参数)->返回对象\n\t注释':
    """
    cond_doc(fn:func)->str('属性名<父属性(元类)>(参数)->返回对象\n\t注释')
    
    __annotations__解析函数
    简单的描述可调用对象属性返回关于可调用对象的调用参数和返回值的解析
    并返回排版好的字符串
    """
    #inspect 是一个专门整理可调用对象参数的库
    result = inspect.getfullargspec(fn)
    #获取返回值类型(如果有注释的话删除返回值的注释)
    value=str(result.annotations.get('return'))
    los=locals();los['try_for']=try_for;los['glo']=los
    try_for("result.annotations.pop('return') if value else None","pass#print('警告:临时的'+value)",los)
    #获取对象标签(如果有)
    try_for("name=fn.__qualname__","try_for('name=fn.__name__','name=type(fn).__name__',glo)",glo=los)
    #判断表达式
    oder=lambda dev,st="*":{False:"",True:st+str(dev)}[bool(dev)]
    #整合形参
    args=(','.join(([f"{result.args[::-1][i]}={repr(result.defaults[::-1][i])}" for i in range(len(result.defaults))]+list(result.args[::-1][len(result.defaults):]))[::-1] if result.defaults else result.args)).rstrip(',')
    #整合实参
    ages=(','.join((f"{i[0]}={repr(i[1])}" for i in result.kwonlydefaults.items())) if result.kwonlydefaults else '').rstrip(',')
    #合并参数
    ime=(
        (f"{args},{oder(result.varargs)},{oder(result.varkw,'**')}".rstrip(',')+f',{ages}').rstrip(',').strip(',')
         if not result.annotations else ','.join((f"{i[0]}:{i[1]}" for i in result.annotations.items()))
         )
    #整理所有
    f_repr=f"{los['name']}{type(fn)}({ime})->{value}:\n\t{str(inspect.getcomments(fn)).rstrip('None')}\n\t{str(inspect.getdoc(fn)).rstrip('None')}"#fn.__doc__
    return f_repr

#不报错code_doc
def try_code_doc(fn:type(lambda _:None)=lambda _:None)->('属性名<父属性(元类)>(参数)->返回对象\n\t注释','err'):
    dic={"txt":None,"cond_doc":cond_doc,"fn":fn}
    try_for("txt=cond_doc(fn)","txt='err:可能不是一个标准的可调用对象'",dic)
    return dic["txt"]
