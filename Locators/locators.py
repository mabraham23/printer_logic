from selenium.webdriver.common.by import By


class Locators():

    # Login Page Locators
    USERNAME_FORM = "relogin_user"
    PASSWORD_FORM = "relogin_password"
    LOGIN_BUTTON = "admin-login-btn"
    MAIN_PAGE_TABSET_PAGE = "#mainpane #tabsetpage"
    LOGIN_TEXT = "logintext"
    USER_MENU = "user-menu"
    TABSET_PAGE = (By.ID, "tabsetpage")

    # home page locators
    ALERTS_TAB = (By.ID, "oAlerts")
