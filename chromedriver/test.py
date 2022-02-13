import unittest
from selenium import webdriver


class FormAuthentication(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://the-internet.herokuapp.com/login')
        self.assertIn('Form Authentication', self.browser.find_element_by_id('username'))


if __name__ == '__main__':
    unittest.main()
