from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class MainAccInfo:
    def __init__(self, driver):
        self._driver = driver

    def get_balance(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'header_wallet_balance')))

        balance_string = self._driver.find_element(By.ID, 'header_wallet_balance').text

        balance_string = balance_string.replace('pуб.', '')
        balance_string = balance_string.replace(',', '.')
        balance_string = balance_string.replace(' ', '')

        return float(balance_string)
