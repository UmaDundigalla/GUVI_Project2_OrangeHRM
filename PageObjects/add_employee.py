import random
import string
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base.base_driver import BaseDriver


class AddNewEmployee:

    # pim
    btn_add_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    txt_firstname_name = "firstName"
    txt_middlename_name = "middleName"
    txt_lastname_name = "lastName"
    txt_employee_id_xpath = "//div[@class = 'oxd-grid-2 orangehrm-full-width-grid']" \
                           "//input[@class ='oxd-input oxd-input--active']"
    btn_addimg_xpath = "//input[@type='file']"
    chkbx_logindetail_id = "checkbox"
    # "//input[@type='checkbox']"
    btn_save_xpath = "//form/div[2]//button[@type='submit']"

    # pim personal details
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
    txt_saveconfmsg_xpath = "//*[text()='Successfully Saved']"




    def __init__(self, driver):
        self.driver = driver

    def addemployee(self, firstname, middlename, lastname, image, employee_id):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)
        self.driver.find_element(By.NAME, self.txt_middlename_name).send_keys(middlename)
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.btn_addimg_xpath).send_keys(image)
        self.driver.find_element(By.XPATH, self.txt_employee_id_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_employee_id_xpath).send_keys(employee_id)
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def personal_details(self, nickname, otherid, licenseno, expirydate, ssn, sin, dob, militaryservice):
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).send_keys(nickname)
        self.driver.find_element(By.XPATH, self.txt_other_id_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.txt_license_no_path).send_keys(licenseno)
        self.driver.find_element(By.XPATH, self.txt_expiry_date_xpath).send_keys(expirydate)
        self.driver.find_element(By.XPATH, self.txt_ssn_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH, self.txt_sin_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH, self.txt_date_of_birth).send_keys(dob)
        self.driver.find_element(By.XPATH, self.btn_gender_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_nationality_click).click()
        self.driver.find_element(By.XPATH, self.txt_military_service_xpath).send_keys(militaryservice)
        self.driver.find_element(By.XPATH, self.btn_save1_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_blood_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_blood_group).click()
        self.driver.find_element(By.XPATH, self.btn_save2_xpath).click()

    def saveconfirmationmsg(self):
        save_confmsg = self.driver.find_element(By.XPATH,self.txt_saveconfmsg_xpath).is_displayed()
        return save_confmsg