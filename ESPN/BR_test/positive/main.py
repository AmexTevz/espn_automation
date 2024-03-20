# coding=utf8
from selenium.common.exceptions import WebDriverException as WDE
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from threading import Thread
from ESPN.tools import BR_Key, selectors
from faker import Faker
import random

fake = Faker()
BROWSERSTACK_USERNAME = BR_Key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = BR_Key.BROWSERSTACK_ACCESS_KEY
URL = "https://hub.browserstack.com/wd/hub"
capabilities = [
    {
        "browserName": "Chrome",
        'bstack:options': {
            "os": "OS X",
            "osVersion": "Mojave",
            "browserVersion": "116.0",
            "consoleLogs": "info"
        }
    },
    {
        "browserName": "Safari",
        'bstack:options': {
            "os": "OS X",
            "osVersion": "Ventura",
            "browserVersion": "16.5"
        }
    },
    {
        "browserName": "Edge",
        'bstack:options': {
            "os": "Windows",
            "osVersion": "11",
            "browserVersion": "latest"
        }
    }
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "browserName": cap["browserName"],
        "os": cap["bstack:options"]["os"],
        "osVersion": cap["bstack:options"]["osVersion"],
        "browserVersion": cap["bstack:options"]["browserVersion"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "consoleLogs" in cap:
        bstack_options["consoleLogs"] = cap["consoleLogs"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)

    # navigate to the ESPN website - Runs from selector.py - main_link
    driver.get(selectors.main_link)

    # Fake first name from the faker library
    first_name = fake.first_name()

    # Fake last name from the faker library
    last_name = fake.last_name()

    # Fake email - a combination of first and last name with random numbers
    email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"

    # check website title - Runs from script_selectors.py - assert_element_text method
    try:
        selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
        print('The header is correct')
    except WDE:
        print('The header is incorrect')

    # signup for the ESPN website - Runs from script_selectors.py - signup method
    selectors.signup(driver, email, first_name, last_name)

    # Check ESPN logo is present - top-left
    try:
        assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
        print('Logo is present')
    except WDE:
        print('Logo is not visible')

    selectors.open_side_menu(driver)

    # Check Welcome message with correct name is present
    try:
        welcome_text = driver.find_element(By.CLASS_NAME, "display-user").text
        assert first_name in welcome_text
        print(f'text detected - Welcome {first_name}')
    except AssertionError:
        welcome_text = driver.find_element(By.XPATH, "(//li[@class='display-user'])[2]").text
        assert first_name in welcome_text
        print(f'asserted through secondary locator - Welcome {first_name}')
    except WDE:
        print('The welcome massage not detected')

    # Add teams to favorites - Runs from script_selectors.py favorite_team method
    selectors.favorite_team(driver)
    time.sleep(1)

    # Log out from the account
    selectors.log_out(driver)
    time.sleep(1)

    # Log back in
    selectors.log_in(driver, email)
    time.sleep(1)

    # Delete the account - Runs from script_selectors.py - delete_profile method
    selectors.delete_profile(driver)
    time.sleep(1)

    # Try to sign in into deleted account - check if account is still active or not
    try:
        assert "There's a problem" in selectors.log_in_no_account(driver, email)
        print("Account is disabled")
    except TypeError:
        print('Finishing test - Fail due to confirmation dialog')
    except WDE:
        print("The account is still active")

    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
