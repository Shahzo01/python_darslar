# input()
# ism = input('Ismingiz nima? ')
# savol = f"Salom {ism.title()} yoshingiz nechida? "
# yosh = input(savol)
# height = input('Bo\'yingiz nechi metr? ')
# height = float(height)
# While()
# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1
# print('Dastur tugadi!')

# print('Istalgan sonni kvadratini hisoblovchi dastur')
# savol = 'Istalgan sonni kiriting  '
# savol += f'\ndasturni to\'xtatish uchun "exit" so\'zini kiriting ==>>'
# qiymat = ' '
# # while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
# print('Dastur tugadi')

# print('Istalgan sonni kvadratini hisoblovchi dastur')
# savol = 'Istalgan sonni kiriting  '
# savol += f'\ndasturni to\'xtatish uchun "exit" so\'zini kiriting ==>>'
# qiymat = ' '
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi!!!")


# print('Istalgan sonni kvadratini hisoblovchi dastur')
# savol = 'Istalgan sonni kiriting  '
# savol += f'\ndasturni to\'xtatish uchun "exit" so\'zini kiriting ==>>'
# qiymat = ' '
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi!!!")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son ** 2} ga teng")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son ** 2} ga teng")

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# savol = input('Sevimli kitobingizni kiriting '
#               '(dasturni yakunlash uchun "stop" so\'zini kiriting )')
# kitob = ' '
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         print('Dastur yakunlandi!!!')

# chipta = 2000
# chipta1 = chipta + 1000
# chipta2 = chipta1 + 7000
# yosh = "Yoshingizni kiriting: "
# yosh += f"Foydalanuvchi 'exit' yoki 'stop' deb yozganda dastur to'xtaydi: "
# yosh = input(yosh)
# while True:
#     if yosh == 'exit' or yosh == 'stop':
#         print("Dastur to'xtadi!!!")
#         break
#     yosh = int(yosh)
#     if int(yosh) < 7:
#         print(f"Chipta narhi {chipta} siz uchun")
#         break
#     elif 7 <= int(yosh) <= 18:
#         print(f"Cipta narhi {chipta1} siuz uchun")
#         break
#     elif 18 <= int(yosh) <= 65:
#         print(f"Chipta narhi {chipta2} siz uchun")
#         break
#     else:
#         print('Chipta narhi sizga bepul!!!')
#         break

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         continue
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
