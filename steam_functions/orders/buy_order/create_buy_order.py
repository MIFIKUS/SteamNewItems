import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from logger.logger import Logs

log = Logs()

class CreateBuyOrder:
    def __init__(self, driver):
        self._driver = driver
        self.MARKET_PLACE_URL = 'https://steamcommunity.com/market/listings/'

    def create_buy_order(self, item_name: str, amount: int, price_for_each: int):

        log.log('Попытка перейти на сайт шмотки')
        self._get_item_url(item_name)
        log.success('Удалось перейти на сайт шмотки')
        time.sleep(1)

        log.log('Попыта открыть окно бай ордера')
        self._open_buy_order()
        log.success('Удалось открыть окно бай ордера')
        time.sleep(1)

        log.log('Попытка вставить информацию в бай ордер')
        self._set_info(amount, price_for_each)
        log.log('Удалось вставить информацию в бай ордер')
        time.sleep(1)

        log.log('Попытка подтвердить бай ордер')
        self._confirm()
        log.success('Удалось подтвердить бай ордер')
        time.sleep(4)

    def _get_item_url(self, item_name: str):
        item_name = item_name.replace(' ', '%20')
        self._driver.get(f'{self.MARKET_PLACE_URL}/730/{item_name}')

    def _open_buy_order(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[4]/div/div[2]/div/div[4]/div[4]/div[1]/div/div[1]/a')))
        self._driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[4]/div/div[2]/div/div[4]/div[4]/div[1]/div/div[1]/a').click()

    def _set_info(self, amount: int, price_for_each: int):
        log.log(f'Цена {price_for_each} Колличество {amount}')
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[5]/div/div/div[2]/a[1]')))
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[2]/div[2]/input').click()
        time.sleep(1)
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[2]/div[2]/input').clear()
        time.sleep(1)

        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/input').click()
        time.sleep(1)
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/input').clear()
        time.sleep(1)

        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/input').click()
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/input').send_keys(Keys.CONTROL + 'a')
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/input').send_keys(str(price_for_each))

        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[3]/div[2]/div[2]/input').send_keys(str(amount))

    def _confirm(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[5]/div/div/div[2]/a[1]')))
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[5]/div/div/div[2]/div[1]/input').click()
        self._driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[5]/div/div/div[2]/a[1]').click()