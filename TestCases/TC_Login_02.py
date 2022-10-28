import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customerlogger import LogGen


class TestInValidLogin:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    password_invalid = ReadConfig.getInvalidPassword()

    logger = LogGen.loggen()

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*********Launching OrangeHRM website*********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("***********TC_Login_02**********")
        self.logger.info("********Verifying the InValid Login Functionality*****")
        lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        lp.clear_textfields()
        lp.set_username(self.username)
        lp.set_password(self.password_invalid)
        lp.click_login()
        errmsg = lp.get_message_invalid_login()
        self.driver.implicitly_wait(10)
        if errmsg == "Invalid credentials":
            self.logger.info("*******Invalid login test is Successful*******")
            assert True
        else:
            self.logger.info("*********Invalid Login is Unsuccessful*******")
            assert False

        self.logger.info("************** Completed TC_Login_02 *********************")
        self.driver.close()







