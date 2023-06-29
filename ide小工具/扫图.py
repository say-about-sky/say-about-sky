# -*- coding: utf-8 -*-
#import glob
from os import path#path.join将两个路径拼接
import os,sys
from aip import AipOcr
exec('from PIL import Image')
from io import BytesIO
import json
#压缩图片
def convertimg(picfile:'图片地址',format:'PNG or JPEG'='JPEG'):
    img = Image.open(picfile)
    width, height = img.size
    while(width*height > 4000000):  # 该数值压缩后的图片大约 两百多k
        width = width // 2
        height = height // 2
    new_img=img.resize((width, height),Image.Resampling.BILINEAR)
    img_byte = BytesIO()
    #解码为二进制
    new_img.save(img_byte,format=format)
    #获取值
    binary_content = img_byte.getvalue()
    #返回压缩后图片的二进制形式编码
    return binary_content

#利用百度api识别文本，并保存提取的文字
def baiduOCR(picfile:'图片的二进制形式(字节)', outfile=None,js=r'.\account.json'):
    """利用百度api识别文本，并保存或返回提取的文字
    picfile:    图片文件名
    outfile:    输出文件
    """
    
    with open(js)as f:
        add=json.loads(f.read())
    APP_ID = add['APP_ID'] # 刚才获取的 ID，下同
    API_KEY = add['API_KEY']
    SECRECT_KEY = add['SECRECT_KEY']
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    try:
        img = convertimg(picfile)
    except:
        img = picfile
    
    #print("正在识别图片：\t")
    message = client.basicGeneral(img)   # 通用文字识别，每天 50次免费
    #message = client.basicAccurate(img)   # 通用文字高精度识别，每天 8 次免费
    #print("识别成功！")
    try:
        val='\n'.join((i['words'] for i in message['words_result']))
    except:
        try:
            print(message['error_msg'])
        except BaseException as e:
            print('捕获失败:',e)
            return sys.exit()
    if outfile:
        with open(outfile, 'a+') as fo:
            # 输出文本内容
            fo.write(val)
    else:
        return val
if __name__=='__main__':
    print(baiduOCR(sys.argv[1],sys.argv[2] if sys.argv[2:]else None))
