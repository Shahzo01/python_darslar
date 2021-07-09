# cars_0 = {'model': 'ferrari', 'rang': 'qizil'}
# print(cars_0['model'])
# print(cars_0['rang'])

# talaba = {'ism': 'shahzod boymirzayev', 'yosh': 20, 't_yil': 2001}
# print(f"{talaba['ism'].title()},\
# {talaba['t_yil']} - yilda tug'ulgan,\ "
#       f"{talaba['yosh']} yoshda")
# talaba['kurs'] = 2
# talaba['fakultet'] = 'amaliy matematika va informatika'
# talaba['ism'] = 'dovron'
# print(talaba)

# talaba = {}

# talaba['ism'] = 'rustam'
# talaba['kurs'] = 3
# talaba['yosh'] = 20
# print(talaba)
# del talaba['ism']
# print(talaba)
# ism = (talaba.get('ism', 'bunday malumot mavjud emas!'))
# print(ism)


#AMALIYOT
# otam = {'ism': 'xolmamat', 'yil': 1963, 'viloyat': 'chiroqchi'}
# onam = {'ism': 'mohigul', 'yil': 1969, 'viloyat': 'chiroqchi'}
# print(f" Otamning ismi {otam['ism'].title()}, {otam['yil']} yilda {otam['viloyat'].title()} viloyatida tug'ulganlar")
# print(f" Onamning ismi {onam['ism'].title()}, {onam['yil']} yilda {onam['viloyat'].title()} viloyatida tug'ulganlar")

# s_taomlar = {'baxrom': 'xonim', 'chorsham': 'manti', 'farrux': 'osh'}
# print(f"Baxromning sevimli taomi {s_taomlar['baxrom']}")
# print(f"Chorshamning sevimli taomi {s_taomlar['chorsham']}")
# print(f"Farruxning sevimli taomi {s_taomlar['farrux']}")

# py_lugat = {'if': "shartli ravishda qo'llanaladigan operator",
#             'else': 'shart bajarilmaganda ishga tushadigan operator',
#             'for': 'tafrorlash operatori', 'float': 'o\'nli son',
#             'integer': 'butun son'}
# k_soz = input('Kalit so\'zini kiriting:')
# if k_soz in py_lugat:
#     print(py_lugat[k_soz])
# else:
#     print('Bunday kalit mavjud emas!!!')

# py_lugat = {'if': "shartli ravishda qo'llanaladigan operator",
#             'else': 'shart bajarilmaganda ishga tushadigan operator',
#             'for': 'tafrorlash operatori', 'float': 'o\'nli son',
#             'integer': 'butun son'}
# k_soz = input('Kalit so\'zini kiriting:')
# k_soz1 = py_lugat.get(k_soz, 'Bunday kalit so\'z mavjud emas!!!')
# print(k_soz1)
