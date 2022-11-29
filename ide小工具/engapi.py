import requests
from string import Template
from playsound import playsound as pd
lod=''
yd_lang=tuple("""
    ar
    yue
    ca
    cs
    da
    nl
    en-AUS
    en-GBR
    en-IND
    en-USA
    en
    fi
    fr-CAN
    de
    de
    el
    he
    hi
    hu
    it
    ja
    ko
    zh-CHS
    zh-TWN
    no
    pl
    pt-BRA
    pt
    ro
    ru
    sk
    es
    sv
    th
    tr
    id
    vi
    """.split('\n    ')[1:-1])


def oppen(voice,ld='mp3'):
    try:
        with open(r'.\txten.'+ld,'wb') as f:
            f.write(voice)
            f.close()
    except:
        print('保存失败')
        
def txengmp(lit:'英语单词'='English words'):
    global lod,voice
    if lod == lit:
        return mp()
    api=Template(f'http://dict.youdao.com/dictvoice?type=1&audio={lit}')
    voice = requests.get(api.substitute(lit=lit)).content
    #print(api.substitute(lit=lit))
    lod=lit
    oppen(voice)
    return mp()
def txchemp(lit:'中英混'='你好输入English words',log='zh'):
    global lod,voice
    if lod == lit:
        return mp()
    api=Template(f"http://tts.youdao.com/fanyivoice?word={lit}&le={log}&keyfrom=speaker-target")
    voice = requests.get(api.substitute(lit=lit)).content
    #print(api.substitute(lit=lit))
    lod=lit
    oppen(voice)
    return mp()
def txlogmp(lit:'字词,句',log:'语言'):
    pass

#播放
def mp(tmp='txten.mp3'):
    global pd
    try:
        pd(tmp)
    except:
        from playsound import playsound as pd
        try:
            pd(tmp)
        except:
            try:
                if tmp.split('.')[1]=='wav':
                    raise '无效'
                oppen(voice,ld='wav')
                mp('txten.wav')
            except:
                print('播放失败')
if __name__=='__main__':
    #txengmp()
    txchemp()
    
