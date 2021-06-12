# yosh = int(input('Yoshingiz nechada?\n==>>'))
# if yosh <= 4:
#     print('Sizga kirish tekin!')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechada?\n==>>'))
# if yosh <= 4:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# else:
#     narx = 10000
# print(f'Sizga kirish {narx} so\'m')

# kun = input('Bugun qanday kun?\n==>>')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni!')
# else:
#     print('Bugun ish kuni')

# kun = input('Bugun qanday kun?\n==>>')
# harorat = float(input('Havo harorati qanday?\n==>>'))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
#     print('Cho\'milgani ketdik!')
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print('Uyda dam olamiz!')
# else:
#     print('Uyda qoling!')

# taom = 15000
# choy = True
# salat = False
# if choy and salat:
#     taom = taom + 10000
# elif choy or salat:
#     taom = taom + 5000
# print(taom)

# ovqat = 15000
# choy = 0
# kompot = 1
# non = 1
# if choy:
#     print('Mijoz choy olmadi')
#     ovqat = ovqat + 2000
# if kompot:
#     print('Mijoz kompot oldi!')
#     ovqat = ovqat + 5000
# if non:
#     print('Mijoz non oldi')
#     ovqat = ovqat + 2000*2
# print(f'Jami {ovqat} so\'m')

# menyu = ['osh', 'qozon kabob', 'shashlik', 'somsa']
# ovqat = input('Nima ovqat yeysiz?\n==>>')
# if ovqat.lower() in menyu:
#     print('Buyurtmangiz qabul qilindi!')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menyu = ['osh', 'qozon kabob', 'shashlik', 'somsa']
# ovqat = input('Nima ovqat yeysiz?\n==>>')
# if ovqat.lower() not in menyu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtmangiz qabul qilindi!')

# menyu = ['osh', 'shashlik', 'somsa', 'qozon kabob']
# buyurtmalar = ['somsa', 'manti', 'shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menyu:
#             print(f'Kechirasiz menyuda {taom} bor')
#         else:
#             print(f'Menyuda {taom} yo\'q')

# j_son = int(input('Juft son kiriting:'))
# if j_son%2:
#     print('Juft son kiriting!')
# else:
#     print('Raxmat!')

# yosh = int(input('Yoshingizni kiriting:'))
# if yosh < 4 or yosh > 60:
#     print('Agar foydalanuvchining yoshi 4 dan kichik yoki 60 dan katta bo\'lsa chipta tekin!')
# elif yosh < 18:
#     print('Agar foydalanuvchininh yishi 18 dan kichik bo\'lsa chipta 10000 so\'m')
# else:
#     print('Agar foydalanuvchininh yishi 18 dan katta bo\'lsa 20000 so\'m')

# AMALIYOT

# son1 =float(input('Birinchi sonni kiriting:'))
# son2 =float(input('Ikkinchi sonni kiriting:'))
# if son1 > son2:
#     print(f'{son1} > {son2}')
# elif son1 == son2:
#     print(f'{son1} = {son2}')
# else:
#     print(f'{son1} < {son2}')

# mahsulotlar = ['non', 'un', 'go\'sht', 'kartoshka', 'pomidor', 'tuz', 'gilos', 'olma', 'qatiq', 'pishiriq']
# savat = []
# for n in range(5):
#     savat.append(input(f'{n+1} - mahsulotni kiriting:'))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'{mahsulot} Do\'konimizda bor')
#     else:
#         print(f'{mahsulot} Do\'konimizda yo\'q')

# mahsulotlar = ['un', 'yog\'', 'shakar', 'non', 'shaftoli', 'olma', 'nok', 'go\'sht']
# savat = []
# for n in range(5):
#     savat.append(input(f'{n + 1} - masulotni qoshing:'))
#
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f'Do\'konimizda quyidagi mahsulotlar yo\'q:')
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print(f'Do\'konimizda quyidagi mahsulotlar bor:')

# foydalanuvchilar = []
# for n in range(5):
#     foydalanuvchilar.append(input(f'{n+1} - loginni kiriting:'))
#
# new_login = input('Yangi login kiriting:')
# if new_login in foydalanuvchilar:
#     print('Login band!!! \nYangi login tanlang', new_login)
# else:
#     print('Xush kelibsiz', new_login)

# son = float(input('Istalgan sonni kiriting:'))
# for n in range(2, 11):
#     if not (son % n):
#         print(f'{son} soni {n} ga qoldiqsiz bo\'linadi')

