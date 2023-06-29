import json
import glob
from os import path#path.join将两个路径拼接
import os
from PIL import Image
from io import BytesIO
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
#image图片形式转base64字符串#暂时不用
def image_to_base64(image: Image.Image, fmt='png') -> str:
    output_buffer = BytesIO()
    image.save(output_buffer, format=fmt)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    return f'data:image/{fmt};base64,' + base64_str
#压缩图片
def convertimg(picfile,format:'PNG or JPEG'='JPEG'):
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
def tenxOCR(picfile:'二进制形式',outfile=None):
    #转换为Base64字符串
    picfile=str(base64.b64encode(picfile),'utf-8')
    #return picfile
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
    cred = credential.Credential("AKID1aAlOtRxSyRoAXvDWnAJHcpGK3hEqXAf",
                                 "aBlTGMVet5BOSQEyc2N0Ul2HMGHEICxt")
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.GeneralBasicOCRRequest()
    params = {
        "Action":"GeneralBasicOCR",
        "Version":"2022-11-23",
        "Region":"ap-beijing",
        "ImageBase64":picfile#图片的 Base64值
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个GeneralBasicOCRResponse的实例，与请求对象对应
    resp = client.GeneralBasicOCR(req)
    # 输出json格式的字符串回包
    if outfile:
        with open(outfile, 'a+') as fo:
            # 输出文本内容
            fo.write(resp)
    else:
        return resp#.to_json_string()

if __name__=='__main__':
    try:
        #调用api识图
        ddf=tenxOCR(convertimg(picfile=r"C:\Users\saysky\Desktop\语文\sept.png"))
        #获取文本
        print('\n'.join((i.DetectedText for i in ddf.TextDetections)))
    except TencentCloudSDKException as err:
        print(err)
