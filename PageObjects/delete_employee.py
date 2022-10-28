import random
import string
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base.base_driver import BaseDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteEmployee:

    # pim
    delete_xpath = "(//*[@class='oxd-icon bi-trash'])[6]"
    delete_confirm_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"
    txt_delconfmsg_xpath = "//*[text()='Successfully Deleted']"

    def __init__(self, driver):
        self.driver = driver

    def deleteemployee(self):
        self.driver.find_element(By.XPATH,self.delete_xpath).click()
        self.driver.find_element(By.XPATH,self.delete_confirm_xpath).click()

    def delconfirmationmsg(self):
        del_confmsg = self.driver.find_element(By.XPATH,self.txt_delconfmsg_xpath).is_displayed()
        return del_confmsg
