import random
import string
import time
import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_customer_page import Add_Customer_Page
from selenium.webdriver.common.by import By

from base_pages.Search_Customers_Page import Search_Customers_Page
from utilities.customer_logger import Log_Maker
from utilities.read_properties import Read_Config

class Test04_Search_Customers:
    admin_page_url=Read_Config.get_admin_page_url()
    logger=Log_Maker.log_generator()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_email(self,setup):
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_email started**********")
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
        self.search_cust_page=Search_Customers_Page(self.driver)
        self.logger.info("**********Searching Customer by Email ID**********")
        self.search_cust_page.enter_email("arthur_holmes@nopCommerce.com")
        self.search_cust_page.click_search()
        time.sleep(5)
        status=self.search_cust_page.search_customer_by_email("arthur_holmes@nopCommerce.com")
        assert True==status
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_email Passed**********")
        self.admin_lp.click_logout()
        self.driver.quit()

    @pytest.mark.regression
    def test_search_customer_by_firstname(self,setup):
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_firstname started**********")
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
        self.search_cust_page=Search_Customers_Page(self.driver)
        self.logger.info("**********Searching Customer by First Name**********")
        self.search_cust_page.enter_firstname("Arthur")
        self.search_cust_page.click_search()
        time.sleep(5)
        status=self.search_cust_page.search_customer_by_name("Arthur Holmes")
        assert True==status
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_firstname Passed**********")
        self.admin_lp.click_logout()
        self.driver.quit()

    @pytest.mark.regression
    def test_search_customer_by_lastname(self,setup):
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_lastname started**********")
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
        self.search_cust_page=Search_Customers_Page(self.driver)
        self.logger.info("**********Searching Customer by Last Name**********")
        self.search_cust_page.enter_lastname("Holmes")
        self.search_cust_page.click_search()
        time.sleep(5)
        status=self.search_cust_page.search_customer_by_name("Arthur Holmes")
        assert True==status
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_lastname Passed**********")
        self.admin_lp.click_logout()
        self.driver.quit()

    @pytest.mark.regression
    def test_search_customer_by_companyname(self,setup):
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_companyname started**********")
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
        self.search_cust_page=Search_Customers_Page(self.driver)
        self.logger.info("**********Searching Customer by Company Name**********")
        self.search_cust_page.enter_companyname("ABC Pvt Ltd")
        self.search_cust_page.click_search()
        time.sleep(5)
        status=self.search_cust_page.search_customer_by_companyname("ABC Pvt Ltd")
        assert True==status
        self.logger.info("**********Test_Search_Customers: test_search_customer_by_companyname Passed**********")
        self.admin_lp.click_logout()
        self.driver.quit()
        