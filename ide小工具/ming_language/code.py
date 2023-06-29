import sys,os,re,regex,jsonlines
try:
    import dir_exp
except:
    try:
        us.append('..')
        import dir_exp
    except:
        print('找不到dir_exp模块 可能由于code.py 目录位置不正确')
#print(f"{sys.argv[0]}\n{os.getcwd()}\n{os.path.abspath('.')}\n{os.path.abspath(os.curdir)}")
#根据运行位置推导代码存放位置(可能会因为运行/编译环境而有些规则不同)
run_load=os.path.dirname(sys.argv[0])
run_load=dir_exp.Mou(os.path.join(run_load,'ming_language') if os.path.basename(run_load)!='ming_language' else run_load)
#添加缓存(.code文件夹)
def new():
    if not run_load['.code']:
        run_load[None]='.code'
    sys.path.append(str(run_load['.code']))
#将文件放入缓存(.code文件夹)
def loop(path:str,name=''):
    if name:
        run_load['.code']<<path
        pa=str(run_load['.code'])+rf'\{name}'
        to=run_load['.code'][os.path.basename(path)]
        
        print('转移... ',to if to else f"Err 当前目录 {os.getcwd()} 下未找到该文件:{os.path.basename(path)}",end=' ')
        return to>pa
    return run_load['.code']<<path
#清除缓存
def remove():
    del run_load['.code'][:]

#承载语言编译方法的类
class Long:
    new()
    remove()
    @staticmethod
    def cpp(text):
        pass
    @staticmethod
    def java(text):
        pass
    @staticmethod
    def rust(text):
        print(text)
        try:
            from .import code_rust
        except:
            import code_rust
        #暂时假设只有一个脚本
        rand=run_load['rust']#dir_exp.Mou目录表达式简化了对目录操作的代码量 有兴趣可以看看源码
        if not rand['goto.jsonl']:
            rand['']='goto.jsonl'
            with jsonlines.open(str(rand['goto.jsonl']),'w') as f:
                f.write({'rust':
                         {'project':
                          {'path':r'.\ming_language\rust\guessing-game',
                           'out':r'guessing_game'
                           }
                          }
                         }
                        )
        with jsonlines.open(str(rand['goto.jsonl']),'r') as f:
            leap=[i for i in f]
            
        read_leap=leap[0]
        path_put=read_leap['rust']['project']['path']
        rust_path=path_put+r"\target\release"+rf"\{read_leap['rust']['project']['out']}.dll"
        
        oder=code_rust.Oder
        sun=oder(rust_path=path_put+r"\src\lib.rs")
        #执行编译
        los_dict=sun(text)
        sun.run()
        print('going in path: '+rust_path)
        loop(rust_path,sun.mod_name_list[-1]+'.pyd')
        print('...ok!')
        return los_dict
