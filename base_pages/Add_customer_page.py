from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Add_Customer_Page:
    link_customers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_addnew_xpath="//a[@class='btn btn-primary']"
    textbox_email_id="Email"
    textbox_password_id="Password"
    textbox_firstname_id="FirstName"
    textbox_lastname_id="LastName"
    radiobutton_male_id="Gender_Male"
    radiobutton_female_id="Gender_Female"
    textbox_companyname_id="Company"
    checkbox_is_tax_exempt_id="IsTaxExempt"
    
    custrole_administrators_xpath="//select[@id='SelectedCustomerRoleIds']/option[contains(text(),'Administrators')"
    custrole_forummoderators_xpath="//select[@id='SelectedCustomerRoleIds']/option[contains(text(),'Forum Moderators')]"
    custrole_guests_xpath="//select[@id='SelectedCustomerRoleIds']/option[contains(text(),'Guests')]"
    custrole_registered_xpath="//select[@id='SelectedCustomerRoleIds']/option[contains(text(),'Registered')]"
    custrole_vendors_xpath="//select[@id='SelectedCustomerRoleIds']/option[contains(text(),'Vendors')]"
    
    dropdown_managerofvendor_id="VendorId"
    active_checkbox_id="Active"
    must_change_password_checkbox_id="MustChangePassword"
    admin_comments_xpath="//textarea[@id='AdminComment']"
    save_button_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def click_customers_menu(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()

    def click_customers_menuitem(self):
        self.driver.find_element(By.XPATH,self.link_customers_menuitem_xpath).click()
    
    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.button_addnew_xpath).click()
    
    def enter_email(self,email):
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)
    
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    
    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID,self.textbox_firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID,self.textbox_lastname_id).send_keys(lastname)
    
    def select_gender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.radiobutton_male_id).click()
        elif gender==' Female':
            self.driver.find_element(By.ID,self.radiobutton_female_id).click()
        else:
            self.driver.find_element(By.ID,self.radiobutton_male_id).click()

    def enter_companyname(self,companyname):
        self.driver.find_element(By.ID,self.textbox_companyname_id).send_keys(companyname)
    
    def click_is_tax_exempt(self):
        self.driver.find_element(By.ID,self.checkbox_is_tax_exempt_id).click()
    
    def select_customer_roles(self,role):       
        if role=='Administrators':
            self.driver.find_element(By.XPATH,self.custrole_administrators_xpath).click()
        elif role=='Forum Moderators':
            self.driver.find_element(By.XPATH,self.custrole_forummoderators_xpath).click()
        elif role=='Guests':
            self.driver.find_element(By.XPATH,self.custrole_guests_xpath).click()
        elif role=='Registered':
            self.driver.find_element(By.XPATH,self.custrole_registered_xpath).click()
        elif role=='Vendors':
            self.driver.find_element(By.XPATH,self.custrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.custrole_guests_xpath).click()

    def select_managerofvendor(self,value):        
        drp=Select(self.driver.find_element(By.ID,self.dropdown_managerofvendor_id))
        drp.select_by_visible_text(value)
        
    def click_active_checkbox(self):
        self.driver.find_element(By.ID,self.active_checkbox_id).click()
    
    def click_must_change_password_checkbox(self):
        self.driver.find_element(By.ID,self.must_change_password_checkbox_id).click()

    def enter_admin_comments(self,comments):
        self.driver.find_element(By.XPATH,self.admin_comments_xpath).send_keys(comments)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

    
