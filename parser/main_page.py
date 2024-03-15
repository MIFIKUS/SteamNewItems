from bs4 import BeautifulSoup
import requests

class GetItems:
    def __init__(self):
        self._cs_items_url = 'https://steamcommunity.com/market/search/render/?query=&start={}&count=100&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730'

    def get_items_list(self, start):
        link = self._cs_items_url.format(start)
        content = requests.get(link)

        if content.status_code == 429:
            return 'TIMEOUT'

        soup = BeautifulSoup(content.json()['results_html'], 'lxml')

        if 'An error was encountered while processing your request' in soup:
            raise Exception('Too much requests')

        if 'Не обнаружены предметы, соответствующие поисковому запросу. Повторите попытку с другими ключевыми словами.' in soup:
            return 'END'

        items_data = soup.find_all('a', class_="market_listing_row_link")

        items_list = {}

        for i in items_data:
            link = i['href']
            item_name = i.find('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult")['data-hash-name']
            items_list.update({item_name: link})

        return items_list

