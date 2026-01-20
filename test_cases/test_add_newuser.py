import random
import string
import time
import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_customer_page import Add_Customer_Page
from selenium.webdriver.common.by import By

from utilities.customer_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test03_Add_New_Customer:
    admin_page_url=Read_Config.get_admin_page_url()
    logger=Log_Maker.log_generator()
    username=Read_Config.get_username()
    password=Read_Config.get_password()

    @staticmethod
    def generate_random_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain=random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        return f"{username}@{domain}"

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self,setup):
        self.logger.info("**********Test_Add_New_Customer: test_add_new_customer started**********")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.get(self.admin_page_url)
        self.logger.info("**********Opening Admin Page URL**********")
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        self.logger.info("**********Admin Logged in Successfully**********")
        self.add_cust_page=Add_Customer_Page(self.driver)
        self.add_cust_page.click_customers_menu()
        self.add_cust_page.click_customers_menuitem()
        self.add_cust_page.click_addnew()
        self.logger.info("**********Adding New Customer Details**********")
        self.email=self.generate_random_email()
        self.add_cust_page.enter_email(self.email)
        self.add_cust_page.enter_password("test123")
        self.add_cust_page.enter_firstname("Venkatesh")
        self.add_cust_page.enter_lastname("Balu")
        self.add_cust_page.select_gender("Male")
        self.add_cust_page.enter_companyname("ABC Pvt Ltd") 
        self.add_cust_page.click_is_tax_exempt()
        self.add_cust_page.select_customer_roles("Guests")
        self.add_cust_page.select_customer_roles("Registered")
        self.add_cust_page.select_managerofvendor("Vendor 2")
        self.add_cust_page.click_active_checkbox()
        self.add_cust_page.click_must_change_password_checkbox()
        self.add_cust_page.enter_admin_comments("This is for testing add new customer functionality.")
        self.add_cust_page.click_save()
        time.sleep(5)
        self.logger.info("**********Saving New Customer Details**********")
        self.msg=self.driver.find_element(By.XPATH,"//div[@id='admin-notifications']//span").text
        customer_added_msg="The new customer has been added successfully."
        if self.msg==customer_added_msg:
            self.logger.info("**********Test_Add_New_Customer: test_add_new_customer Passed**********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_add_new_customer.png")
            self.logger.error("**********Test_Add_New_Customer: test_add_new_customer Failed**********")
            assert False        
        self.driver.close()
        self.logger.info("**********Test_Add_New_Customer: test_add_new_customer ended**********")


