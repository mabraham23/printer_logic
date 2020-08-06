import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from TestData.testdata import TestData
from Page_Objects.login_page import LoginPage


class Login_Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/opt/WebDriver/bin/chromedriver')
        self.driver.maximize_window()

    # test login screen by clicking submit without adding the username
    def test_login_no_username(self):
        driver = self.driver

        driver.get('https://markstest.printercloud.com/admin/index.php')

        login_page = LoginPage(driver)
        # enter password
        login_page.enter_password(TestData.Password)
        # cick login button
        login_page.click_login()
        # check the top right corner to see if username has been added
        self.assertNotIn(TestData.Username, login_page.check_user_menu())
        # check that the error message displayed
        self.assertEqual(login_page.check_for_login_text(),
                         "Please enter your username and password:")

    # test login screen by clicking submit without adding password
    def test_login_no_password(self):
        driver = self.driver

        driver.get('https://markstest.printercloud.com/admin/index.php')

        login_page = LoginPage(driver)
        # enter the username
        login_page.enter_username(TestData.Username)
        # click the login button
        login_page.click_login()
        # make sure that the username isn't in the top right
        self.assertNotIn(TestData.Username, login_page.check_user_menu())
        # make sure the error message displayed
        self.assertEqual(login_page.check_for_login_text(),
                         "Please enter your username and password:")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
