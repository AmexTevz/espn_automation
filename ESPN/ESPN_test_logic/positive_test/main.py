import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from ESPN.tools import selectors
from ESPN.tools import webDrivers

# gets driver functionality from tools/webDriver
driver = webDrivers.chromedriver()

# navigate to the ESPN_test_logic - Runs from selector.py - main_link
driver.get(selectors.main_link)
driver.maximize_window()

# check website title - Runs from selectors.py - assert_element_text method
try:
    selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
    print('The header is correct')
except WDE:
    print('The header is incorrect')


# signup for the ESPN_test_logic - Runs from selectors.py - signup method
selectors.signup(driver)

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
    assert selectors.first_name in welcome_text
    print(f'text detected - Welcome {selectors.first_name}')
except WDE:
    print('can not find the name ')

# Add teams to favorites - Runs from selectors.py favorite_team method
selectors.favorite_team(driver)
time.sleep(1)

# Log out from the account
selectors.log_out(driver)
time.sleep(1)
print('Successfully signed out')

# Log back in
selectors.log_in(driver)
time.sleep(1)
print('Successfully signed back in')

# Delete the account - Runs from selectors.py - delete_profile method
selectors.delete_profile(driver)
time.sleep(1)
print('The account has been deleted')

# Try to sign in into deleted account - check if account is still active or not
try:
    assert "There's a problem" in selectors.log_in_no_account(driver)
    print("Account is disabled")
except WDE:
    print("The account is still active")


