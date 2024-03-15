from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from steam_functions import _get_credentials

from logger.logger import Logs

logs = Logs()

class Login:
    def __init__(self, driver):
        self.LOGIN_PAGE = 'https://steamcommunity.com/login/home/'
        self._login = _get_credentials.get_login()
        self._password = _get_credentials.get_password()
        self._driver = driver

    def login(self):
        logs.log('Попытка перейти на страницу логина')
        self._get_login_page()
        logs.success('Удалось перейти на страницу логина')

        logs.log('Попытка ввести логин')
        self._set_login()
        logs.success('Удалось ввести логин')

        logs.log('Попытка ввести пароль')
        self._set_password()
        logs.success('Удалось ввести пароль')

        logs.log('Попытка нажать кнопку подтвердить')
        self._apply()
        logs.success('Удалось нажать кнопку подтвердить')

        logs.log('Попытка ввести стим гвард')
        self.set_steam_guard_code()
        logs.success('Удалось ввести стимгвард')

    def _get_login_page(self):
        self._driver.get(self.LOGIN_PAGE)

    def _set_login(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')))
        self._driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input').send_keys(self._login)

    def _set_password(self):
        self._driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys(self._password)

    def _apply(self):
        self._driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()

    def set_steam_guard_code(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/form/div/div[2]/div[1]/div')))
        code = input('Введите код стим гварда')

        counter = 1
        for i in code:
            self._driver.find_element(By.XPATH, f'/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/form/div/div[2]/div[1]/div/input[{counter}]').send_keys(i)
            counter += 1




