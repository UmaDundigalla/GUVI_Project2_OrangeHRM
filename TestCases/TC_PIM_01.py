import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customerlogger import LogGen
from PageObjects.add_employee import AddNewEmployee


def random_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class TestAddEmployee:

    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

# pim
    firstname = ReadConfig.getFirstName()
    middlename = ReadConfig.getMiddleName()
    lastname = ReadConfig.getLastName()
    image = "C:\\UmaRaniDundigalla\\UmaRani_workspace\\GUVI\\Guvi_Projects\\GUVI_Project2\\TestData\\user_image.png"
    employee_id = random_generator()

# pim personal details
    nickname = "dundigalla"
    otherid = "888"
    licenseno1 = "789"
    expirydate = "2024-04-30"
    ssn = "456-789-456"
    sin = "909012456"
    dob = "1988-04-30"
    militaryservice = "no"

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
        emp = AddNewEmployee(self.driver)
        self.logger.info("*******TC_PIM_01********")
        emp.addemployee(self.firstname, self.middlename, self.lastname, self.image, employee_id=random_generator())
        self.logger.info("*******Employee added*******")
        emp.personal_details(self.nickname, self.otherid, self.licenseno1, self.expirydate,
                             self.ssn, self.sin, self.dob, self.militaryservice)
        self.logger.info("********Employee Personal Details are added********")
        self.driver.execute_script("window.scrollBy(0, -2000)", "")
        self.driver.implicitly_wait(10)
        self.savemsg = emp.saveconfirmationmsg()
        self.driver.implicitly_wait(10)
        if self.savemsg == True:
            self.logger.info("***************** Successfully Added New Employee ****************************")
            assert True
        else:
            self.logger.info("***************** Adding New Employee is Unsuccessful  ****************************")
            assert False
        self.logger.info("************** Completed TC_PIM_01 *********************")
        #self.driver.close()





