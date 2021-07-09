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
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til)
