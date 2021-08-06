car0 = {
    'model': 'lasetti',
    'rang': 'oq',
    'yil': '2015',
    'narh': '9000',
    'km': '190000',
    'karobka': 'avtomat'
}

car1 = {
    'model': 'nexia3',
    'rang': 'ko\'k',
    'yil': '2018',
    'narh': '10000',
    'km': '20000',
    'karobka': 'mehanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'havorang',
    'yil': '2020',
    'narh': '13000',
    'km': 'karobka',
    '40000': 'avtomat'
}
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rangda, "
#       f"{car['yil']} - yil, {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#         print(f"{car['model'].title()}, "
#               f"{car['rang']} rangda, "
#               f"{car['yil']} - yil, {car['narh']}$")

# print(cars[0]['model'].title())

malibus = []
for new_car in range(10):
    new_car = {
        'model': 'malibu',
        'rang': None,
        'narx': None,
        'yil': '2021',
        'karobka': 'avto'
    }
    malibus.append(new_car)
# print(malibus)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['karobka'] = 'mexanika'

# for malibu in malibus:
#     print(malibu)

# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx'] = 35000
# for malibu in malibus:
#     print(malibu)

dasturchilar = {'shahzod': ['python', 'html, css', '3dmax'],
                'eldor': ['java', 'python', 'html, css'],
                'sunnatilla': ['java', 'js', 'html, css'],
                'bobur': ['java', 'js', 'html, css'],
                }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quidagi dasturlash tillarini biladi: ")
#     for til in tillar:
#         print(f'{til.upper()}', end=" ")

hamkasblar = {
    'davron': {
        'familiya': 'ashurov',
        't_yil': '2001',
        'malumot': 'oliy',
        'tillar': ['o\'zbek', 'rus']
    },
    'oybek': {
        'familiya': 'tuychiyev',
        't_yil': '2000',
        'malumot': 'o\'rta',
        'tillar': 'o\'zbek'
    },
    'rustam': {
        'familiya': 'safarov',
        't_yil': '2001',
        'malumot': "o'rta",
        'tillar': 'o\'zbek'
    }
}
# for ism, info in hamkasblar.items():
#     print(f'{ism.title()} {info["familiya"].title()} '
#           f'{info["t_yil"]} - da tug\'ulgan '
#           f'Malumoti {info["malumot"].title()} '
#           f'{info["tillar"]} tilini yaxshi biladi')

# AMALIYOT
mashxurlar = {
    'stiv': {
        'familiya': 'jobs',
        'yil': 1955,
        'joy': 'san fransisko kaliforniya',
        'umr': 56
    },

    'erkin': {
        'familiya': 'vohidov',
        'yil': 1963,
        'joy': 'farg\'ona',
        'umr': 80
    },

    'elon': {
        'familiya': 'mask',
        'yil': 1971,
        'joy': 'janubiy afrika',
        'umr': 'hozirda hoyot'
    }
}
# for ism, info in mashxurlar.items():
#     print(f"{ism.upper()} {info['familiya'].upper()} "
#           f"{info['yil']} - da {info['joy'].upper()} da tavallud topgan "
#           f"{info['umr']} yil umr kurgan")

kinolar = {
    'davron': [
        'rembo',
        'terminator',
        'uzuklar hukmdori'
    ],
    'oybek': [
        'geta',
        'forsaj',
        'tutash taqdirlar'
    ],
    'rustam': [
        'jeyms bond',
        'ulfatlar',
        'pubg'
    ]
}
# for ism, kino in kinolar.items():
#     print(f"{ism.title()} ning sevimli kinosi:")
#     for n in kino:
#         print(n.upper())

davlatlar = {
    "o'zbekiston": {
        'poytaxt': 'toshkent',
        'hududi': 448978,
        'aholisi': 34.800000,
        'pul birligi': 'so\'m'
    },

    'rossiya': {
        'poytaxt': 'moskva',
        'hududi': 17_098_246,
        'aholisi': 144_000_000,
        'pul birligi': 'rubl'
    },

    'aqsh': {
        'poytaxt': 'vashington',
        'hududi': 9_631_418,
        'aholisi': 327_000_000,
        'pul birligi': 'dollar ==>> $ '
    },

    'malayziya': {
        'poytaxt': 'kuala - lumpur',
        'hududi': 329_750,
        'aholisi': 325_000_000,
        'pul birligi': 'ringit'
    }
}
for davlat, info in davlatlar.items():
    print(f'\n{davlat.upper()}\nPoytaxt - {info["poytaxt"].upper()}'
          f'\nHududi - {info["hududi"]} kv.km ga teng'
          f'\nAholisi - {info["aholisi"]} mln kishi'
          f'\nPul birligi - {info["pul birligi"].capitalize()}')

# davlat1 = input('Davlat nomini kiriting: ').lower()

# if davlat1 == davlatlar:
#     info = davlatlar[davlat1]
#     print(f"{davlatlar[davlat1.upper()]}\nPoytaxt - {info['poytaxt']}"
#           f"\nHududi - {info['hududi']} kv.km"
#           f"\nAholisi - {info['aholisi']}"
#           f"\nPul birligi - {info['pul birligi']}")
# else:
#     print(f"{davlat1} bizda bunday malunot yo'q")