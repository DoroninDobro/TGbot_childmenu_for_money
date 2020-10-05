import json

all_recipes = dict()

all_recipes['https://telegra.ph/Tvorozhnye-keksy-s-zavarnym-kremom-i-persikovym-dzhemom-09-27'] = ('Творожные кексы с заварным кремом и персиковым джемом', ['Сахар', 'Молоко', 'Мука', 'Яйцо', 'Джем', 'Творог', 'Разрыхлитель', 'Сливочное масло'])
all_recipes['https://telegra.ph/Morozhenoe-so-sgushchyonkoj-08-31'] = ('Мороженое со сгущёнкой', ['Сахар ванильный', 'Молоко сгущенное', 'Йогурт', 'Сметана'])
all_recipes['https://t.me/childrenmenu/946'] = ('РЫБНОЕ СУФЛЕ', ['яйцо'])

json.dump(all_recipes,open("dict_final.json","w"))
print('Success')