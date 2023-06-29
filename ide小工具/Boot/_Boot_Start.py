#print("Boot_Ing ok")

'''加入mod功能'''

try:
    Boot_file_path_dir_exp
except:
    print('未分配文件路径')
    Boot_file_path_dir_exp=dir_exp.Mou(os.path.dirname(__file__))
#如果索引不到mods文件夹的话则创建一个
if not Boot_file_path_dir_exp['Boot']['mods']:
    Boot_file_path_dir_exp['Boot']['mods']=None
#迭代导入附加模组
def load_mods():
    mod=Boot_file_path_dir_exp['Boot']['mods']
    import_mod=mod['*.py']
    import_mod_tuple= tuple(map(lambda i:(i%1).rstrip('.py') ,import_mod)) if type(import_mod)==list else ((import_mod%1).rstrip('.py'),)
    #加入环境变量
    sys.path.append(str(mod))
    #判断如果在idle中运行则跳过进度条
    print_bool =False if psutil.Process(os.getppid()).name()=="pythonw.exe" else True
    USE.use(*import_mod_tuple,glo=g_l.__dict__,print_bool=print_bool,text='加载模组...')
load_mods()
