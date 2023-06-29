import sys
Codec_tuple=("UTF-8","GBK","GB18030 ","UTF-16","ISO-8859-1")
#快捷读取文并返回文件内容件字符串
def Read_To_Retuern(path:str,o:str='rb')->bytes:
    #print('read',o)
    try:
        with open(str(path),o) as f:
            return f.read()
    except:
        return f'没有这个文件或目录 {path}'
#快捷读取文件并返回文件内容列表
def Read_To_list_Retuern(path:str,o:str='rb')->'list[bytes]':
    try:
        with open(str(path),o) as f:
            return f.readlines()
    except:
        return f'没有这个文件或目录 {path}'
#快捷将字节码列表转化为字符串元组
def Lines_to_str_tuple(fs:list,byte:str='utf-8')->'list[str]':
    return tuple(map(lambda i:str(i,byte),fs))
#循环解码bytes为str直到解出
def Loop_do_byte_codec(by:bytes)->str:
    als=Codec_tuple
    i=0
    byte=als[i]
    while 1:
        try:
            #print(byte)
            return str(by,byte)
        except:
            i+=1
            try:
                byte=als[i]
            except:
                return str(print('无法解码byte'))
#快捷写入文件
def Write_To_file_Return(path:str,s:[bytes,str,list,tuple]=b'',o:str=''):
    o=o if o else 'a+' if type(s)==str else 'ba+' 
    with open(str(path),o) as f:
        return f.write(s) if type(s) in (bytes,str) else f.writelines(s)
#调用diy 如果没有返回值则返回自身的字符串
def Diy_to_code_or_str(s:str,local=None)->{'ok':'code','err':'str'}:
    #通过上级调用者的环境获取diy函数
    if local:
        fn=sys._getframe(3)
        f=sys._getframe(2)
        ff=sys._getframe(1)
        local={**fn.f_globals,**f.f_globals,**ff.f_globals}
        diy=local['diy']
    try:
        opt=eval(s,local['Clsr'].glo,local['Clsr'].loc)
    except:
        try:
            opt=diy(s)
        except:
            opt=None
    return ' '.join(opt) if type(opt) in (list,tuple,set) else str(opt) if opt else s
#str套用类方便自定义嵌套字符串的表示
class STR:
    def __init__(self,s:str):
        self.s=str(s)
    def __repr__(self):
        return f'"""{self.s}"""'
    def __str__(self):
        return f"""{self.s}"""
class Fc:
    def __init__(self):
        self.ind=1
    def __get__(self,cls_self,cls,*v,**k):
        return sys._getframe(self.ind)



Boot_file_path_dir_exp_bool_func=lambda il,sin='\n',byte='utf-8':sin.join(({str(i).rsplit('.',1)[-1]:(";".join((str(STR(f"diy('''{l.rstrip()}''')"))
                                for l in
                                Lines_to_str_tuple(Read_To_list_Retuern(i),byte=byte)))).replace("diy('''''');",'').rstrip(';'),
                                'py':str(Read_To_Retuern(i),byte)}[str(i).rsplit('.',1)[-1]] for i in il)
                                ) if byte else sin.join((Loop_do_byte_codec(Read_To_Retuern(i)) for i in il ))
#filew -a+ 你好 C:\Users\Administrator\Desktop\pyLi\基础\ide小工具\语法演示\你好.txt
