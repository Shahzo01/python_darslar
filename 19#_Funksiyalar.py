# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu Alekum")

# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchidan ismini so'rab
#     salom beruvchi dastur"""
#     print(f"Assalomu Alekum Hurmatli! {ism.title()}")


# salom_ber('ikromjon')

#  DOCSTRING Funksiya haqida malumot!
# print(input.__doc__)

# def salom_ber(ism='shahzod', familiya='boymirzayev'):
#     """Foydalanuvchiin ism familiyasini sorab consolga chiqruvchi dastur"""
#     print(f"Assalom Alekum hurmatli {ism.title()} {familiya.title()}! ")


# salom_ber('ikromjon', 'odiljonov')
# salom_ber()


# def yil_aniqlash(t_yil=2001, j_yil=2021, ism='shahzod'):
#     """Foydalanuvchidan ismini sorab yoshini aniqlovchi dastur"""
#     print(f"Assalom Alekum hurmatli {ism.capitalize()} siz {j_yil - t_yil} yoshdasiz!")

# yil_aniqlash()

# 1
# def yosh_hisobla(ism, t_yil=int(input('Tug\'ulgan yilingizni kiriting:')), j_yil=2021):
#     """Foydalanuvchidan ismini, yilini sorab ismini, yoshini aniqlovchi dastur!"""
#     print(f"Assalom Alekum hurmatli {ism.title()} siz {j_yil - t_yil} yoshdasiz!")


# yosh_hisobla('shahzod')

# 2
# def daraja_hisobla(son=int(input("Istalgan sonni kiriting: "))):
#     """Foydalanuvchidan son olib kvadrati va kubini hisoblovchi dastur"""
#     print(f"{son} sonining kvadrati {son**2} ga teng "
#           f"kubi {son**3} ga teng")
# daraja_hisobla()

# 3
# def juft_toqligi(son=int(input('Istalgan sonni kiriting: '))):
#     """Foydalanuvchidan son olib, juft yoki toqligini aniqlovchi dastur!"""
#     if son % 2 == 0 and son > 0:
#         print(f"{son} soni juft son")
#     elif son % 2 == 1 and son > 0:
#         print(f"{son} soni toq son!")
#     elif son == 0:
#         print(f"{son} bu raqam juft ham emas toq ham emas!")
#     else:
#         print(f"siz {son} manfiy son kiritdingiz!")


# juft_toqligi()


# def juft_toqligi(son):
#     """Foydalanuvchidan son olib, juft yoki toqligini aniqlovchi dastur!"""
#     if son % 2 == 0 and son > 0:
#         print(f"{son} soni juft son")
#     elif son % 2 == 1 and son > 0:
#         print(f"{son} soni toq son!")
#     elif son == 0:
#         print(f"{son} bu raqam juft ham emas toq ham emas!")
#     else:
#         print(f"siz {son} manfiy son kiritdingiz!")


# juft_toqligi(son=int(input('Istalgan sonni kiriting: ')))

# 4
# def s_taqqoslash(son1, son2):
#     """Foydalanuvchidan ikkita son so'rab qaysi
#     katta bo'lsa shuni consolga chiqaruvchi dastur"""
#     if son1 > son2:
#         print(f"{son1} > {son2}")
#     elif son1 == son2:
#         print(f"{son1} = {son2}")
#     else:
#         print(f"{son1} < {son2}")


# s_taqqoslash(son1=int(input('Birinchi sonni kiriting: ')), son2=int(input('Ikkinchi sonni kiriting: ')))

# 5
# def daraja_hisoblash(x, y=2) -> object:
#     """Foydalanuvchidan x va y sonlarini olib,x**y ni konsolga chiqaruvchi funksiya yozing."""
#     print(f"{x} ning kvadrati {x ** y} ga teng bo'ladi")


# daraja_hisoblash(x=int(input('Istalgan sonni kiriting: ')))

# 6
# def bolinuvchi(x=int(input('Istalgan sonni kiriting: '))):
#     """Foydalanuvchidan son qabul qilib,
#         sonni 2 dan 10 gacha bo'lgan sonlarga
#         qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
#         Natijalarni konsolga chiqaring."""
#     for n in range(2, 11):
#         if x % n == 0 and x >= 0:
#             print(f"{x}, {n} ga qoldiqsiz bo'linadi javob:{x // n}")


# bolinuvchi()
