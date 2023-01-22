import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


URL = 'https://astrakhan.muz-doma.ru/'
name_file = URL.strip('https://astrakhan.').strip('-doma.ru/')


soup: BeautifulSoup = BeautifulSoup(requests.get(URL).text, features='html.parser')

sM: BeautifulSoup = soup.find(id='servicesMenuList')

lst_link = []

for el in sM.find_all('a'):
    lst_link.append(re.search(r'\w*(-\w*)*.php',str(el))[0])