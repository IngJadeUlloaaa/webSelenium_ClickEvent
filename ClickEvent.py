import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')
    def test_using_clickEvent(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')
        try:
            container = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/input[1]')
                )
            )

            buttom1 = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/input[1]')
            buttom1.click()
            time.sleep(3)

            buttom2 = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/input[2]')
            buttom2.click()
            time.sleep(2)
        except:
            print("Error: Cannot Found")
            driver.quit()
    def tearDown(self):
        self.driver.close()
if __name__=='__main__':
    unittest.main()