import requests,re
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
data_value=('AUTO','dict','fanyideskweb','16611770649142','4ed326d5b51b81dcdf3d60d4f2dbe9d5','json','2.1','fanyi.web','FY_BY_REALTIME','1661177064914','50b61ff102560ebc7bb0148b22d7715c')
data_key=('type', 'smartresult', 'client', 'salt', 'sign', 'doctype', 'version', 'keyfrom', 'action', 'Its', 'bv')
def tetr(str_i:str='你好 世界'):
    data_dict={'i':str_i}
    data_dict.update(dict(zip(data_key,data_value)))
    response = requests.post(url,headers=headers,data=data_dict)
    dictTrans = response.json()
    return ''.join((i['tgt'] for i in dictTrans['translateResult'][0]))
