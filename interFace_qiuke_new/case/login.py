# coding=utf-8
# 封装登录的用例

from base.runmethod import runMethod
from base.loginAllOrg import login_all_org
from util.operation_json import operationJson
import unittest
import datetime

class Login(unittest.TestCase):
    """中国层级账号登录接口集合"""

    @classmethod
    def setUpClass(self):
        """登录管理员账号，获取token"""
        login_all_org().login_admin()     # 以admin登录
        self.url = operationJson(file_path='../data/url.json').get_data("url")
        self.auth = operationJson(file_path='../data/token.json').get_data('qiuke_token')
        self.username = operationJson(file_path='../data/useridAndOrgid.json').get_data('qiuke_username')
        self.userid = operationJson(file_path='../data/useridAndOrgid.json').get_data(('qiuke_userid'))
        self.orgid = operationJson(file_path='../data/useridAndOrgid.json').get_data('qiuke_orgid')

    def test_getByUserName(self):
        """接口：/api/doraemon-user/user/getByUserName"""
        path = "/api/doraemon-user/user/getByUserName"
        data = {"userName":self.username}
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()      # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'],200)
        self.assertEqual(res['success'],True)
        self.assertEqual(res['msg'],'操作成功')
        self.assertLess(duration,1000)
        self.assertIsNotNone(res['data'])

    def test_getUserVO(self):
        """接口：/api/doraemon-user/user/getUserVO"""
        path = '/api/doraemon-user/user/getUserVO'
        id = self.userid
        data = {"id":id}
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_listUserUnReadMsg(self):
        """接口：/api/tq-scgrid-message-service/userMsg/listUserUnReadMsg"""
        path = "/api/tq-scgrid-message-service/userMsg/listUserUnReadMsg"
        userid = self.userid
        data = {"userId":userid}
        header = {"auth":self.auth}
        res = runMethod().post_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_myMessageListPage(self):
        """接口：/api/tq-scgrid-message-service/msgManage/myMessageListPage"""
        path = "/api/tq-scgrid-message-service/msgManage/myMessageListPage"
        data = {"page":1,
                "rows":100,
                "readStatus":0,
                "userId":self.userid
                }
        header = {"auth":self.auth}
        res = runMethod().post_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_userHasConfigManageArea(self):
        """接口：/api/tq-scgrid-doraemon-system-extend/organizationExtend/userHasConfigManageArea"""
        path= "/api/tq-scgrid-doraemon-system-extend/organizationExtend/userHasConfigManageArea"
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,None,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_listSCGridAppBaseMenu(self):
        """接口：/api/tq-scgrid-doraemon-system-extend/menu/listSCGridAppBaseMenu"""
        path = "/api/tq-scgrid-doraemon-system-extend/menu/listSCGridAppBaseMenu"
        data = {"groupEname":"LightGroup"}
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_infos(self):
        """接口：/api/mms/infos"""
        path = "/api/mms/infos"
        data = {"namespaces":"screen,information,issue,safety,comprehensivestat,office,accept,http://10.0.188.11:28096/socialWaring/waringView,extapp"}
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        #self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionScreen(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"screen:workbench"}
        header = {"auth":self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionIssue(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"issue:myIssue:needDoIssue"}
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url + path, data, header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionSafety(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"safety:drugManage:drugVisit:sign"}
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url + path, data, header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionGrid(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"grid:gridPower:gridMember:approve"}
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url + path, data, header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionAccept(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"accept:appeal:needAccept:accept"}
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url + path, data, header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_checkUserPermissionComprehensivestat(self):
        """接口：/api/tq-project-workbench/workbench/checkUserPermission"""
        path = "/api/tq-project-workbench/workbench/checkUserPermission"
        data = {"ename":"comprehensivestat:workload:issueWorkload"}
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url + path, data, header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_findLatestEventList(self):
        """接口：/api/tq-project-workbench/workbench/findLatestEventList"""
        path = "/api/tq-project-workbench/workbench/findLatestEventList"
        data = {"orgId":self.orgid,
                "size":20,
                "scope":2,
                "keywords":None
                }
        header = {"auth":self.auth}
        res = runMethod().post_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    def test_findIssueCompositeStatistics(self):
        """接口：/api/tq-project-workbench/workSurvey/findIssueCompositeStatistics"""
        path = "/api/tq-project-workbench/workSurvey/findIssueCompositeStatistics"
        data = {"orgId":self.orgid,
                "year":datetime.datetime.now().year,
                "month":datetime.datetime.now().month,
                "scope":1
                }
        header = {"auth": self.auth}
        res = runMethod().get_main(self.url+path,data,header)
        duration = res.elapsed.total_seconds()  # 获取响应时间
        res = res.json()
        self.assertEqual(res['code'], 200)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['msg'], '操作成功')
        self.assertLess(duration, 1000)
        self.assertIsNotNone(res['data'])

    @classmethod
    def tearDownClass(self):
        print("___________end_________")


if __name__ == "__main__":
    unittest.main()

