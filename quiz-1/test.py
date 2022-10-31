# Quiz 1 - დასრულებული

# ვიზუალურად უფრო აღქმადი რომ იყოს, გამოყენებულია timesleep -ები:
# დასაწყისში - 4 წამი
# ტესტებს შორის - 2 წამი,
# ალერტი როცა ამოდის ტექსტით "Book already present in the your collection!" - 2 წამი,
# ბოლოს - 4 წამი


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException


class SampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/login")

        cls.wait = WebDriverWait(cls.driver, 30)
        cls.options = Options()
        cls.options.add_argument("--disable-notifications")

        cls.test_1_username = "test123"
        cls.test_1_password = "Automation@123"
        cls.test_1_expected_result = "Log out"
        cls.test_2_expected_result = 8
        cls.test_3_expected_result = "Git Pocket Guide"
        cls.test_4_expected_result = "Book already present in the your collection!"
        cls.test_5_expected_result = 8
        cls.test_6_expected_result = ["Welcome,", "Login in Book Store"]

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    def tearDown(self):
        time.sleep(2)

    def test_1(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(self.test_1_username)
            self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.test_1_password)
            self.driver.find_element(By.XPATH, '//*[@id="login"]').click()
            
            log_out_el = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="submit"]')))
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 1 - ACTUAL: {log_out_el.text} | EXPECTED: {self.test_1_expected_result} | STATUS: {'success' if log_out_el.text == self.test_1_expected_result else 'fail'}")
            self.assertEqual(log_out_el.text, self.test_1_expected_result)

    def test_2(self):
        try:
            try:
                book_store_el = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]/span')))
                book_store_el.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click()", book_store_el)
            books_el = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            count_of_books = len(books_el.find_elements(By.XPATH, './/img'))
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 2 - ACTUAL: {count_of_books} | EXPECTED: {self.test_2_expected_result} | STATUS: {'success' if count_of_books == self.test_2_expected_result else 'fail'}")
            self.assertEqual(count_of_books, self.test_2_expected_result)

    def test_3(self):
        try:
            git_book_el = self.driver.find_element(By.XPATH, '//*[@id="see-book-Git Pocket Guide"]')
            git_book_el.click()

            title_el = self.driver.find_element(By.XPATH, '//*[@id="title-wrapper"]')
            title_label_els = [title_label_el.text for title_label_el in title_el.find_elements(By.XPATH, './/label')]
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 3 - ACTUAL: {title_label_els[1]} | EXPECTED: {self.test_3_expected_result} | STATUS: {'success' if  title_label_els[1] == self.test_3_expected_result else 'fail'}")
            self.assertTrue(self.test_3_expected_result in title_label_els)

    def test_4(self):
        try:
            try:
                add_collection_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[2]/button')))
                add_collection_btn.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click()", add_collection_btn)
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            time.sleep(2)
            alert.accept()
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 4 - ACTUAL: {alert_text} | EXPECTED: {self.test_4_expected_result} | STATUS: {'success' if alert_text == self.test_4_expected_result else 'fail'}")
            self.assertEqual(alert_text, self.test_4_expected_result)

    def test_5(self): 
        try:
            try:
                back_to_book_store_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[1]/button')))
                back_to_book_store_btn.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click()", back_to_book_store_btn)
            books_el = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            count_of_books = len(books_el.find_elements(By.XPATH, './/img'))
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 5 - ACTUAL: {count_of_books} | EXPECTED: {self.test_5_expected_result} | STATUS: {'success' if count_of_books == self.test_5_expected_result else 'fail'}")
            self.assertEqual(count_of_books, self.test_5_expected_result)
            
    def test_6(self):
        try:
            log_out_el = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="submit"][.="Log out"]')))
            log_out_el.click()

            welcome_text_div = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]')
            welcome_text_1 = welcome_text_div.find_element(By.XPATH, f'.//*[contains(text(), "{self.test_6_expected_result[0]}")]')
            welcome_text_2 = welcome_text_div.find_element(By.XPATH, f'.//*[contains(text(), "{self.test_6_expected_result[1]}")]')
        except:
            self.assertTrue(False)
        else:
            print(f"TEST 6 - ACTUAL: {welcome_text_1.text + ' ' + welcome_text_2.text} | EXPECTED: {' '.join(self.test_6_expected_result)} | STATUS: {'success' if welcome_text_1 and welcome_text_1 else 'fail'}")
            self.assertTrue(welcome_text_1 and welcome_text_2)



if __name__ == "__main__":
    unittest.main(verbosity=0)