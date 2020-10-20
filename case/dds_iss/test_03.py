# coding:utf-8
import unittest,requests,json
from selenium import webdriver
import time

# 测试
gateway = 'http://119.28.123.164:80'
# # gateway_test = 'http://119.28.123.164:80'
headers_ = {'Content-type': 'application/json;utf-8'}  # 有些接口把租户放在body里面
tenantId = "CL"
headers1 = {'Content-type': 'application/json;utf-8', "tenantId": tenantId}  # 有些接口把租户放在header里面

class TestISSServiceThree(unittest.TestCase):
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
        '''分页拉取基础接驳点信息'''
        url = gateway + '/o2o-dds-iss-jv/tranShipPointInfo/getTranShipPointInfoV1'
        body = {
               "pageNum": "0",
               "pageSize": 800,
               "cityCode": "S437674",
               "areaCode": "CLCMB01",
               "dataVersion": "1577687297121"
                  }
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code,200,'返回状态码正常，为200')
        self.assertNotEqual(response.json()["obj"]["dataVersion"],None,'返回dataVersion不为null') #dataVersion .json()["obj"]["dataVersion"]
        print('拉取接驳点接口正常')


    def test_case02(self):
        '''查询指定网点所有分拣计划'''
        url = gateway + '/o2o-dds-iss-jv/sortCellSetService/querySortCell'
        body = {
              "bagSrcDeptcode": "CLCMB01A",
              "dataVersion": "0"
         }
        response = requests.post(url=url, headers=headers_, data=json.dumps(body))
        self.assertEqual(response.status_code,200,'返回状态码正常，为200')
        self.assertNotEqual(response.json()["obj"]["sortCells"],None,'正常返回分拣计划格口') #sortCells .json()["obj"]["sortCells"]
        print('查询分拣计划接口正常')

    def test_case03(self):
        '''RLS路由查询'''
        url = gateway + '/o2o-dds-iss-jv/RLS/callRlsByBnoV1'
        body = {
                "waybillNo": "CL1504567994207",
                "username": "CL10000399",
                "mark": "3"
            }
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code, 200, '返回状态码正常，为200')
        self.assertEqual(response.json()["success"], True, 'success值为true')
        self.assertNotEqual(response.json()["obj"]["destDeptCode"], None,'RLS路由查询正常')  # sortCells .json()["obj"]["sortCells"]
        print('RLS路由查询接口正常')

    def test_case04(self):
        '''分拣'''
        url = gateway + '/o2o-dds-iss-jv/buildBag/addBagPackageBySort'
        body = [
                 {
                     "bagType": "3",
                     "cellNo": "A-A02",
                     "checkType": "1",
                     "destDeptCode": "CLCMB01AA02",
                     "id": 0,
                     "orgCode": "CLCMB01A",
                     "planType": "2",
                     "sortPlan": "CLCMB01A_SortPlan",
                     "sortVersion": "1588734808756",
                     "waybillNoList": [
                         "CL1504567994207"
                     ]
                 }
              ]
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code, 200, '返回状态码正常，为200')
        self.assertEqual(response.json()["success"], True, 'success值为true')
        # self.assertNotEqual(response.json()["obj"]["destDeptCode"], None,'RLS路由查询正常')  # sortCells .json()["obj"]["sortCells"]
        print('分拣接口正常')

    def test_case05(self):
        '''接口名称：根据包号或运单号查询包信息
           功能描述：分拣中的加件入包；根据包号或运单号查询暂存包或已建包的记录。
           调用方式：http post'''
        url = gateway + '/o2o-dds-iss-jv/buildBag/getPackageList'
        body = {
                   "bagNo": "CL1111000002375"
               }
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code, 200, '返回状态码正常，为200')
        self.assertEqual(response.json()["success"], True, 'success值为true')
        # self.assertNotEqual(response.json()["obj"]["destDeptCode"], None,'RLS路由查询正常')  # sortCells .json()["obj"]["sortCells"]
        if response.json()["success"] == True:
            print('查询到包信息')
        else:
            print("查不到包信息")

    # def gen_ContainerNo(tenantId):
    #     url = gateway + '/shivaomspcmjv/containerNo/generateContainerNo'
    #     body = {
    #         "requestId": genRandomString(20),
    #         "systemCode": "NEXT-TCS",
    #         "containerType": "1",  # containerType String(5) 是 容器类型（1：物理包号；2：虚拟包号）
    #         "generateNum": 1,
    #         "operateDeptCode": "149666855",
    #         "operateEmpCode": "149855",
    #         "operateTm": str((round(time.time() * 1000))),
    #         "tenantId": tenantId,
    #         "tenantPrefix": tenantId
    #     }
    #     global ContainerNo
    #     r = requests.post(url, headers=headers_, data=json.dumps(body))
    #     ContainerNo = r.json()["obj"]
    #     ContainerNo_s = " ".join(ContainerNo)
    #     return ContainerNo_s
    # def gen_saaswaybillNo(tenantId):
    #     url = gateway + '/saas-bsp-service/waybillno/batchCreate'
    #     body = {
    #         "tenantId": tenantId,
    #         "count": "1"
    #     }
    #     r = requests.post(url, headers=headers_, data=json.dumps(body))
    #     # print(r.json())
    #     waybillNo_list = r.json()["obj"]
    #     waybillNo = waybillNo_list[0]
    #     return waybillNo

    def test_case06(self):
        # '''1.先从PCM获取包号'''
        url = gateway + '/shivaomspcmjv/containerNo/generateContainerNo'
        body = {
            "requestId": str((round(time.time() * 1000))),
            "systemCode": "NEXT-TCS",
            "containerType": "1",  # containerType String(5) 是 容器类型（1：物理包号；2：虚拟包号）
            "generateNum": 1,
            "operateDeptCode": "149666855",
            "operateEmpCode": "149855",
            "operateTm": str((round(time.time() * 1000))),
            "tenantId": tenantId,
            "tenantPrefix": tenantId
        }
        global ContainerNo
        r = requests.post(url, headers=headers_, data=json.dumps(body))
        ContainerNo = r.json()["obj"]
        bagNo = " ".join(ContainerNo)

        # '''2.先从BSP获取运单号'''
        url = gateway + '/saas-bsp-service/waybillno/batchCreate'
        body = {
            "tenantId": tenantId,
            "count": "1"
        }
        r = requests.post(url, headers=headers_, data=json.dumps(body))
        # print(r.json())
        waybillNo_list = r.json()["obj"]
        waybillNo = waybillNo_list[0]

        # '''3.建包'''
        '''建包'''
        url = gateway + '/o2o-dds-iss-jv/buildBag/addBagPackage'
        body = [
                  {
                      "bagNo": bagNo,
                      "checkType": "1",
                      "destDeptCode": "",
                      "operateEmpCode": "CL10000399",
                      "orgCode": "CLCMB01A",
                      "waybillNoList": waybillNo
                  }
              ]
        response = requests.post(url=url, headers=headers1, data=json.dumps(body))
        self.assertEqual(response.status_code, 200, '返回状态码正常，为200')
        self.assertEqual(response.json()["success"], True, 'success值为true')
        # self.assertNotEqual(response.json()["obj"]["destDeptCode"], None,'RLS路由查询正常')  # sortCells .json()["obj"]["sortCells"]
        if response.json()["success"] == True:
            print('空单建包成功')
        else:
            print("空单建包失败")

    # def test_07(self):
    #     self.driver.find_element_by_id("kw").send_keys("yoyo")
    #
    #
    # def test_08(self):
    #     self.driver.find_element_by_id("kw").send_keys("haha")

if __name__ == "__main__":
    unittest.main()
