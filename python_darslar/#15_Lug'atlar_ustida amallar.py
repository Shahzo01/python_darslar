# talaba = {'ism': 'alijon',
#           'familiya': 'shamsiyev',
#           'yosh': 21, 'kurs': 4}
# print(talaba.items())
# for kalit, qiymat in talaba.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat}\n")

telefonlar = {'ali': 'galaxy s20',
              'vali': 'iphone 10',
              'olim': 'redmi note 10',
              'anvar': 'nokia 1202',
              'jovoh': 'iphone 10'}
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telifoni {q}")

# .keys() kalitlarni qaytaruvchi metod
mahsulotlar = {'olma': 10000,
               'anor': 12000,
               'nok': 15000,
               'shaftoli': 20000}
# print('Do\'konimizdagi mahsulotlar')
# for mevalar in mahsulotlar.keys():
#     print(mevalar.title())

# bozorlik = ['anor', 'nok', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling!!!!")

# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telefonlar.values())
# print('Foydalanuvchilar quidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#      print(tel.title())
# for tel in set(telefonlar.values()):
#     print(tel.title())

lugat = {'boolean': 'mantiqiy qiymat',
         'float': 'o\'nlik son',
         'for': 'biror bir amalni qayta-qayta bajarish tsikli',
         'int': 'butun son',
         'list': 'ro\'yhatlar',
         'type': 'turlari',
         'apple': 'olma',
         'apricot': 'o\'rik'
         }
# print('Tartiblangan lug\'at:')
# for k, q in sorted(lugat.items()):
#     print(f"{k} - {q}")


davlatlar = {
    "o'zbekiston": 'toshkent',
    'aqsh': 'washington',
    'rossiya': 'moskva',
    'tojikiston': 'dushanbe',
    "qirg'iziston": 'bishkek',
    'qozog\'iston': 'nursulton',
    'malayziya': 'kuala-lumpur',
    'singapur': 'sungapur',
    'italiya': 'rim'}
# for d, p in davlatlar.items():
#     print(f"{d.upper()} - {p.upper()}")
# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
#
# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.upper())
#
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital is None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

Restoran = {'osh': "35000",
            'manti': '4000',
            'somsa': '4500',
            'qozon kabob': '40000',
            'tandir': '45000',
            'shashlik': '15000'}
print('3 ta taom buturtma bering:\n')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taom : ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in Restoran:
        print(f"{buyurtma.title()} {Restoran[buyurtma]} so'm")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q")
