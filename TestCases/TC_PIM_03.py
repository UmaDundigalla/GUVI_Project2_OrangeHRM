import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from PageObjects.delete_employee import DeleteEmployee
from Utilities.readProperties import ReadConfig
from Utilities.customerlogger import LogGen
from PageObjects.edit_employee import EditEmployee


class TestEditEmployee:

    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_deleteemployee(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        deleteemp = DeleteEmployee(self.driver)
        self.logger.info("*******TC_PIM_03********")
        deleteemp.deleteemployee()
        self.driver.implicitly_wait(10)
        self.delmsg = deleteemp.delconfirmationmsg()
        self.driver.implicitly_wait(10)
        if self.delmsg == True:
            self.logger.info("********Employee is deleted Successfully********")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** Delete Employee is Unsuccessful******")
            assert False
        self.logger.info("**********Completed TC_PIM_03***********")