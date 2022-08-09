import os
import sys

from selenium.webdriver.common.by import By

SYSTEM = sys.platform
PATH_TO_PROJECT = os.path.dirname(os.path.abspath(__file__))

if SYSTEM == 'mac64':
    CHROME_DRIVER = "chromedriver"
else:
    CHROME_DRIVER = "chromedriver 3"

DRIVER_PATH = os.path.join(PATH_TO_PROJECT, '/Users/innakoval/Documents/GitHub/test/drivers', CHROME_DRIVER)
IMPLICITLY_WAIT = 3
EXPLICITLY_WAIT = 30

DEFAULT_LOCATOR_TYPE = By.XPATH


UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

if SYSTEM == 'macOS':
    CHROME_DRIVER = 'chromedriver.exe'
    FIREFOX_DRIVER = 'geckodriver.exe'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
else:
    CHROME_DRIVER = 'chromedriver'
    FIREFOX_DRIVER = 'geckodriver'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
