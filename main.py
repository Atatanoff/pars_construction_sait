import requests
from bs4 import BeautifulSoup
import pandas as pd

from ParsPages.parsHeadPage import parsHP
from ParsPages.makeListLink import makeLL
from ParsPages.parsChildPage import parsCP


list_head_url=(
    # 'https://astrakhan.electric-doma.ru/',
	'https://astrakhan.santehnic-doma.ru/',
	'https://astrakhan.muz-doma.ru/',
)


def write_sheet_list(name, data, sheet, mode='w'):
    df = pd.DataFrame(data) 
    with pd.ExcelWriter(name+'.xlsx', mode=mode, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=sheet)

def run():
    for url in list_head_url:
        soup: BeautifulSoup = BeautifulSoup(requests.get(url).text, features='html.parser')
        name_file = url.split('-')[0].split('.')[1]
        print(f'Парсим {url}')
        list_work_head_page = parsHP(soup)
        write_sheet_list(name_file, list_work_head_page, name_file)
        list_link = makeLL(soup)
        for ch_url in list_link:
            list_work_chield_page = parsCP(url, ch_url)
            
            write_sheet_list(name_file, list_work_chield_page, ch_url.split('.')[0].replace('-','_'), mode='a')
            


if __name__=='__main__':
    run()
    