import pytest
import time
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.customer_logger import Log_Maker
from utilities import excel_utils


class Test02_admin_login_datadriven:

    admin_page_url=Read_Config.get_admin_page_url()
    logger=Log_Maker.log_generator()
    path=".//test_data//admin_login_data.xlsx"
    status_list=[]

    
            
    def test_validadmin_login_dd(self,setup: webdriver):
        self.logger.info("**********Test_admin_login: test_validadmin_login started**********")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.rows=excel_utils.get_row_count(self.path,"admin_login_data")
        print("Number of rows in excel:",self.rows)
        
        for r in range(2,self.rows+1):
            self.username=excel_utils.read_cell_data(self.path,"admin_login_data",r,1)
            self.password=excel_utils.read_cell_data(self.path,"admin_login_data",r,2)
            self.expected_loginstatus=excel_utils.read_cell_data(self.path,"admin_login_data",r,3)

            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5) 


            if self.expected_loginstatus=='Yes':
                act_title=self.driver.title
                expected_title="Dashboard / nopCommerce administration"
                self.logger.info("**********Verifying the title of the page**********")
                if act_title==expected_title:
                    self.logger.info("**********Test Title Verification Passed**********")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()                  
                else:
                    self.driver.save_screenshot(".\\screenshots\\"+"test_validadmin_login.png")
                    self.status_list.append("Fail") 
            else:
                act_message=self.driver.find_element(By.XPATH,"//li").text
                expected_message="No customer account found"
                if act_message==expected_message:
                    self.status_list.append("Pass")                    
                else:
                    self.driver.save_screenshot(".\\screenshots\\"+"test_invalidadmin_login.png")
                    self.status_list.append("Fail") 
             
        print(self.status_list)
        if "Fail" not in self.status_list:
            self.logger.info("**********Admin Login Data Driven Test Passed**********")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Admin Login Data Driven Test Failed**********")
            self.driver.close()
            assert False
        
        
