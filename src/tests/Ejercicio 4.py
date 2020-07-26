import unittest
import time
from selenium import webdriver


class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniel\Desktop\chromedriver\chromedriver.exe")
        self.driver.get('http://automationpractice.com/index.php')

    def test_001(self):
        #buscar = self.driver.find_element_by_xpath('//input[contains(text(), "search_query")]').send_keys("camisas") "aplica para combo list
        #buscar = self.driver.find_element_by_xpatch('//button)
        buscar = self.driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys("camisas")
        #busqueda =self.driver.find_element_by_name('submit_search').click() "esto tmb esta bien"
        busqueda = self.driver.find_element_by_xpath('//*[@id="searchbox"]/button').click()

        #prueba = self.driver.find_element_by_xpath('//a[@title="Best Sellers"]').click()
        time.sleep(4)
        #botonOrganizar = self.driver.find_element_by_xpath('//div[contains(text(),"10022-libres_de_sucursales")]')
        resultado = self.driver.find_element_by_xpath('//p[@class="alert alert-warmign"]')
        self.assertEqual(resultado.text,'No results were found for your search "camisas"')

')



    def tearDown(self):
      self.driver.close()

if __name__ == '__main__':
    unittest.main()