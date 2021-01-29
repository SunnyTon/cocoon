import requests
import unittest
import logging
import addCenterWarehouseDataTemplate
from urllib import  parse  #使用requests发送post请求，body的汉字会进行url编码，即%xx形式。想看到原始body，需要使用parse.unquote进入url解码
class test_syn_sto_from_centerwarehouse(unittest.TestCase):
    """添加调拨单接口"""
    @classmethod
    def setUpClass(cls):
        cls.url='http://cqstt-test.sxcq2015.com/stt-erp/admin/stomaster/synStoFromCenterWarehouse'
    @classmethod
    def tearDownClass(cls):
            pass
    def setUp(self):
            pass
    def tearDown(self):
            pass
    def test00(self): #代码逻辑::获取当前最新发布会ID，设置入参，eid置空，发送post请求
        """添加date为空生成"""
        cid=''
        data=addCenterWarehouseDataTemplate.getCenterWarehouseData(cid)
        r=requests.post(self.url,data=data)
        code=r.json()['code']
        self.assert_(code,0)
        logging.info(f"case:生成调拨单，date为空\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")
if __name__ == '__main__':
    unittest.main(verbosity=2)