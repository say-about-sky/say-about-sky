pip_install='python -m pip install {mod}'
pip_dict={}

try:
    import os
    from progress.bar import Bar
except ModuleNotFoundError as e:
    os.system(pip_install.format(mod=e.name))
    
Secd=lambda d:';'.join((f"from {i[0]} import {','.join(i[1])}" if type(i[1]) in (tuple,list) else f"{i[0]}=__import__('{i[1]}')" for i in d.items()))
Spadd=lambda d,f='.':d.split(f)
#循环(隐式)导入
def use(*pub:"tuple(str,str),dict{str:str}或者str",glo=globals(),print_bool:"是否分段执行并打印进度"=True,text='载入模块:',fill='-',suffix='%(percent)d%%',pip_bool=False):
    #print(print_bool)
    #额外生成器
    add=( f"{i[1]}=__import__('{i[0]}')" if type(i) in (tuple,list) else Secd(i) if "items" in dir(i) else f"{i}=__import__('{i}')" for i in pub)
    bar=Bar(text, max=len(pub), fill=fill, suffix=suffix)
    #判断是否分段执行并打印进度
    if print_bool:
        l=0
        for i in add:
            try:
                exec(i,glo)
                l+=1
                bar.next()
            except ModuleNotFoundError as e:
                if pip_bool and ('No module named' in e.msg):
                    pip_mod=pip_dict.get(e.name)
                    pip_mod={pip_mod:pip_mod,None:e.name}[pip_mod]
                    pip_cmd=pip_install.format(mod=pip_mod)
                    print(f"use->Err in to:({pip_mod})",pub[l],'\n\t Because:',e)
                    while 1:
                        put=str(input(f'可能是由于缺失依赖模块,是否执行以下命令安装模块?\n\t{pip_cmd} (y/n)'))[:1].lower()
                        match put:
                            case 'y':
                                os.system(pip_cmd);break
                            case 'n':
                                print(f'安装模块{pip_mod}\t...放弃');break
                            case s:
                                print(s)
            except BaseException as e:
                print("use->Err in to:",pub[l],'\n\t Because:',e)
        bar.finish()
        return print(" :)")
    return exec(';'.join(add),glo)
