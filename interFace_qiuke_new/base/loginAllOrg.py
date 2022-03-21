# coding=utf-8
# 封装各组织层级的登录

from util.operation_json import operationJson
from base.runmethod import runMethod
import hashlib

class login_all_org:

    def login_and_write_token(self,id,pw):
        url = operationJson(file_path='../data/url.json').get_data("url")
        path = "/api/doraemon-oauth/oauth/token"
        data = {"username": id,
                "password": pw,
                "grant_type": "password"
                }
        header = {"Authorization": "Basic dXNlcmNlbnRlcjoxMTg2MDQ1ZDU1OTlkZTZlZjJjYTI4MjM0N2E1NWNhMg=="}
        res = runMethod().post_main(url=url + path, data=data, header=header)
        res = res.json()
        if (res['code'] == 200) and (res['success'] == True):
            key = str(id)+'_token'
            velue = res['token_type'] + " " + res['access_token']
            token_file_path = '../data/token.json'
            operationJson(token_file_path).write_data_with_key_and_velue(key,velue)     # 以增量或修改的方式将token写入json文件中

            userid_file_path = '../data/useridAndOrgid.json'
            useridKey = str(id)+'_userid'
            orgidKey = str(id)+'_orgid'
            usernameKey = str(id)+'_username'
            userid = res['user_id']
            orgid = res['org_id']
            username = res['user_name']
            operationJson(userid_file_path).write_data_with_key_and_velue(useridKey,userid)   # 写入userid
            operationJson(userid_file_path).write_data_with_key_and_velue(orgidKey,orgid)    # 写入orgid
            operationJson(userid_file_path).write_data_with_key_and_velue(usernameKey,username)    # 写入username
        else:
            print(res)


    def login_admin(self):
        file_path = '../data/idAndPw.json'
        idAndPwData = operationJson(file_path).read_data()
        if ('adminid' in idAndPwData) and ('adminpw' in idAndPwData):
            id = operationJson(file_path).get_data("adminid")
            pw = operationJson(file_path).get_data("adminpw")
            pw = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()  # 密码需要转码MD5
            self.login_and_write_token(id,pw)
        else:
            print("没有获取到json文件中的adminid或adminpw，请检查添加")

    def login_wangge(self):
        file_path = '../data/idAndPw.json'
        idAndPwData = operationJson(file_path).read_data()
        if ('wanggeid' in idAndPwData) and ('wanggepw' in idAndPwData):
            id = operationJson(file_path).get_data("wanggeid")
            pw = operationJson(file_path).get_data("wanggepw")
            pw = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()  # 密码需要转码MD5
            self.login_and_write_token(id, pw)
        else:
            print("没有获取到json文件中的wanggeid或wanggepw，请检查添加")

    def login_shequ(self):
        file_path = '../data/idAndPw.json'
        idAndPwData = operationJson(file_path).read_data()
        if ('shequid' in idAndPwData) and ('shequpw' in idAndPwData):
            id = operationJson(file_path).get_data("shequid")
            pw = operationJson(file_path).get_data("shequpw")
            pw = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()  # 密码需要转码MD5
            self.login_and_write_token(id, pw)
        else:
            print("没有获取到json文件中的shequid或shequpw，请检查添加")
            
    def login_jiedao(self):
        file_path = '../data/idAndPw.json'
        idAndPwData = operationJson(file_path).read_data()
        if ('jiedaoid' in idAndPwData) and ('jiedaopw' in idAndPwData):
            id = operationJson(file_path).get_data("jiedaoid")
            pw = operationJson(file_path).get_data("jiedaopw")
            pw = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()  # 密码需要转码MD5
            self.login_and_write_token(id, pw)
        else:
            print("没有获取到json文件中的jiedaoid或jiedaopw，请检查添加")
            
    def login_quxian(self):
        file_path = '../data/idAndPw.json'
        idAndPwData = operationJson(file_path).read_data()
        if ('quxianid' in idAndPwData) and ('quxianpw' in idAndPwData):
            id = operationJson(file_path).get_data("quxianid")
            pw = operationJson(file_path).get_data("quxianpw")
            pw = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()  # 密码需要转码MD5
            self.login_and_write_token(id, pw)
        else:
            print("没有获取到json文件中的quxianid或quxianpw，请检查添加")
    



if __name__ == "__main__":
    LAO = login_all_org().login_admin()