import pytest

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestLogin001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info(
            "******************************** test_homePageTitle Started *************************************")
        self.logger.info("************************** Verifying Home Page Title **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info(
                "******************************** test_homePageTitle Passed *************************************")
        else:
            self.driver.save_screenshot(
                r"C:\Users\hunshab\PycharmProjects\pythonSeleniumProject2\Screenshots\test_homePageTitle.png")
            self.driver.close()
            self.logger.error(
                "******************************** test_homePageTitle Failed *************************************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info(
                "******************************** test_homePageTitle Passed *************************************")
        else:
            self.driver.save_screenshot(
                r"C:\Users\hunshab\PycharmProjects\pythonSeleniumProject2\Screenshots\test_login.png")
            self.driver.close()
            self.logger.error(
                "******************************** test_homePageTitle Failed *************************************")
            assert False
