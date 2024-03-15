from selenium.webdriver import Chrome, ChromeService

from parser.main_page import GetItems
from steam_functions.login.login import Login
from steam_functions.item_info.get_info import GetInfo
from steam_functions.orders.buy_order.create_buy_order import CreateBuyOrder
from steam_functions.acc_info.main_info import MainAccInfo

from logger.logger import Logs

import time

log = Logs()


log.log('Попытка создать драйвер')
chrome_service = ChromeService(executable_path='services_files\\chromedriver.exe')
driver = Chrome(service=chrome_service)
log.success('Драйвер создан')

login = Login(driver)
items = GetItems()
info = GetInfo(driver)
acc_info = MainAccInfo(driver)
buy_order = CreateBuyOrder(driver)

log.success('Все классы инициализированы')

log.log('Попытка залогиниться')
login.login()
log.success('Удалось залогиниться')

def get_main_list():
    main_items_list = {}
    counter = 1
    while True:
        while True:
            items_list = items.get_items_list(counter)
            if items_list == 'TIMEOUT':
                time.sleep(300)
            else:
                break
        if items_list == 'END':
            break
        main_items_list.update(items_list)
        counter += 100
    return main_items_list

print('Собран полный список шмоток')

def get_additional_list():
    while True:
        additional_items_list = {}
        counter = 1
        while True:
            items_list = items.get_items_list(counter)
            if items_list == 'TIMEOUT':
                time.sleep(300)
            else:
                break
            counter += 100
        if items_list == 'END':
            break

        additional_items_list.update(items_list)
        counter += 100


log.log('Получение основного списка шмоток...')
main_items_list = get_main_list()
log.success('Удалсь получить основной список шмоток')

while True:
    log.log('Получение дополнитнльного списка шмоток...')
    additional_list = get_additional_list()
    log.success('Удалось получить дополнительный список шмоток')

    if main_items_list != additional_list:
        log.warning('Найдено несоответсвие между списками')

        difference = [i for i in additional_list.items() if i not in main_items_list.items()]
        log.log(f'Новые шмотки и их ссылки {difference}')

        log.log('Начало покупки шмоток')
        for i in difference:
            link = i[0]
            item_name = i[1]
            log.log(f'Название: {item_name} Ссылка: {link}')

            driver.get(link)

            item_info = info.get_info()
            log.log(f'Полная информация о шмотке {item_info}')

            item_type = item_info['item_type']
            item_price = item_info['item_price']
            log.log(f'Тип: {item_type} Цена: {item_price}')

            log.log('Попытка получить баланс')
            balance = acc_info.get_balance()
            log.success(f'Удалось получить баланс. Баланс: {balance}')

            amount_items_to_buy = int((balance / 100 * 10) / item_price)

            log.log(f'Колличество шмоток к покупке: {amount_items_to_buy}')

            log.log('Попытка создать бай ордер')
            buy_order.create_buy_order(item_name,amount_items_to_buy, item_price)

    main_items_list = additional_list
