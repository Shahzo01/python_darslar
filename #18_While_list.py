# ismlar = []
# print("Do'stlaringizni ro'yhatini tuzamiz: ")
# n = 1
# while True:
#     savol = input(f"{n} - Do'stingizni ismini yozing: ")
#     ismlar.append(savol)
#     takrorlash = input("Yana ism qo'shasizmi ? (ha/yo'q)")
#     n += 1
#     if takrorlash != 'ha':
#         break
# print("Do'stlaringiz ro'yhati")
# for ism in ismlar:
#     print(ism.title())

# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input("Do'stingizni yoshini kiritning: ")
#     savol = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     dostlar[ism] = int(yosh)
#     if savol != 'ha':
#         ishora = False
# print("Do'stlaringiz ro'yhati: ")
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} da")

# talabalar = ['davron', 'ulug\'bek', 'shahzod', 'firdafs']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.capitalize()} ga nechi baho: ")
#     print(f"{talaba.capitalize()} baholandi uning bahosi {baho}")
#     baholangan_talabalar[talaba] = int(baho)

# mahsulotlar = {}
# while True:
#     savol = input("Mahsulot nomini kiriting: ")
#     narx = input("Kiritgan mahsulotingizni narhini ham kiriting: ")
#     mahsulotlar[savol] = int(narx)
#     javob = input("Mahsulot kiritishni hohlaysizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         break
# print(mahsulotlar)