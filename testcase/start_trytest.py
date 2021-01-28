from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
import  unittest
import time,os

class tryTest(unittest.TestCase):
    url = "https://xnjd.cn"
    driver = webdriver.Chrome()
    def setup(self):
        print("start")
        pass
    def test_login(self):
        print("working")
        try:
            self.driver.find_element_by_name("password").click()
        except NoSuchElementException as msg:
            print("定位元素异常！")
            notime =time.strftime("%Y%m%d.%H.%M.%S")
            t = self.driver.get_screenshot_as_file("%s,jpg"%notime).
    def setup(self):
        print("over")
        self.driver.quit()

if __name__=="__main__" :
    unittest.main()