import unittest
import time
from selenium import webdriver

from Page_Objects.login_page import LoginPage
from TestData.testdata import TestData


class Login_Success_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/opt/WebDriver/bin/chromedriver')
        cls.driver.maximize_window()

    def test_login_success(self):
        driver = self.driver

        driver.get('https://markstest.printercloud.com/admin/index.php')

        # create an instance of the login page
        login_page = LoginPage(driver)
        # enter username
        login_page.enter_username(TestData.Username)
        # enter password
        login_page.enter_password(TestData.Password)
        # click the login button
        login_page.click_login()
        # wait for the mainpane to add the tabset page as a child aka logged in
        login_page.check_main_page_added_tabset()
        # check that the top right corner is displaying the username
        self.assertIn(TestData.Username, login_page.check_user_menu())

    @ classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
