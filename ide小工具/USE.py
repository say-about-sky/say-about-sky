from progress.bar import Bar

Secd=lambda d:';'.join((f"from {i[0]} import {','.join(i[1])}" if type(i[1]) in (tuple,list) else f"{i[0]}=__import__('{i[1]}')" for i in d.items()))
Spadd=lambda d,f='.':d.split(f)
#循环(隐式)导入
def use(*pub:"tuple(str,str),dict{str:str}或者str",glo=globals(),print_bool:"是否分段执行并打印进度"=True,text='载入模块:',fill='-',suffix='%(percent)d%%'):
    #print(print_bool)
    #额外生成器
    add=( f"{i[1]}=__import__('{i[0]}')" if type(i) in (tuple,list) else Secd(i) if "items" in dir(i) else f"{i}=__import__('{i}')" for i in pub)
    bar=Bar(text, max=len(pub), fill=fill, suffix=suffix)
    #判断是否分段执行并打印进度
    if print_bool:
        l=0
        try:
            for i in add:
                exec(i,glo)
                l+=1
                bar.next()
                #print('',end='-')
            print(" :)")
        except BaseException as e:
            print("use->Err in to:",pub[l],'\n\t Because:',e)
        bar.finish()
        return
    return exec(';'.join(add),glo)
