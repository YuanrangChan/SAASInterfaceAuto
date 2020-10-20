# coding:utf-8
import unittest,requests,json
from selenium import webdriver

# 测试
gateway = 'http://119.28.123.164:80'
# # gateway_test = 'http://119.28.123.164:80'
headers_ = {'Content-type': 'application/json;utf-8'}  # 有些接口把租户放在body里面
tenantId = "CL"
headers1 = {'Content-type': 'application/json;utf-8', "tenantId": tenantId}  # 有些接口把租户放在header里面

class TestTaskServiceThree(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test_01(self):
        a = 1
        b = 2
        self.assertTrue(3, a+b)

    def test_02(self):
        a = 1
        b = 0
        self.assertTrue(3, a / b)

    def test_03(self):
        a = 3
        b = 2
        # self.assertTrue(6, a*b)
        self.assertEqual(61, a*b)

    def test_case01(self):
        '''查询任务操作服务'''
        url = gateway + '/dds-tms/taskRestService/queryTaskOperate'
        body = {
                 "systemCode": "JV-DDS-TMS",
                 "operateEmpCode":"CL10000411",
	             "taskCode":"V66VHRTL",
	             "orgCode":"CLCMB01AJ1",
                 "cityCode": "CLCMB01",
                 "tenantId":"CL"
             }
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code,200,'返回状态码正常，为200')
        # self.assertNotEqual(response.json()["obj"]["dataVersion"],None,'返回dataVersion不为null') #dataVersion .json()["obj"]["dataVersion"]
        print('查询任务操作服务接口正常')


    def test_case02(self):
        '''根据任务码查询任务详情'''
        url = gateway + '/dds-tms/taskRestService/queryTaskDetail'
        body = {
                "systemCode": "JV-DDS-TMS",
                "operateEmpCode": "CL10000411",
                "taskCode": "V66VHRTL",
                "cityCode": "CLCMB01",
                "tenantId":"CL"
           }
        response = requests.post(url=url, headers=headers_, data=json.dumps(body))
        self.assertEqual(response.status_code,200,'返回状态码正常，为200')
        # self.assertNotEqual(response.json()["obj"]["sortCells"],None,'正常返回分拣计划格口') #sortCells .json()["obj"]["sortCells"]
        print('根据任务码查询任务详情接口正常')

    def test_case03(self):
        '''更新任务状态'''
        url = gateway + '/dds-tms/taskRestService/updateTaskStatus'
        body = {
                  "actualPickPackageNum": 0,
                  "bagReqs": [
                      {
                          "bagNo": "CL1111000002444",
                          "contentType": "1",
                          "packageNos": []
                      }
                  ],
                  "carNo": "",
                  "cdsOperateType": 0,
                  "cityCode": "CLCMB01",
                  "firstPick": True,
                  "lockerNoList": [],
                  "noUploadLoad": False,
                  "operateEmpCode": "CL10000411",
                  "operateType": 2,
                  "orgCode": "CLCMB01DJ1",
                  "resourceSource": 0,
                  "resourceSourceName": "自有骑士",
                  "systemCode": "SAAS_DDS_TALLY",
                  "taskCode": "V9F4RR4H",
                  "tenantId": "CL",
                  "updateBagList": [
                          "CL1111000002444"
                                   ]
                   }
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code, 200, '返回状态码正常，为200')
        self.assertEqual(response.json()["success"], True, 'success值为true')
        # self.assertNotEqual(response.json()["obj"]["destDeptCode"], None,'RLS路由查询正常')  # sortCells .json()["obj"]["sortCells"]
        print('更新任务状态接口正常')

    # def test_07(self):
    #     self.driver.find_element_by_id("kw").send_keys("yoyo")
    #
    #
    # def test_08(self):
    #     self.driver.find_element_by_id("kw").send_keys("haha")

if __name__ == "__main__":
    unittest.main()
