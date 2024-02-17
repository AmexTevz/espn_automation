import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from ESPN.tools import selectors, webDrivers
import random
from faker import Faker


fake = Faker()

# gets driver functionality from tools/webDriver
driver = webDrivers.chromedriver()

# navigate to the ESPN website - Runs from selector.py - main_link
driver.get(selectors.main_link)

# Fake first name from the faker library
first_name = fake.first_name()

# Fake last name from the faker library
last_name = fake.last_name()

# Fake email - a combination of first and last name with random numbers
email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"

# check website title - Runs from selectors.py - assert_element_text method
try:
    selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
    print('The header is correct')
except WDE:
    print('The header is incorrect')

# signup for the ESPN_test_logic - Runs from selectors.py - signup method
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

# Add teams to favorites - Runs from selectors.py favorite_team method
selectors.favorite_team(driver)
time.sleep(1)

# Log out from the account
selectors.log_out(driver)
time.sleep(1)

# Log back in
selectors.log_in(driver, email)
time.sleep(1)

# Delete the account - Runs from selectors.py - delete_profile method
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

