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

class EditEmployee:

    # pim
    edit_xpath = "(//*[@class='oxd-icon bi-pencil-fill'])[2]"

    # pim personal details
    txt_firstname_name = "firstName"
    txt_middlename_name = "middleName"
    txt_lastname_name = "lastName"

    # pim personal details
    # btn_addimg_xpath = "//input[@type='file']"
    txt_nickname_xpath = "//form[@class='oxd-form']/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_other_id_xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    txt_license_no_path = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    txt_issued_date = "//form/div[2]//div[2]//div[2]//input[@placeholder='yyyy-mm-dd']"
    txt_expiry_date_xpath = "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    txt_ssn_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    txt_sin_xpath = "//div[3]/div[2]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    txt_date_of_birth = "//form/div[3]/div[2]//div/input[@placeholder='yyyy-mm-dd']"
    btn_gender_xpath = "//label[normalize-space()='Female']"
    btn_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    btn_nationality_click = "//*[contains(text(),'Indian')]"
    btn_married_status = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_married_status_click = "//*[contains(text(),'Single')]"
    txt_military_service_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    btn_save1_xpath = "//div[5]/button[@type='submit']"
    btn_blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text oxd-select-text--active']"
    btn_blood_group = "//*[contains(text(),'O+')]"
    btn_save2_xpath = "//form/div[2]/button[@type='submit']"
    txt_updtconfmsg_xpath = "//*[text()='Successfully Updated']"

    def __init__(self, driver):
        self.driver = driver

    def edit(self):
        self.driver.find_element(By.XPATH, self.edit_xpath).click()
        self.driver.find_element(By.NAME, self.txt_middlename_name).clear()
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).clear()


    def editemployee(self, middlename):
        self.driver.find_element(By.NAME, self.txt_middlename_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.NAME, self.txt_middlename_name).send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, self.txt_middlename_name).send_keys(middlename)



    def save(self):
        self.driver.find_element(By.XPATH, self.btn_save1_xpath).click()

    def updtconfirmationmsg(self):
        updt_confmsg = self.driver.find_element(By.XPATH,self.txt_updtconfmsg_xpath).is_displayed()
        return updt_confmsg