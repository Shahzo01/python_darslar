# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
#
#
# talaba = toliq_ism_yasa('shahzod', 'boymirzayev')
# print(talaba)
# print(f"{talaba} darsga keldi!")
#
#
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya!"""
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familiya.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism.title()
#
# talaba = toliq_ism_yasa('shahzod', 'xolmamat', 'boymirzayev')
# print(talaba)
# talaba = toliq_ism_yasa('shahzod', 'boymirzayev')
# print(talaba)


# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'karobka': karobka,
#             'yil': yili,
#             'narh': narhi}
#     return avto


# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2021)
# avto2 = avto_info('GM', 'Malibu', 'Oq', 'Avtomat', 2021, 30000)
# avtolar = [avto1, avto2]
# # print(avtolar[0]['narh'])
# print("Online bozordagi moshinalar")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'Nomalum'
#     print(f"{avto['model']} rangi {avto['rang']} narhi = {narh}")


# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
#
#
# oraliq(0, 10)
# oraliq(10, 20)
# print(oraliq(0, 10), oraliq(10, 20))


# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'karobka': karobka,
#             'yil': yili,
#             'narh': narhi}
#     return avto
#
#
# print("Saytimizdagi alveolar ro'yhatini shakllantiramiz!")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end=' ')
#     kompaniya = input('Ishlab chiqaruvchi: ')
#     model = input('Modeli: ')
#     rangi = input('Rangi: ')
#     karobka = input('Karobka: ')
#     yili = input('Ishlab chiqarilgan yili: ')
#     narhi = input('Narhi: ')
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'Nomalum'
#     print(f"{avto['rang'].title()} \t{avto['model'].title()}"
#           f"\t{avto['karobka'].title()} yili = {avto['yil'].title()}"
#           f"\tnarhi = {avto['narh'].title()}")


def oraliq(min, max, qadam=''):
    sonlar = []
    qadam = input("Qadamlar soni: ")
    while min < max:
        sonlar.append(min)
        min += int(qadam)
    return sonlar


print(oraliq(0, 10))
