from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

class test_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniel\Desktop\chromedriver\chromedriver.exe")
        self.driver.get('http://172.20.50.128:8080/sijai/unsecure/login.xhtml')

    def test_001(self):
        time.sleep(3)
        usuario = self.driver.find_element_by_id("j_idt14")
        usuario = self.driver.find_element_by_id("userName")
        time.sleep(1)
        usuario.send_keys("daniel")
        usuario.click()
        time.sleep(1)
        password = self.driver.find_element_by_id("j_idt15")
        password = self.driver.find_element_by_id("password")
        time.sleep(1)
        password.send_keys("test1234")
        password.click()
        time.sleep(1)
        ingresar = self.driver.find_element_by_id("login")
        time.sleep(1)
        ingresar.click()
        time.sleep(5)


    def tearDown (self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()