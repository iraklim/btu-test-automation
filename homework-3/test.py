import requests
import unittest
import json
from jsonpath_ng.ext import parse as json_parse


class SampleApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_url = "https://bookstore.toolsqa.com/BookStore/v1/Books"
        cls.response = requests.get(cls.api_url)
        cls.books_data_json = json.loads(cls.response.text)

        cls.test_1_expected_result = 200
        cls.test_2_expected_result = "9781593277574"
        cls.test_3_expected_result = [234, 254]

        cls.test_result_text = "TEST {} - ACTUAL: {} | EXPECTED: {} | STATUS: {}"
        

    def test_1(self):
        print(self.test_result_text.format(1, self.response.status_code, self.test_1_expected_result,
            'success' if self.response.status_code == self.test_1_expected_result else 'fail'))
        self.assertEqual(self.response.status_code, self.test_1_expected_result)

    def test_2(self):
        parse_last_book_isbn = json_parse("$.books[-1:].isbn")
        last_book_isbn = [match.value for match in parse_last_book_isbn.find(self.books_data_json)]
        print(self.test_result_text.format(2, last_book_isbn[0], self.test_2_expected_result,
            'success' if last_book_isbn[0] == self.test_2_expected_result else 'fail'))
        self.assertEqual(last_book_isbn[0], self.test_2_expected_result)
    
    def test_3(self):
        parse_pages_count = json_parse("$.books[:].pages")
        pages_count = [match.value for match in parse_pages_count.find(self.books_data_json)]
        print(self.test_result_text.format(3, pages_count[:2], self.test_3_expected_result,
            'success' if pages_count[:2] == self.test_3_expected_result else 'fail'))
        self.assertEqual(pages_count[:2], self.test_3_expected_result)



if __name__ == "__main__":
    unittest.main(verbosity=0)
