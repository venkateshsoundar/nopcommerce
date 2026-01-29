from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

# -------------------------
# Driver Setup (Headless optional)
# -------------------------
options = Options()
# options.add_argument("--headless=new")   # Uncomment for headless
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Explicit wait object
wait = WebDriverWait(driver, 10)

try:
    # -------------------------
    # Open URL
    # -------------------------
    driver.get("https://admin-demo.nopcommerce.com/")

    # -------------------------
    # Wait for Email field & enter value
    # -------------------------
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "Email"))
    )
    email.clear()
    email.send_keys("admin@yourstore.com")

    # -------------------------
    # Wait for Password field & enter value
    # -------------------------
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "Password"))
    )
    password.clear()
    password.send_keys("admin")

    # -------------------------
    # Wait for Login button & click
    # -------------------------
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    # -------------------------
    # Wait for Dashboard title
    # -------------------------
    wait.until(EC.title_contains("Dashboard"))
    print("✅ Login successful, Dashboard loaded")

except TimeoutException as t:
    print(t)
    print("❌ Timeout: Element not found within time")

except Exception as e:
    print("❌ Unexpected error:", e)

finally:
    time.sleep(2)
    driver.quit()
