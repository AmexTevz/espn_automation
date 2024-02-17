from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import string
import time

# Generates the random password with alphanumeric values
fake_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

# Creating the list of teams
teams = 'Napoli, Genoa,Valencia, Manchester United, Newcastle United, Borussia Dortmund, Atalanta'.split(',')
team_list = random.sample(teams, 3)

# Website address
main_link = "https://www.espn.com/"

# Button - menu
side_menu_button = "global-user-trigger"

# Button - sign-up
signup_button = "(//a[contains(.,'Sign Up')])"

# Button - sign-up - for smaller screens
secondary_signup_button = "(//a[contains(.,'Sign Up')])[6]"

# Input field - email
email_input = "InputIdentityFlowValue"

# Input field - password
password_input = "InputPassword"

# Input field - email
first_name_input = "InputFirstName"

# Button - submit
submit_button = "BtnSubmit"

# Button - add favorite teams
add_favorites_button = "(//a[contains(.,'+Add favorites')])"

# Button - add favorite teams - for smaller screens
secondary_add_favorites_button = "(//a[contains(.,'+Add favorites')])[2]"

# Input field - search for teams to add to favorites
team_search_input = "//input[@type='search']"

# Button - follow favorite teams
follow_button = "(//button[@tabindex='0'])[1]"

# Button - edit profile
profile = "(//a[contains(.,'ESPN Profile')])"

# Button - edit profile - for smaller screens
secondary_profile = "(//a[contains(.,'ESPN Profile')])[2]"

# Button - Close the frame
frame_close = "//button[@aria-label='Close dialog']"

# Link - Delete account
delete_account = "AccountDeleteLink"

# Button - Log-in
log_in_button = "(//a[contains(.,'Log In')])[2]"

# Button - Log-in - for smaller screens
secondary_log_in_button = "(//a[contains(.,'Log In')])[3]"

# Message - shows up if email doesn't exist
log_in_error = "InputIdentityFlowValue-error"

# Button - Log-out
log_out_button = "(//a[contains(.,'Log Out')])"

# Button - Log-out - for smaller screens
secondary_log_out_button = "(//a[contains(.,'Log Out')])[2]"


# asserts actual and expected texts
def assert_element_text(element, selector):
    assert selector in element


def screenshot(driver, filename):
    driver.get_screenshot_as_file(f'{filename}.png')


# Opens the right side menu for the account management
def open_side_menu(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.ID, side_menu_button))).click()


def move_to_element(driver, actions):
    driver.move_to_element()


# Sign-up for the ESPN website by switching to iframe, passing fake credentials, and switching back to the main window
def signup(driver,email,first,last):
    wait = WebDriverWait(driver, 10)
    open_side_menu(driver)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, signup_button))).click()
    except WDE:
        wait.until(EC.visibility_of_element_located((By.XPATH, secondary_signup_button))).click()
    driver.switch_to.frame('oneid-iframe')
    wait.until(EC.visibility_of_element_located((By.ID, email_input))).send_keys(
        email + Keys.TAB + Keys.ENTER)
    (wait.until(EC.visibility_of_element_located((By.ID, first_name_input))).
     send_keys(first + Keys.TAB + last, Keys.TAB + fake_password))

    time.sleep(1)
    driver.find_element(By.ID, submit_button).click()
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(5)
    credentials = f'Login: {email}  Password: {fake_password}'
    print(f'Successfully signed up')
    print(f'{credentials:_^100}')


# switches to the iframe, adds teams from the team_list to the favorites and returns to the main page
def favorite_team(driver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, add_favorites_button))).click()
    except:
        wait.until(EC.visibility_of_element_located((By.XPATH, secondary_add_favorites_button))).click()
    driver.switch_to.frame('favorites-manager-iframe')
    team_input = wait.until(EC.visibility_of_element_located((By.XPATH, team_search_input)))
    try:
        for i in team_list:
            team_input.send_keys(i.strip())
            time.sleep(2)
            wait.until(EC.visibility_of_element_located((By.XPATH, follow_button))).click()
            print(f'Added {i} to the favorite teams')
            team_input.clear()
            time.sleep(1)
    except WDE:
        print('Could not retrieve teams - FireFox bug')
    finally:
        driver.find_element(By.XPATH, frame_close).click()
        time.sleep(3)
        driver.switch_to.default_content()


# Sign-in to existing account
def log_in(driver,email):
    wait = WebDriverWait(driver, 10)
    try:
        open_side_menu(driver)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, log_in_button))).click()
        except:
            wait.until(EC.visibility_of_element_located((By.XPATH, secondary_log_in_button))).click()
        driver.switch_to.frame('oneid-iframe')
        (wait.until(EC.visibility_of_element_located((By.ID, email_input))).
         send_keys(email + Keys.TAB + Keys.ENTER))
        (wait.until(EC.visibility_of_element_located((By.ID, password_input))).
         send_keys(fake_password + Keys.TAB + Keys.TAB + Keys.ENTER))
        time.sleep(3)
        driver.switch_to.default_content()
        print('Successfully signed back in')
    except Exception:
        print("Email confirmation dialog popped up during signing in - unable to continue")
        pass


# Sign-out from the account
def log_out(driver):
    wait = WebDriverWait(driver, 5)
    open_side_menu(driver)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, log_out_button))).click()
    except:
        wait.until(EC.visibility_of_element_located((By.XPATH, secondary_log_out_button))).click()
    print('Successfully signed out')


# switches to the iframe and deletes the account
def delete_profile(driver):
    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    try:
        open_side_menu(driver)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, profile))).click()
        except:
            wait.until(EC.visibility_of_element_located((By.XPATH, secondary_profile))).click()
        driver.switch_to.frame('oneid-iframe')
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, delete_account))).click()
        for _ in range(2):
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.ID, submit_button))).click()
        time.sleep(2)
        driver.switch_to.default_content()
        print('The account has been deleted')
    except Exception:
        print("Email confirmation dialog popped up during account deletion - unable to continue")
        pass


# Additional sign-in method to check behavior if the account doesn't exist
def log_in_no_account(driver, email):
    try:
        wait = WebDriverWait(driver, 10)
        open_side_menu(driver)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, log_in_button))).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, secondary_log_in_button))).click()
        driver.switch_to.frame('oneid-iframe')
        (wait.until(EC.visibility_of_element_located((By.ID, email_input))).
         send_keys(email + Keys.TAB + Keys.ENTER))
        error_msg = wait.until(EC.visibility_of_element_located((By.ID, log_in_error))).text
        return error_msg
    except:
        pass
