list_head_url=(
    'https://astrakhan.electric-doma.ru/',
	'https://astrakhan.santehnic-doma.ru/',
	'https://astrakhan.muz-doma.ru/',
)
for el in list_head_url:
    s = el.split('-')[0].split('.')[1]
    print(s)