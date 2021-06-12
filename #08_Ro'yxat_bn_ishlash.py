# cars = ['bmw', 'ferrari', 'audi', 'tesla', 'mers']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# # sort metodi alifbo tartibi bo'yicha tartiblaydi ro'yhatlarni, katta harf kelganda dastlab uni yozadi
# texnika = ['kir_moshina', 'telivizor', 'dazmol', 'gaz_plita', 'Blendir']
# texnika.sort()
# print(texnika)
# texnika.sort(reverse=True)
# print(texnika)

# mevalar = ['olma', 'anor', 'gilos', 'xurmo', 'shaftoli']
# print(sorted(mevalar))
# print(mevalar)
# print(sorted(mevalar, reverse=True))

# sonlar = [12, 23, 45, -98, -7.99, 20.5]
# print(sorted(sonlar, reverse=True))
# print(sorted(sonlar))

# ro'yhatni teskarisiga aylantirib qo'yamiz
# poliz_ekinlari = ['qovun', 'tarvuz', 'oshqovoq', 'sabzi', 'piyoz', 'pomidor', 'bodiring']
# poliz_ekinlari.reverse()
# print(poliz_ekinlari)
# print(len(poliz_ekinlari))
# son = len(poliz_ekinlari)
# print(son)

# # range() funksiasi
# sonlar = list(range(0, 10))
# print(sonlar)
# t_sonlar = list(range(1, 20, 2))
# j_sonlar = list(range(2, 21, 2))
# print(t_sonlar)
# print(j_sonlar)
# max_qiymat1 = max(t_sonlar)
# max_qiymat2 = max(j_sonlar)
# min_qiymay1 =min(t_sonlar)
# min_qiymay2 = min(j_sonlar)
# print(max_qiymat1)
# print(max_qiymat2)
# print(min_qiymay1)
# print(min_qiymay2)

# narhlar = [12000, 20000, 12500, 18000, -9000, 19999]
# # print(min(narhlar))
# # print(max(narhlar))
# # print(sum(narhlar))
# # print(narhlar[:3])
# # print(narhlar[2:])
# sonlar = narhlar[:]
# print(sonlar)
# print(sonlar[2:])
# print(sonlar[:2])

# # Tuples bu o'zgarmas ro'yhat oddiy qavsda belgilanadi
# kompyuter = ('hp', 'asus', 'aser', 'lenova', 'del', 'apple')
# print(type(kompyuter))
# kompyuter = list(kompyuter)
# print(type(kompyuter))
# kompyuter.append('windows')
# kompyuter.insert(-1, "linux")
# print(kompyuter)

# davlatlar = ['Uzbekistan', 'Russion', 'Usa', 'China', 'India', 'Dubay', 'Afrika', 'Avstralya']
# print(davlatlar)
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# j_sonlar = list(range(120, 1201, 2))
# print(sum(j_sonlar))
# print(max(j_sonlar) - min(j_sonlar))
# print(len(j_sonlar))
# sonlar1 = j_sonlar[:20]
# sonlar2 = j_sonlar[270:290]
# sonlar3 = j_sonlar[-20:]
# print(sonlar1)
# print(sonlar2)
# print(sonlar3)
