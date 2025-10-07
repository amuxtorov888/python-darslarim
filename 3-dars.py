'''
mehmonlar = ['Ali', 'Vali', 'Husan', 'Hasan', 'Olim']
#print('Salom',mehmonlar[0])

for mehmon in mehmonlar:
    #print('Salom',mehmon)
    print(f"Hurmatli {mehmon} sizni 20-Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan Abdullayevlar oilasi\n")


sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng ")

sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2) 
    
print(sonlar)
print(sonlar_kvadrati)      

dostlar = []
print('5 ta dostingiz kim?')

for n in range(5):
    dostlar.append(input(f"{n+1} - dostingizni kirining: "))
print(f" {dostlar} \n Bu sizning 5 ta dostingiz")     

avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:    
        print(avto.title())
 
ism = input("Ismingizni kiriting: \n")
if ism.lower() != 'akmal':
    print(f"Uzr {ism.title()} biz Akmalni kutyabmiz")
else:
    print("Salom, Akmal")     
 
javob = float(input("12x6 nechiga teng?>>>"))
if javob != 72 :
    print('Javob xato')
       
yosh = int(input("Yoshingizni kirining: "))
if yosh >= 18:
    print("Xush kelibsiz!")
else:
    print("Kirish mmkin emas!")        
'''
x, y = 25,50
print('x>y') if x>y else print('x<y')
    