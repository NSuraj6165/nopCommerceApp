import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************ Searching By Email *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Successful *************")

        self.logger.info("************ Started Searching By Email *************")

        self.lp.clickCustomer()
        self.logger.info("************ Clicked On Customers *************")
        self.lp.clickCustomerAgain()
        self.logger.info("************ Clicked On Customers Menu *************")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")

        assert True == status
        self.logger.info("************ Searching By Email Successful *************")