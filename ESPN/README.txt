------------------ ESPN Website Test ------------------

There are three folders with main.py files in them.

1. ESPN_test_logic => positive_test => main.py is a general script upon which unittest and BrowserStack tests were built. You can ignore that one or run it.

2. ESPN_unitTest => positive_test => main.py is a unit test with Chrome, Edge, and Firefox browser tests. Two tests for each

ESPN_BR => Positive_test => main.py is the script for BrowserStack.

All three scripts get functionalities from the ESPN/tools folder selectors.py and webDrivers.py. Put your BR credentials inside the tools folder.


webDrivers.py. manages all webdrivers. Comment or uncomment the "headless" option inside that folder for the headless function.

selectors.py has all locators and functions, and main.py controls the general flow.


------------------- website specific details -----------------

This website utilizes frames. Almost all operations open new frames where we should switch to handle them. Inside the frames, no elements have IDs or other distinctive characteristics. Some of them have CLASS names, but other elements also share those names. Also, all elements are dynamic, meaning they change positions and Xpaths depending on screen size.
To account for that, I implemented secondary Xpaths for some of them. So, the script addresses the secondary locator if the first one is not found. For example, the default screen size for Headless is 800x600. In that resolution, elements have different Xpaths than if we perform tests in larger resolution - for example, 1200x800.


------------------- about test -------------------

These are the steps that the script performs.

- navigate to the ESPN website
- assert that the ESPN logo is present
- open the side menu, go to the signup menu, and sign up
- open the side menu and assert that the welcome message includes the first name with which we just signed up
- go into the favorite teams tab and randomly add three teams to the favorites
- open side menu and log-out
- open the side menu and sign in again
- open the side menu, go to account options, and delete the account
- open the side menu and try to log in with the deleted account
- assert that an error message showed up when we tried to pass a deleted email


-------------------- notes -----------------------

1. Sometimes, when favorite teams are typed, teams do not show up in Firefox. This happens only in FF, and the test will skip this part if it occurs.
 
2. In rare cases, the ESPN website will ask for the code they send to email. This happens when we try to log in to the account.
If that happens, there is little we can do, so I implemented a "fail-safe switch," which ends that test and proceeds to the next one.