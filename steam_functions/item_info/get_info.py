from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json


class GetInfo:
    def __init__(self, driver):
        self._driver = driver

    def get_info(self) -> dict:
        item_type = self._get_item_type()
        item_price = self._get_item_price(item_type)
        return {'item_type': item_type,
                'item_price': item_price}

    def _get_item_type(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(By.ID, 'largeiteminfo_item_type'))
        item_type_str = self._driver.find_element(By.ID, 'largeiteminfo_item_type')

        with open('steam_functions\\internal_files\\item_types.json') as item_types_json:
            item_types = json.load(item_types_json)

        for i in item_types.items():
            if item_type_str in i[1]:
                return item_types.get(i[0])

    def _get_item_price(self, item_type):
        with open('prices.json') as prices_json:
            prices = json.load(prices_json)

        return prices[item_type]
