# coding=utf-8
# 封装get/post请求
import requests
import json

class runMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url = url,data = data,headers = header)
        else:
            res = requests.post(url = url,data = data)
        return res

    def get_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header)
        else:
            res = requests.get(url=url,data=data)
        return res



if __name__ == "__main__":
    url = 'http://192.168.10.116:1000/api/doraemon-oauth/oauth/token'
    data = {
        'tenantId': '000000',
        'username': 'lycs@',
        'password': '1bbd886460827015e5d605ed44252251',
        'grant_type': 'password',
        'scope': 'all'
    }
    header = {
        'Authorization': 'Basic dXNlcmNlbnRlcjoxMTg2MDQ1ZDU1OTlkZTZlZjJjYTI4MjM0N2E1NWNhMg=='
    }

    res = runMethod().post_main(url=url,data=data,header=header)
    print(res)


