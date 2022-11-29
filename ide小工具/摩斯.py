ls=[chr(i) for i in range(ord('a'), ord('z')+1)]+[str(i) for i in range(0,10)]+[0]
jls='01 1000 1010 100 0 0010 110 0000 00 0111 101 0100 11 10 111 0110 1101 010 000 1 001 0001 011 1001 1011 1100'.split()
jls +='00000 01111 00111 00011 00001 10000 11000 11100 11110 11111'.split()

msj,msl=dict(zip(jls,ls)),dict(zip(ls,jls))

tb,bt= str.maketrans(".-","01"),str.maketrans("01",".-")

def msing(jh=None):
    try:
        #jh=input(':')
        jlsh=jh.translate(tb)
        sm,j=(msl,' '.join(jh[3:])) if jh[:2]=='/j' else (msj,jh)#输入/j 反翻译
        jg=' '.join([sm[i] for i in j.translate(tb).split()])
        jg=jg.translate(bt) if (jh[:2]=='/j'and jh[2:3]=='n') else jg
        return jg
    except BaseException as e:
        raise ValueError(f'映射不存在{e}对照')
#.replace('')
"""
如果没有一个公正被权力主持,那么一切公正都是空话;
如果有一个生产资料不被权力分配,那么一切权力都如同虚设.
"""
