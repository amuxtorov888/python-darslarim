#1-dars
'''
print("Hello, World!")
print(7+8)


#2-dars
print(""" Odam ersang, demak odami,
    Oniki, yo'q xalq g'amidin g'ami  """)
print(19/5)#qoldiq bilan chiqadi
print(19//5)#butun qismini chiqaradi
print(19%5)#qoldiq chiqadi
print(2**3)#darajaga oshirish
print(2*3+5/2-4)#amal bajarish tartibi
print((2*3+5)/2-4)#qavs ichidagi amal birinchi bajariladi
print("To'qizning kvadrati: ", 9**2, "ga teng")

#3-dars
ism = "Akmal"
yosh = 26
print("Mening ismim " + ism)
print("Mening yoshim " + str(yosh))

a = 6
b = 7
c = (a + b + yosh) ** 2
print(c)
'''
#4-dars
ism = 'James'
familiya = 'Bond'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())#katta harf bilan yozish
print(ism_sharif.lower())#kichik harf bilan yozish
print(ism_sharif.title())#har bir so'z bosh harfi katta bo'ladi
print(ism_sharif.capitalize())#faqat birinchi harf katta bo'ladi

meva = '    olma    '
print("men " + meva.lstrip() + "ni yaxshi ko'raman")#chap tomondagi bo'shliqlarni olib tashlaydi
print("men " + meva.rstrip() + "ni yaxshi ko'raman")#o'ng tomondagi bo'shliqlarni olib tashlaydi
print("men " + meva.strip() + "ni yaxshi ko'raman")#ikkala tomondagi bo'shliqlarni olib tashlaydi

ism = input("Ismingiz nima?:  ")
print("Assalomu alaykum, " + ism.title())

'''
print(ism_sharif.replace('a', 'o'))#bitta harfni boshqasi bilan almashtirish
print(ism_sharif.replace('James', 'Danial'))#so'zni boshqasi bilan almashtirish
print(ism_sharif.find('m'))#harf yoki so'z qaysiinchi indeksdan boshlanishini ko'rsatadi
print(ism_sharif.find('z'))#bunday harf yoki so'z yo'q bo'lsa -1 ni qaytaradi
print(ism_sharif.index('B'))#harf yoki so'z qaysiinchi indeksdan boshlanishini ko'rsatadi
# print(ism_sharif.index('Z'))#bunday harf yoki so'z yo'q bo'lsa xatolik beradi
print(len(ism_sharif))#so'z uzunligini ko'rsatadi
print(ism_sharif.count('a'))#so'zda nechta harf borligini ko'rsatadi
print(ism_sharif.count('z'))#bunday harf yo'q bo'lsa 0 ni qaytaradi
print(ism_sharif.startswith('J'))#so'z shu harf yoki so'z bilan boshlanadimi, deb so'raydi
print(ism_sharif.startswith('j'))#katta-kichik harfga e'tibor beradi
print(ism_sharif.endswith('d'))#so'z shu harf yoki so'z bilan tugaydimi, deb so'raydi
print(ism_sharif.endswith('D'))#katta-kichik harfga e'tibor beradi
print(ism_sharif.isalpha())#faqat harflardan tashkil topganmi, deb so'raydi
print(ism_sharif.isdigit())#faqat raqamlardan tashkil topganmi, deb so'raydi
print(ism_sharif.isspace())#faqat bo'shliqdan tashkil topganmi, deb so'raydi
print(ism_sharif + '1')#stringga raqam qo'shsa ham stringga aylanadi
'''