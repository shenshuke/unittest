import unittest
import requests
import HTMLTestRunner
from selenium import webdriver


class test_serchtest(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start>>>>>>")
        pass

    def test_search_by_id(self):
        print("working>>>>>>")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://sso.xnjd.cn/login?service=http%3A%2F%2Fstudy.xnjd.cn%2FIndex_index.action")
        self.search_by_id = self.driver.find_element_by_id("username")
        self.search_by_id.clear()
        self.search_by_id.send_keys("18920863")
        self.search_by_id = self.driver.find_element_by_id("password")
        self.search_by_id.clear()
        self.search_by_id.send_keys("864724")
        self.search_by_mane_submit = self.driver.find_element_by_name("submit")
        self.search_by_mane_submit.click()
        sever_code = requests.get(
            "http://sso.xnjd.cn/login?service=http%3A%2F%2Fstudy.xnjd.cn%2FIndex_index.action").status_code
        self.assertEqual(200, sever_code)
        self.driver.quit()

    def tearDown(self):
        print("over>>>>")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
