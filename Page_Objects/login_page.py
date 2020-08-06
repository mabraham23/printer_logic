from Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage():
    """Login Page"""

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.USERNAME_FORM
        self.password_textbox_id = Locators.PASSWORD_FORM
        self.login_button_id = Locators.LOGIN_BUTTON
        self.login_text = Locators.LOGIN_TEXT
        self.user_menu = Locators.USER_MENU
        self.main_page = Locators.MAIN_PAGE_TABSET_PAGE

    # enter username
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(
            self.username_textbox_id).send_keys(username)

    # enter password
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(
            self.password_textbox_id).send_keys(password)

    # click the login button
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    # see if user logged in correctly by checking to see if the main page added it's child
    def check_main_page_added_tabset(self):
        return (WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element_by_css_selector(Locators.MAIN_PAGE_TABSET_PAGE)))

    # check for error message when clicking submit without correct credentials
    def check_for_login_text(self):
        text = self.driver.find_element_by_id(self.login_text)
        return text.get_attribute('innerHTML')

    # check to see if the username has been added to the top right toolbar after the user logs in
    def check_user_menu(self):
        menu = self.driver.find_element_by_id(self.user_menu)
        return menu.get_attribute('innerHTML')

    # experimental function that I didn't end up using but I saw a demo of online
    def is_visible(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TABSET_PAGE))
        return bool(element)
