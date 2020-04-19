from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains

class test_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniel\Desktop\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://testeandosoftware.com/blogs-de-testing-en-espanol/')


    def test_001(self):
        time.sleep(3)
        buscar=self.driver.find_element_by_class_name("search-field")
        buscar.click()
        time.sleep(3)
        buscar.send_keys("Testing Manual")
        time.sleep(3)
        buscar.send_keys(Keys.ENTER)
        time.sleep(3)
        buscar = self.driver.find_element_by_class_name("search-field")
        buscar.click()
        buscar.send_keys(Keys.BACKSPACE)
        buscar.clear()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        accion = ActionChains(self.driver)
        formacion = self.driver.find_element_by_xpath("//*[@id='mainnav-menu']/li[2]")
        accion.move_to_element(formacion).perform()
        presentacion = self.driver.find_element_by_xpath("//*[contains(text(), 'Presentaciones')]")
        accion.move_to_element(presentacion).perform()
        presentacion.click()
        time.sleep(10)

    def tearDown(self):
            assert 'Presentación Archives - Testeando Software' in self.driver.title #para verificar el nombre del titulo
            self.driver.close()

if __name__ == '__main__':
    unittest.main()