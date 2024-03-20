import datetime
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
import random
import string
import HtmlTestRunner
from tools import script_selectors, webDrivers

fake = Faker()


class ChromeESPN(unittest.TestCase):
    def setUp(self):
        self.driver = webDrivers.chromedriver()

    def test_espn_chrome(self):
        driver = self.driver

        # navigate to the ESPN website - Runs from selector.py - main_link
        driver.get(script_selectors.main_link)

        # Fake first name from the faker library
        first_name = fake.first_name()

        # Fake last name from the faker library
        last_name = fake.last_name()

        # Fake email - a combination of first and last name with random numbers
        domain = '@cevipsa.com'
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15)) + domain

        # check website title - Runs from script_selectors.py - assert_element_text method
        try:
            script_selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
            print('The header is correct')
        except WDE:
            print('The header is incorrect')

        # signup for the ESPN website - Runs from script_selectors.py - signup method
        script_selectors.signup(driver, email, first_name, last_name)

        # Check ESPN logo is present - top-left
        try:
            assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
            print('Logo is present')
        except WDE:
            print('Logo is not visible')

        script_selectors.open_side_menu(driver)

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
        script_selectors.favorite_team(driver)
        time.sleep(1)

        # Log out from the account
        script_selectors.log_out(driver)
        time.sleep(1)

        # Log back in
        script_selectors.log_in(driver, email)
        time.sleep(1)

        # Delete the account - Runs from script_selectors.py - delete_profile method
        script_selectors.delete_profile(driver)
        time.sleep(1)

        # Try to sign in into deleted account - check if account is still active or not
        try:
            assert "There's a problem" in script_selectors.log_in_no_account(driver, email)
            print("Account is disabled")
        except TypeError:
            print('Finishing test - Fail due to confirmation dialog')
        except WDE:
            print("The account is still active")

    def test_espn_chrome_1120_850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)

        # navigate to the ESPN website - Runs from selector.py - main_link
        driver.get(script_selectors.main_link)

        # Fake first name from the faker library
        first_name = fake.first_name()

        # Fake last name from the faker library
        last_name = fake.last_name()

        # Fake email - a combination of first and last name with random numbers
        domain = '@cevipsa.com'
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15)) + domain

        # check website title - Runs from script_selectors.py - assert_element_text method
        try:
            script_selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
            print('The header is correct')
        except WDE:
            print('The header is incorrect')

        # signup for the ESPN website - Runs from script_selectors.py - signup method
        script_selectors.signup(driver, email, first_name, last_name)

        # Check ESPN logo is present - top-left
        try:
            assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
            print('Logo is present')
        except WDE:
            print('Logo is not visible')

        script_selectors.open_side_menu(driver)

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
        script_selectors.favorite_team(driver)
        time.sleep(1)

        # Log out from the account
        script_selectors.log_out(driver)
        time.sleep(1)

        # Log back in
        script_selectors.log_in(driver, email)
        time.sleep(1)

        # Delete the account - Runs from script_selectors.py - delete_profile method
        script_selectors.delete_profile(driver)
        time.sleep(1)

        # Try to sign in into deleted account - check if account is still active or not
        try:
            assert "There's a problem" in script_selectors.log_in_no_account(driver, email)
            print("Account is disabled")
        except TypeError:
            print('Finishing test - Fail due to confirmation dialog')
        except WDE:
            print("The account is still active")

    def tearDown(self):
        self.driver.quit()


#
#
# class EdgeESPN(unittest.TestCase):
#     def setUp(self):
#         self.driver = webDrivers.edgeDriver()
#
#     def test_espn_edge(self):
#         driver = self.driver
#
#         # navigate to the ESPN website - Runs from selector.py - main_link
#         driver.get(selectors.main_link)
#
#         # Fake first name from the faker library
#         first_name = fake.first_name()
#
#         # Fake last name from the faker library
#         last_name = fake.last_name()
#
#         # Fake email - a combination of first and last name with random numbers
#         email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"
#
#         # check website title - Runs from script_selectors.py - assert_element_text method
#         try:
#             script_selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
#             print('The header is correct')
#         except WDE:
#             print('The header is incorrect')
#
#         # signup for the ESPN website - Runs from script_selectors.py - signup method
#         script_selectors.signup(driver, email, first_name, last_name)
#
#         # Check ESPN logo is present - top-left
#         try:
#             assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
#             print('Logo is present')
#         except WDE:
#             print('Logo is not visible')
#
#         script_selectors.open_side_menu(driver)
#
#         # Check Welcome message with correct name is present
#         try:
#             welcome_text = driver.find_element(By.CLASS_NAME, "display-user").text
#             assert first_name in welcome_text
#             print(f'text detected - Welcome {first_name}')
#         except AssertionError:
#             welcome_text = driver.find_element(By.XPATH, "(//li[@class='display-user'])[2]").text
#             assert first_name in welcome_text
#             print(f'asserted through secondary locator - Welcome {first_name}')
#         except WDE:
#             print('The welcome massage not detected')
#
#         # Add teams to favorites - Runs from script_selectors.py favorite_team method
#         selectors.favorite_team(driver)
#         time.sleep(1)
#
#         # Log out from the account
#         selectors.log_out(driver)
#         time.sleep(1)
#
#         # Log back in
#         script_selectors.log_in(driver, email)
#         time.sleep(1)
#
#         # Delete the account - Runs from script_selectors.py - delete_profile method
#         selectors.delete_profile(driver)
#         time.sleep(1)
#
#         # Try to sign in into deleted account - check if account is still active or not
#         try:
#             assert "There's a problem" in selectors.log_in_no_account(driver, email)
#             print("Account is disabled")
#         except TypeError:
#             print('Finishing test - Fail due to confirmation dialog')
#         except WDE:
#             print("The account is still active")
#
#     def test_espn_edge_1120x850(self):
#         driver = self.driver
#         driver.set_window_size(1120, 850)
#
#         # navigate to the ESPN website - Runs from selector.py - main_link
#         driver.get(selectors.main_link)
#
#         # Fake first name from the faker library
#         first_name = fake.first_name()
#
#         # Fake last name from the faker library
#         last_name = fake.last_name()
#
#         # Fake email - a combination of first and last name with random numbers
#         email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"
#
#         # check website title - Runs from script_selectors.py - assert_element_text method
#         try:
#             script_selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
#             print('The header is correct')
#         except WDE:
#             print('The header is incorrect')
#
#         # signup for the ESPN website - Runs from script_selectors.py - signup method
#         script_selectors.signup(driver, email, first_name, last_name)
#
#         # Check ESPN logo is present - top-left
#         try:
#             assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
#             print('Logo is present')
#         except WDE:
#             print('Logo is not visible')
#
#         selectors.open_side_menu(driver)
#
#         # Check Welcome message with correct name is present
#         try:
#             welcome_text = driver.find_element(By.CLASS_NAME, "display-user").text
#             assert first_name in welcome_text
#             print(f'text detected - Welcome {first_name}')
#         except AssertionError:
#             welcome_text = driver.find_element(By.XPATH, "(//li[@class='display-user'])[2]").text
#             assert first_name in welcome_text
#             print(f'asserted through secondary locator - Welcome {first_name}')
#         except WDE:
#             print('The welcome massage not detected')
#
#         # Add teams to favorites - Runs from script_selectors.py favorite_team method
#         selectors.favorite_team(driver)
#         time.sleep(1)
#
#         # Log out from the account
#         selectors.log_out(driver)
#         time.sleep(1)
#
#         # Log back in
#         script_selectors.log_in(driver, email)
#         time.sleep(1)
#
#         # Delete the account - Runs from script_selectors.py - delete_profile method
#         script_selectors.delete_profile(driver)
#         time.sleep(1)
#
#         # Try to sign in into deleted account - check if account is still active or not
#         try:
#             assert "There's a problem" in script_selectors.log_in_no_account(driver, email)
#             print("Account is disabled")
#         except TypeError:
#             print('Finishing test - Fail due to confirmation dialog')
#         except WDE:
#             print("The account is still active")
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# class FireFoxESPN(unittest.TestCase):
#     def setUp(self):
#         self.driver = webDrivers.firefoxDriver()
#
#     def test_espn_ff(self):
#         driver = self.driver
#
#         # navigate to the ESPN website - Runs from selector.py - main_link
#         driver.get(script_selectors.main_link)
#
#         # Fake first name from the faker library
#         first_name = fake.first_name()
#
#         # Fake last name from the faker library
#         last_name = fake.last_name()
#
#         # Fake email - a combination of first and last name with random numbers
#         email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"
#
#         # check website title - Runs from script_selectors.py - assert_element_text method
#         try:
#             selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
#             print('The header is correct')
#         except WDE:
#             print('The header is incorrect')
#
#         # signup for the ESPN website - Runs from script_selectors.py - signup method
#         selectors.signup(driver, email, first_name, last_name)
#
#         # Check ESPN logo is present - top-left
#         try:
#             assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
#             print('Logo is present')
#         except WDE:
#             print('Logo is not visible')
#
#         selectors.open_side_menu(driver)
#
#         # Check Welcome message with correct name is present
#         try:
#             welcome_text = driver.find_element(By.CLASS_NAME, "display-user").text
#             assert first_name in welcome_text
#             print(f'text detected - Welcome {first_name}')
#         except AssertionError:
#             welcome_text = driver.find_element(By.XPATH, "(//li[@class='display-user'])[2]").text
#             assert first_name in welcome_text
#             print(f'asserted through secondary locator - Welcome {first_name}')
#         except WDE:
#             print('The welcome massage not detected')
#
#         # Add teams to favorites - Runs from script_selectors.py favorite_team method
#         script_selectors.favorite_team(driver)
#         time.sleep(1)
#
#         # Log out from the account
#         script_selectors.log_out(driver)
#         time.sleep(1)
#
#         # Log back in
#         selectors.log_in(driver, email)
#         time.sleep(1)
#
#         # Delete the account - Runs from script_selectors.py - delete_profile method
#         script_selectors.delete_profile(driver)
#         time.sleep(1)
#
#         # Try to sign in into deleted account - check if account is still active or not
#         try:
#             assert "There's a problem" in script_selectors.log_in_no_account(driver, email)
#             print("Account is disabled")
#         except TypeError:
#             print('Finishing test - Fail due to confirmation dialog')
#         except WDE:
#             print("The account is still active")
#
#     def test_espn_ff_1120x850(self):
#         driver = self.driver
#         driver.set_window_size(1120, 850)
#
#         # navigate to the ESPN website - Runs from selector.py - main_link
#         driver.get(script_selectors.main_link)
#
#         # Fake first name from the faker library
#         first_name = fake.first_name()
#
#         # Fake last name from the faker library
#         last_name = fake.last_name()
#
#         # Fake email - a combination of first and last name with random numbers
#         email = f"{first_name}.{last_name}{random.randint(100, 5000)}@gmail.com"
#
#         # check website title - Runs from script_selectors.py - assert_element_text method
#         try:
#             selectors.assert_element_text('ESPN - Serving Sports Fans. Anytime. Anywhere.', driver.title)
#             print('The header is correct')
#         except WDE:
#             print('The header is incorrect')
#
#         # signup for the ESPN website - Runs from script_selectors.py - signup method
#         selectors.signup(driver, email, first_name, last_name)
#
#         # Check ESPN logo is present - top-left
#         try:
#             assert driver.find_element(By.XPATH, "//a[@href='/'][contains(.,'ESPN')]").is_displayed()
#             print('Logo is present')
#         except WDE:
#             print('Logo is not visible')
#
#         selectors.open_side_menu(driver)
#
#         # Check Welcome message with correct name is present
#         try:
#             welcome_text = driver.find_element(By.CLASS_NAME, "display-user").text
#             assert first_name in welcome_text
#             print(f'text detected - Welcome {first_name}')
#         except AssertionError:
#             welcome_text = driver.find_element(By.XPATH, "(//li[@class='display-user'])[2]").text
#             assert first_name in welcome_text
#             print(f'asserted through secondary locator - Welcome {first_name}')
#         except WDE:
#             print('The welcome massage not detected')
#
#         # Add teams to favorites - Runs from script_selectors.py favorite_team method
#         selectors.favorite_team(driver)
#         time.sleep(1)
#
#         # Log out from the account
#         selectors.log_out(driver)
#         time.sleep(1)
#
#         # Log back in
#         selectors.log_in(driver, email)
#         time.sleep(1)
#
#         # Delete the account - Runs from script_selectors.py - delete_profile method
#         selectors.delete_profile(driver)
#         time.sleep(1)
#
#         # Try to sign in into deleted account - check if account is still active or not
#         try:
#             assert "There's a problem" in script_selectors.log_in_no_account(driver, email)
#             print("Account is disabled")
#         except TypeError:
#             print('Finishing test - Fail due to confirmation dialog')
#         except WDE:
#             print("The account is still active")
#
#     def tearDown(self):
#         self.driver.quit()


today = datetime.datetime.today()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
