import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    def tearDown(self):
        time.sleep(1)

    def test_1(self):
        self.driver.get("https://demoqa.com/progress-bar")
        try:
            button = self.driver.find_element(By.XPATH, '//*[@id="startStopButton"]')
            button.click()
            progress_bar = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="progressBar"]/div[@aria-valuenow="100"]')
                    )
                )
            progress_bar_value = progress_bar.get_attribute("aria-valuenow")
        except:
            print("Something went wrong / Progress bar not found")
            self.assertTrue(False)
        else:
            print(f"Test 1 was completed seccessfully: Progress bar current value is {progress_bar_value}%")
            self.assertEqual(progress_bar_value, "100")

    def test_2(self):
        self.driver.get("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        try:
            dropdown_element = Select(self.driver.find_element(By.XPATH, '//*[@id="dropdowm-menu-1"]'))
            dropdown_element.select_by_visible_text('Python')
        except:
            print("(Python) dropdown_element not found")
            self.assertTrue(False)
        else:
            print("Test 2 was completed seccessfully: Python is selected from the dropdown")
            self.assertTrue(True)
        
    def test_3(self):
        try:
            selection_option_1 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/label[1]/input').click()
            selection_option_2 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/label[2]/input').click()
            selection_option_4 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/label[4]/input').click()
        except:
            print("Selection option(s) not found")
            self.assertTrue(False)
        else:
            print("Test 3 was completed seccessfully: Three new options is selected")
            self.assertTrue(True)

    def test_4(self):
        try:
            radio_button_purple = self.driver.find_element(By.XPATH, '//*[@id="radio-buttons"]/input[@value="purple"]')
            radio_button_purple.click()
        except:
            print("Purple radio button not found")
            self.assertTrue(False)
        else:
            print("Test 4 was completed seccessfully: Purple radio butten is activated")
            self.assertTrue(True)

    def test_5(self):
        try:
            dropdown_orange_disabled = self.driver.find_element(By.XPATH, '//*[@id="fruit-selects"]/option[@value="orange" and @disabled="disabled"]')
        except:
            print("Orange disabled dropdown not found")
            self.assertTrue(False)
        else:
            print("Test 5 was completed seccessfully: Orange dropdown is disabled")
            self.assertTrue(True)



if __name__ == "__main__":
    unittest.main(verbosity=0)