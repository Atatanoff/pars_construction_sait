import requests
from bs4 import BeautifulSoup
import pandas as pd


def td_not_has_class(tag):    
    if tag.name == 'td' and len(tag.attrs) == 0:
        return True
    else: False

def parsHP(soup: BeautifulSoup) -> tuple:
    lst = []

    for el in soup.find_all(attrs={'data-is-child': True}):
        name = el.a.string
        price = str(el.s).strip('<s> от').strip('руб </s>').strip()
        sell_price = str(el.find( attrs={ 'tooltip-club': True } )).strip('<span tooltip-club=""> от').strip('руб</span>').strip()
        if sell_price == 'None':
            sell_price = str(el.find_all(td_not_has_class)[0]).strip('<td>от').strip('руб</td>').strip()
        if price == 'None':
            price = sell_price
            sell_price = '-'
        lst.append((name, price, sell_price,))
    
    return tuple(lst)
    

if __name__=='__main__':
    soup: BeautifulSoup = BeautifulSoup(requests.get('https://astrakhan.muz-doma.ru/').text, features='html.parser')
    print(*parsHP(soup), sep='\n')
