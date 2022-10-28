import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customerlogger import LogGen
from PageObjects.edit_employee import EditEmployee


class TestEditEmployee:

    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # pim
    firstname = ReadConfig.getFirstName()
    middlename = ReadConfig.getMiddleName()
    lastname = ReadConfig.getLastName()
    image = "C:\\UmaRaniDundigalla\\UmaRani_workspace\\GUVI\\Guvi_Projects\\GUVI_Project2\\TestData\\user_image.png"
    nickname = ReadConfig.getNickName()

    logger = LogGen.loggen()

    def test_addemployee(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        editemp = EditEmployee(self.driver)
        self.logger.info("*******TC_PIM_02********")
        editemp.edit()
        self.driver.implicitly_wait(10)
        editemp.editemployee(self.middlename)
        self.driver.implicitly_wait(10)
        editemp.save()
        self.updtmsg = editemp.updtconfirmationmsg()
        self.driver.implicitly_wait(5)
        if self.updtmsg == True:
            self.logger.info("********Employee Personal Details are edited Successfully********")
            assert True
        else:
            self.logger.info("********Employee personal details edit Unsuccessful*********")
            assert False
        self.logger.info("*************Completed TC_PIM_02**********")
        self.driver.close()

