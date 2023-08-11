from selenium.webdriver.common.by import By

class SearchCustomer:

    txtEmail_id = (By.ID, "SearchEmail")
    btnSearch_id = (By.ID, "search-customers")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(*SearchCustomer.txtEmail_id).clear()
        self.driver.find_element(*SearchCustomer.txtEmail_id).send_keys(email)

    def ClickSearch(self):
        self.driver.find_element(*SearchCustomer.btnSearch_id).click()

    def searchCustomerByEmail(self, email):
        flag = False
        emailid = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr/td[2]").text
        if emailid == email:
            flag = True
        return flag

