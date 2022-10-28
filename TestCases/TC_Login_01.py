import pytest
from PageObjects.login_page import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customerlogger import LogGen


class TestValidLogin:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*********Launching OrangeHRM website*********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("***********TC_Login_01**********")
        self.logger.info("********Verifying the Valid Login Functionality*****")
        lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        lp.clear_textfields()
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()

        act_url = self.driver.current_url
        if act_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
            self.logger.info("*******Login is Successful*******")
            assert True
        else:
            self.driver.save_screenshot("C://UmaRaniDundigalla//UmaRani_workspace//GUVI//Guvi_Projects//GUVI_Project2//Screenshots//" + "TC_Login_01Failed.png")
            self.logger.info("*********LoginFailed*******")
            assert False
        self.logger.info("************** Completed TC_Login_01 *********************")
        self.driver.close()