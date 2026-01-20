import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities.customer_logger import Log_Maker
from pytest_metadata.plugin import metadata_key


# Hook for command line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox"
    )


# Fixture to get the browser name
@pytest.fixture()
def browser(request):
    print("\n**********Fetching browser value from command line options**********")
    print(f"Browser value is: {request.config.getoption('--browser')}")
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        print("Launching Edge browser")
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Browser not supported")

    return driver


## pytest hooks to add environment info to HTML report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nopCommerce'
    config.stash[metadata_key]['Module Name'] = 'Admin Login'
    config.stash[metadata_key]['Tester'] = 'Venkatesh'

@pytest.hookimpl(optionalhook=True)
# pytest hook to modify/delete environment info to HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
