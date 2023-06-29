"""
import os
import openai
#from api_secrets import API_KEY
#openai.organization = "org-ni6n0PeFw7OYwJtcC07yqU4Z"
#openai.api_key = os.getenv("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")
#lis=openai.Model.list()
#api_key="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"
"""
import openai
'''
en={
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0,
  "top_p": 1,
  "n": 1,
  "stream": False,
  "logprobs": None,
  "stop": "\n"
}
'''
#登录
def login(api_key = "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"):
    openai.api_key=api_key
#发送请求
def run_openai(prompt='',engine="text-ada-001",start='',end='',**kv):
    #temperature=1,top_p=1,max_tokens
    lod_kv={"max_tokens":1024,'n':1,'temperature':0.5}
    kv=dict(filter(lambda i:'__' not in i[0] and not i[0] in run_openai.__code__.co_varnames,kv.items()),**lod_kv)
    #print(kv)
    print(end=start)
    if prompt in ['??','&?','?&','?*','*?','-list','--list']:
        hel=openai.Model.list()
        add=[i['id'] for i in hel['data']]
        print(add)
        return add
    response = openai.Completion.create(
        engine=engine,
        #model="text-davinci-003",
        prompt=prompt,**kv)
    print(end=end)
    return response

if __name__=='__main__':
    import sys
    login()
    if sys.argv[1:] and sys.argv[1]!="model":
        print('正在思考..')
        print(run_openai(sys.argv[1])["choices"][0]["text"].strip())
    elif sys.argv[1]=="model":
        print('正在思考..')
        print(run_openai(sys.argv[3],engine=sys.argv[2])["choices"][0]["text"].strip())


