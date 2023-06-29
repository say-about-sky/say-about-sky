import sys,os,re,regex
#装饰语法对照
orde_dict={'__new__': '#[new]'}
#解析单个字符串表达式返回fun的参数
def jiex_fname(ltxt)->str:
    fun_all=re.search('(.*?)[{]',ltxt[-1]).group()[0:-1]
    fun_name=re.search('(.*?)[(]',fun_all).group()[:-1] if '(' in fun_all else fun_all
    fun_cl= regex.search("(?<rec>\\((?:[^()]++|(?&rec))*\\))",fun_all,flags=regex.VERBOSE).group()[1:-1] if ~(fun_all.find('(')) and ~(fun_all.find(')')) else ''
    fn=regex.search("(?<rec>\\{(?:[^{}]++|(?&rec))*\\})",ltxt[-1],flags=regex.VERBOSE).group()[1:-1]
    return fun_all,fun_name,fun_cl,fn
#解析单个字符串表达式l并返回拼接好的字符串
def jiex_fund(fun_all,fun_name,fun_cl,fn)->str:
    func_return= fun_all[fun_all.rfind('->'):] if '->' in fun_all else ''
    function_str=f"#[pyfunction]\nfn {fun_name}({fun_cl}){func_return}"+'{'+fn+'}'
    add_function_str=f"m.add_function(wrap_pyfunction!({fun_name},m)?)?;"
    #print(function_str)
    return function_str,add_function_str
class Oder:
    def __init__(self,rust_path=r'C:\Users\saysky\Desktop\pyLi\yfs\rust\guessing-game\src\lib.rs',put_path=r'C:\Users\saysky\Desktop\pyLi\yfs\rust\guessing-game\target\release\gu)essing_game.dll'):
        self.rust_path=rust_path
        self.put_path=put_path
        self.mod_name_list=[]
    def __call__(self,text):
        self.mod_name_list=compiling(text,self=self)
        losd={}
        for mod_name in self.mod_name_list:
            try:
                call_fun_str=f"""
def call_fun():
    import {mod_name}
    return {mod_name}"""
                los=dict()
                exec(call_fun_str,None,los)
                losd.update({mod_name:los["call_fun"]})
            except BaseException as e:
                print(f"err: {e}")
        return losd
    def run(self):
        tpt=os.path.dirname(os.path.dirname(self.rust_path))
        go_cmd=f'cd {tpt} &cargo build --release &cd %cd%'
        return os.system(go_cmd)


text=((('css', []),), (['{v:i32=v}', '{\n     mmp{v:i32=v}\n    }', '{\n    println!("ok")\n    }', '{\nfn __new__(v:i32)->Self{\n     mmp{v:i32=v}\n    }\n#[staticmethod]\nfn a(){\n    println!("ok")\n    }\n}', '{name:&\'a str="ggh"}', '{\nggh{name:&\'a str="ggh"}\n}', '{}', '{\nprintln!("{}",self.name)\n}', '{\nfn __new__()->Self{\nggh{name:&\'a str="ggh"}\n}\nfn class_name(&self){\nprintln!("{}",self.name)\n}\n}', '{\n$class mmp{\nfn __new__(v:i32)->Self{\n     mmp{v:i32=v}\n    }\n#[staticmethod]\nfn a(){\n    println!("ok")\n    }\n}\n$class ggh<\'a>{\nfn __new__()->Self{\nggh{name:&\'a str="ggh"}\n}\nfn class_name(&self){\nprintln!("{}",self.name)\n}\n}\n}'],))
def compiling(text,self:Oder=None):
    conkg=('class',)
    rust_path,put_path,mod_name_list=self.rust_path,self.put_path,self.mod_name_list
    for i in range(len(text[1])):
        txt=text[1][i][-1][1:-1]
        mod_name=text[0][i][0]
        if '$' in txt:
            with open(os.path.join(os.path.dirname(rust_path),'lib_lod.rs')) as f:lib_txt=f.read()
            func_se=lib_txt.find('// pyfunction:'),lib_txt.rfind("#[pymodule]")
            mod_se=lib_txt.find('// add_pyfunction:'),lib_txt.rfind('Ok(())')
            
            snippet=(lib_txt[func_se[1]:mod_se[0]+len(lib_txt[mod_se[0]:mod_se[1]])]).split('\n')
            snippet_pymodule='\n'.join(snippet[:1]+[f'#[pyo3(name = "{mod_name}")]']+snippet[2:])
            
            snippet_list=[lib_txt[:func_se[0]+len(lib_txt[func_se[0]:func_se[1]])-1],
                      None,
                      '\n'+snippet_pymodule,
                      None,
                      '\n'+lib_txt[mod_se[1]:]]
        
            runt_low=re.findall(r'((?P<len>[$](.*?))([^$]+.*?))',txt)
            #过滤关键字
            runt=tuple(filter(lambda x:False in [(i in x[-1]) for i in conkg],runt_low))
            add_class_list,new_class_list=[],[]
            #类拼接
            if "$class" in txt:
                class_list=list()
                for i in runt_low:
                    low=regex.findall(r"[$]class (.+?)[{]",i[0],flags=regex.DOTALL)
                    
                    if low:
                        ig=i[-1].strip('class').strip().strip(low[0])
                        #这里要加入关于解析函数，类型的操作(目前假设只有一个函数__new__)
                        orde=re.findall(r"fn (.+)[(]",ig[1:-1])
                        orde=[i.split('<')[0] if '<' in i else i for i in orde]
                        #print(low,orde)
                        #是否作为魔法方法装饰
                        trims_hand_tuple=tuple([orde_dict[i] for i in filter(lambda x:x in orde_dict,orde)])
                        #print(ig)
                        ght=re.search(low[0].split('<',1)[0]+r'(|\s)[{]((.+)fn|(.+))',ig,re.DOTALL)
                        
                        #print(ght[0],orde,ig)
                        set_static=regex.findall("(?<rec>\\{(?:[^{}]++|(?&rec))*\\})",ght[0])[0] if "#[new]" in trims_hand_tuple else "{ }"
                        #print(set_static)
                        #解析并自动生成struct
                        set_static_dict={i[0]:i[-1].split('=') for i in (i.split(':',1) for i in set_static[1:-1].split(','))}
                        #print(set_static_dict)
                        static=f'#[pyclass(subclass)]\nstruct {low[0]}'+'{'+",".join((f"{k}:{v[0]}" for k,v in set_static_dict.items()))+'}'
                        #print(f"ig={ig};low={low};set_static_dict={set_static_dict};ght={ght[2]}")
                        ign_str=ig[:ght.start()]+low[0]+'{'+",".join((f"{k}:{v[-1]}" for k,v in set_static_dict.items()))+'}'+ght[2].split('}',1)[-1]+ig[ght.end():]
                        class_list.append((f"#[pymethods]\nimpl {low[0]}",(trims_hand_tuple,low[0].split('<',1)[0] if ("<'" in low[0]) and ('>' in low[0]) else low[0],static),ign_str))
                
                add_class_list=[i[1][-1]+'\n' for i in class_list]+['\n'+f"{i[0]}"+'{\n'+[l for i in class_list for l in i[1][0]][0]+i[-1][1:] for i in class_list]
                new_class_list=[f"m.add_class::<{i[1][1]}>()?;" for i in class_list]
                #print(add_class_list)
                #sped=regex.findall(r"[$]class\s"+class_name,txt,flags=regex.DOTALL)[0]
            #print(snippet_list)
            
            #迭代拼接
            function_list=[j[0] for j in (jiex_fund(*jiex_fname(l)) for l in runt)]
            add_function_list=[j[1] for j in (jiex_fund(*jiex_fname(l)) for l in runt)]
        
            snippet_list[1],snippet_list[3]='\n'.join(add_class_list+function_list),'\n'.join(new_class_list+add_function_list)
            #输出
            with open(rust_path,'w') as f:f.writelines(snippet_list)
        mod_name_list+=[mod_name]
    return mod_name_list
