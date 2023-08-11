from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//button[@class='button-1 login-button']")
    link_logout_linktext = (By.LINK_TEXT, "Logout")
    customer_link = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    customer_again = (By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Customers')]")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(*LoginPage.textbox_username_id).clear()
        self.driver.find_element(*LoginPage.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.textbox_password_id).clear()
        self.driver.find_element(*LoginPage.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*LoginPage.link_logout_linktext).click()

    def clickCustomer(self):
        self.driver.find_element(*LoginPage.customer_link).click()

    def clickCustomerAgain(self):
        self.driver.find_element(*LoginPage.customer_again).click()