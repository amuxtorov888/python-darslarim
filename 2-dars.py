'''
a = 20 # integer
b = 5.5 # float
temp = 36.6 # float
print(type(a))
print(type(b)) 
aholi_soni = 7_594_000_000
print('Aholi soni: ', aholi_soni)

x,y,z = 10, 5.5, -56
print(type(x), type(y), type(z))

c = a*b
print(c)

d = 100//2 

radius = 20
pi = 3.14159
area = pi * radius**2
print("Radiusi", radius, "ga teng doiraning yuzi =", area) 

t_yil = input("Tug'ilgan yilingizni kiriting: ")
yosh = 2025 - int(t_yil)
print("Sizning yoshingiz: ", yosh)


mevalar = ['olma', 'anor', 'anjir', 'shaftoli'] # mevalar ro'yxati'''
narxlar = [12000, 15000, 18000, 22000] # narxlar ro'yxati
'''
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar ro'yxati
ismlar = [] # bo'sh ro'yxat
print(mevalar[0]) # ro'yxatning birinchi elementini chaqirish
print(mevalar[-1]) # ro'yxatning to'rtinchi elementini chaqirish
print(narxlar[1]) # ro'yxatning ikkinchi elementini chaqirish
print(sonlar[-1]) # ro'yxatning oxirgi elementini chaqirish
print(mevalar[1:3]) # ro'yxatning ikkinchi va uchinchi elementini chaqirish
print(mevalar[:3]) # ro'yxatning birinchi uchta elementini chaqirish
print(mevalar[1:]) # ro'yxatning ikkinchi elementidan boshlab oxirigacha chaqirish
print(mevalar[-3:]) # ro'yxatning oxirgi uchta elementini chaqirish
print(mevalar[::2]) # ro'yxatning juft indeksli elementlarini chaqirish
print(mevalar[::-1]) # ro'yxatni teskari tartibda chaqirish
mevalar[0] = 'nok' # ro'yxatning birinchi elementini o'zgartirish
mevalar.append('tarvuz') # ro'yxatning oxiriga yangi element qo'shish
mevalar.append('qovun') # ro'yxatning oxiriga yangi element qo'shish
mevalar.extend(['abrikos', 'o\'rik']) # ro'yxatning oxiriga yangi elementlar qo'shish
mevalar.insert(2, 'gilos') # ro'yxatning uchinchi elementi sifatida yangi element qo'shish
mevalar.insert(3, 'banan') # ro'yxatning to'rtinchi elementi sifatida yangi element qo'shish
mevalar.remove('anor') # ro'yxatdan anor elementini o'chirish
mevalar.pop(1) # ro'yxatning ikkinchi elementini o'chirish
del mevalar[0] # ro'yxatning birinchi elementini o'chirish
mevalar.sort() # ro'yxatni alfavit tartibida tartiblash
#mevalar.sort(reverse=True) # ro'yxatni teskari alfavit tartibida tartiblash

cars = []

cars.append('BMW')
cars.append('Mercedes')     
cars.append('Toyota')
cars.append('Kia')  
cars.append('Hyundai')
cars.append('Chevrolet')
cars.append('Nexia')    
cars.remove('Nexia')
cars.sort() # alfavit tartibida
cars.sort(reverse=True) # teskari alfavit tartibida
    


print(mevalar) 
print(cars)
print(len(cars)) # ro'yxatdagi elementlar soni  


bozorlik = ['un', 'yog\'', 'shakar', 'tuz', 'piyoz', 'kartoshka', 'sabzi', 'olma', 'banan', 'apelsin']
print(bozorlik)
mahsulot = bozorlik.pop(0)
print('Men ' + mahsulot + ' sotib oldim')
print('Olinmagan mahsulotlar: ', bozorlik)

cars = []

cars.append('BMW')
cars.append('Mercedes')     
cars.append('Toyota')
cars.append('Kia')  
cars.append('Hyundai')
cars.append('Chevrolet')
cars.append('Nexia')    
cars.remove('Nexia')
#cars.sort() # alfavit tartibida
cars.sort(reverse=True) # teskari alfavit tartibida
sonlar = [12,45,23,56,998,1,5,78,34]
sonlar.sort()
#print(sorted(sonlar, reverse=True))#sort qilmaydi, asl ro'yxat o'zgarmaydi
#print( sorted(sonlar) )#sort qilmaydi, asl ro'yxat o'zgarmaydi
sonlar = list(range(21,30))#21 dan 300 gacha 10 lik oralik bilan sonlar ro'yxatini yaratadi
print(sonlar)


#print(cars)


toq_sonlar = list(range(1,20,2))#1 dan 20 gacha bo'lgan toq sonlar ro'yxatini yaratadi
juft_sonlar = list(range(0,21,2))#0 dan 20 gacha bo'lgan juft sonlar ro'yxatini yaratadi
max_qiymat = max(toq_sonlar)
sanash = list(range(0,100))


print(toq_sonlar)
print(juft_sonlar)
#print(sanash)
print(max_qiymat)
print(min(narxlar))
print(max(narxlar))
print(sum(narxlar))
print("Eng arzonnarx:  ",min(narxlar) , "Eng qimmati:  ",max(narxlar), "Jami: ",sum(narxlar))

cars = ['Bmw','Mersedes-Benz','Porch,','Volva','Tesla','Audi']


my_cars = cars[:]
my_cars.remove('Volva')
my_cars[0] = 'Lacetti'

print(cars)
print(my_cars)
'''
#Tuple

toys = ('bus','car','bear','dino','snake','lizard')
toys = list(toys)
toys.append('teddy')

#print(toys[0])
#print(toys[2:5])
#print(toys[3:])
print(type(toys))
print(toys)


