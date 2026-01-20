from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Search_Customers_Page:
    textbox_email_id="SearchEmail"
    textbox_firstname_id="SearchFirstName"
    textbox_lastname_id="SearchLastName"
    btn_search_id="search-customers"
    text_companyname="SearchCompany"
    rows_table_xpath="//table[@id='customers-grid']//tbody/tr"
    columns_table_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)
    
    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID,self.textbox_firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID,self.textbox_lastname_id).send_keys(lastname)

    def enter_companyname(self,companyname):
        self.driver.find_element(By.ID,self.text_companyname).send_keys(companyname)

    def click_search(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()    
    
    def get_no_of_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.rows_table_xpath))
    
    def get_no_of_columns(self):
        return len(self.driver.find_elements(By.XPATH,self.columns_table_xpath))
    
    def search_customer_by_email(self,email):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table_email=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if table_email==email:
                flag=True
                break
        return flag
    
    def search_customer_by_name(self,Name):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table_name=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if table_name==Name:
                flag=True
                break
        return flag
    
    def search_customer_by_companyname(self,companyname):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table_companyname=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[5]").text
            if table_companyname==companyname:
                flag=True
                break
        return flag