import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://astrakhan.muz-doma.ru/'
name_file = URL.strip('https://astrakhan.').strip('-doma.ru/')

def td_not_has_class(tag):
    
    if tag.name == 'td' and len(tag.attrs) == 0:
        return True
    else: False


soup: BeautifulSoup = BeautifulSoup(requests.get(URL).text, features='html.parser')

df = pd.DataFrame({'Наименование работ': [], 'Цена': [], 'Цена членов клуба': []})

for el in soup.find_all(attrs={'data-is-child': True}):
    # name =  el['data-service-name']
    # df.loc[ len(df.index) ] = [name, el['data-service-price'] ]
    name = el.a.string
    price = str(el.s).strip('<s> от ').strip(' руб </s>')
    sell_price = str(el.find( attrs={ 'tooltip-club': True } )).strip('<span tooltip-club=""> от').strip(' руб</span>')
    if sell_price == 'None':
        sell_price = str(el.find_all(td_not_has_class)[0]).strip('<td>от ').strip(' руб</td>')
    df.loc[ len(df.index) ] = [name, price, sell_price ]
df.to_excel(f'prise_{name_file}.xlsx', sheet_name='Общие работы')


