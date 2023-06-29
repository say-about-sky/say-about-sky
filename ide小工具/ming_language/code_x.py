
runt=re.findall(r'((?P<len>[$](.*?))([^$]+.*?))',txt)
fun_all=re.search('(.*?)[{]',runt[0][-1]).group()[0:-1]
fun_name=re.search('(.*?)[(]',fun_all).group()[:-1] if '(' in fun_all else fun_all
#fn是提取出来的要写入的代码内容
fn=regex.search("(?<rec>\\{(?:[^{}]++|(?&rec))*\\})",runt[0][-1],flags=regex.VERBOSE).group()[1:-1]
with open(os.path.join(os.path.dirname(rust_path),'lib_lod.rs')) as f:lib_txt=f.read()
guess_the_number_name_s=lib_txt.find("#[pyfunction]")+len("#[pyfunction]")
guess_the_number_name_e=lib_txt.find("fn guess_the_number")
guess_the_number_name_sub=f'\n#[pyo3(name = "{fun_name}")]\n'

guessing_game_name_s=lib_txt.find("#[pymodule]")+len("#[pymodule]")
guessing_game_name_e=lib_txt.find("fn guessing_game")
guessing_game_name_sub=f'\n#[pyo3(name = "{mod_name}")]\n'
                
sten=lib_txt[guess_the_number_name_e:guessing_game_name_s]
                
lop=re.search(r'fn guess_the_number(.*?)[{]',sten)
new_lib_txt=(sten[:lop.end()]+fn+sten[lop.end():]).rstrip()

stn=(lib_txt[:guess_the_number_name_s],
            guess_the_number_name_sub,
            new_lib_txt,
            guessing_game_name_sub,
            lib_txt[guessing_game_name_e:])
