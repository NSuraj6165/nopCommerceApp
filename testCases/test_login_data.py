import pytest
from TestData.LoginData import LoginData
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_Data(self, setup, getData):
        useremail = getData["Username"]
        password = getData["Password"]
        self.logger.info("************ Verifying LoginData Test *************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(useremail)
        self.lp.setPassword(password)

        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************ Login Test is Passed *************")
            self.lp.clickLogout()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************ Login Test is failed *************")
            assert ("Dashboard" not in act_title)
        self.driver.close()

    @pytest.fixture(params=LoginData.login_data)
    def getData(self, request):
        return request.param
