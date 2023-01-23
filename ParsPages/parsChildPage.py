from bs4 import BeautifulSoup
import requests
import re


def parsCP(head_url: str, ch_url: str) -> tuple:
    print(f'парсим {head_url+ch_url} \n')
    soup: BeautifulSoup =  BeautifulSoup(requests.get(head_url+ch_url).text, features='html.parser')
    lst = []
    
    for el in soup.find_all(attrs={'class': 'odd'}):
        try:
            name = str(el.find(attrs={'class': 'service-name'}).string).strip()
            price = el.find(attrs ={'class': 'realPrice'})
            unit = re.search(r'[а-я]+\.?\s?[а-я]*',str(el.find('small')))

            if price == None:
                price = el.find_all('td')[2]
            
            if unit == None:
                unit = [""]
            
            
            price = re.search(r'\d+\s?\d*|[а-яА-Я]+', str(price))[0]

        # парсим https://astrakhan.santehnic-doma.ru/ustanovka-batarey.php 

            lst.append((name, price, unit[0], ))
        except Exception as e: print(e) 
    
    return tuple(lst)

if __name__ == '__main__':
    print(parsCP('https://astrakhan.electric-doma.ru/', 'ustanovka-batarey.php'), sep='\n')