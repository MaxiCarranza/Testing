from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains

class test_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniel\Desktop\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.cantv.com.ve/')



    def test_01(self):
        #anuncio = self.driver.find_element_by_class_name('fancy-imagine')
        anuncio = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/img')
        time.sleep(5)
        anuncio.clic()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()