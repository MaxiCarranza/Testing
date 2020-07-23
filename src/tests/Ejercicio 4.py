import unittest
import time
from selenium import webdriver


class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniel\Desktop\chromedriver\chromedriver.exe")
        self.driver.get('https://testeandosoftware.com/blogs-de-testing-en-espanol/')

    def test_001(self):
        noticias=self.driver.find_element_

        time.sleep(5)


    def tearDown(self):
      self.driver.close()

if __name__ == '__main__':
    unittest.main()