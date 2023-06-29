#-*- coding:utf-8 -*-
if 'pickle' not in globals():
    gls=globals()
    import pickle
    __all__=('run_dump','run_load','gls')
def run_dump(lop=globals(),lod=r'.\global.log'):
    with open(lod,'wb') as f:
        lop=lop.copy()
        lop=tuple(filter(lambda i:('__'not in i[0])and i[0]not in ['pickle','f'],lop.items()))
        #print(lod,'_'*10,lop)
        pickle.dump(lop,f)
        
def run_load(lod=r'.\global.log'):
    with open(lod,'rb') as f:
        loop=pickle.load(f)
    return loop
