
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://the-internet.herokuapp.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        time.sleep(2)

    def test_1(self):
        """
        ლექციაზე განხილული მაგალითი გადაწერილი პითონზე
        https://github.com/Alinatkabladze/BTU_Project/blob/master/src/test/java/ExampleTests.java
        """

        button = self.driver.find_element(By.XPATH, '//ul/li/a')
        button.click()
        text = self.driver.find_element(By.XPATH, '//*[@id=\"content\"]/div/h3')
        self.assertEqual(text.text, "No Test")


    def test_2(self):
        """
        დავალების პასუხი
        - Navigate back to the main page
        - Click on DropDown
        - Select 'Option 1'
        """

        self.driver.back()
        dropdown_page_url = self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a')
        dropdown_page_url.click()
        dropdown_element = Select(self.driver.find_element(By.XPATH, '//*[@id="dropdown"]'))
        dropdown_element.select_by_visible_text('Option 1')
        self.assertTrue(True)
        


if __name__ == "__main__":
    unittest.main()
