from bs4 import BeautifulSoup
import pandas as pd
import re
import requests


def makeLL(soup: BeautifulSoup) -> list:
    print(f'Получаем список ссылок с основной страницы')
    sM: BeautifulSoup = soup.find(id='servicesMenuList')
    lst_link = []

    for el in sM.find_all('a'):
        try:
            lst_link.append(re.search(r'\w*(-\w*)*.php',str(el))[0])
        except Exception as e:
            print(e)
            continue
    return lst_link


if __name__=='__main__':
    s = BeautifulSoup(requests.get('https://astrakhan.electric-doma.ru/').text, features="html.parser")
    for el in makeLL(s):
        print(el.split('.')[0].replace('-','_'))
