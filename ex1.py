import requests
from bs4 import BeautifulSoup
import pandas as pd


soup: BeautifulSoup = BeautifulSoup(requests.get('https://astrakhan.electric-doma.ru/').text, features='html.parser')

df = pd.DataFrame({'Наименование работ': [], 'Цена': []})

for el in soup.find_all(attrs={'data-service-name': True}):
    name =  el['data-service-name']
    #df.loc[ len(df.index) ] = [name, el['data-service-price'] ]
    print(name)
    
df.to_excel('prise.xlsx')


