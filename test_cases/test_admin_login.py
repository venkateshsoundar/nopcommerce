import pytest
import time
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.customer_logger import Log_Maker


class Test01_admin_login:

    admin_page_url=Read_Config.get_admin_page_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    invalid_username=Read_Config.get_invalid_username()
    invalid_password=Read_Config.get_invalid_password()
    logger=Log_Maker.log_generator()

    @pytest.mark.regression
    def test_title_verification(self,setup: webdriver):
        self.logger.info("**********Test01_admin_login: test_title_verification started**********")
        self.logger.info("**********Navigating to admin page URL**********")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        act_title=self.driver.title
        expected_title="nopCommerce demo store. Login"
        self.logger.info("**********Verifying the title of the page**********")
        if act_title==expected_title:
            self.logger.info("**********Test Title Verification Passed**********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_title_verification.png")
            self.driver.close()
            assert False
    
    @pytest.mark.regression
    @pytest.mark.sanity       
    def test_validadmin_login(self,setup: webdriver):
        self.logger.info("**********Test02_admin_login: test_validadmin_login started**********")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5) 
        act_title=self.driver.title
        expected_title="Dashboard / nopCommerce administration"
        self.logger.info("**********Verifying the title of the page**********")
        if act_title==expected_title:
            self.logger.info("**********Test Title Verification Passed**********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_validadmin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalidadmin_login(self,setup: webdriver):
        self.logger.info("**********Test03_admin_login: test_invalidadmin_login started**********")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.invalid_password)
        self.admin_lp.click_login()
        time.sleep(5) 
        act_message=self.driver.find_element(By.XPATH,"//li").text
        expected_message="No customer account found"
        if act_message==expected_message:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_invalidadmin_login.png")
            self.driver.close()
            assert False
