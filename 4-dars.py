'''
son = 50

if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")    


yosh = int(input("yoshingizni kiriting: ")) 
if yosh <= 4:
    print("Sizga kirish bepul")
elif yosh <= 12:
    print("Sizga kirish 5000 so\'m") 
else:
    print("Sizga kirish 10000 so'\m ")          


kun = input("Bugun nima kun?>>> ")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print('Dam olish kuni')
else:
    print('Bugun ish kuni')  
    
kun = input("Bugun nima kun?>>> ")
harorat = float(input("Havo harorati qanday>>> "))
if (kun.lower() == 'yakshanba'or kun.lower() == 'shanba') and  harorat >= 30:
    print("Cho\'milgani ketdik! ")
elif (kun.lower() == 'yakshanba'or kun.lower() == 'shanba') and harorat < 30:
    print('Uyda dam olamiz!')    
      
narx = 15000
choy = True 
salat = False

if choy and salat:
    narx = narx + 10000
elif choy or salat:
    narx = narx + 5000    
print(f"Jami {narx} so'm ")       



menu = ['osh', 'qozonkabob', ' shashlik', 'norin','somsa']
ovqat = input("Nima ovqat yeysiz?:  ")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday ovqat yo\'q")     
'''
menu = ['osh', 'qozonkabob', 'shashlik', 'norin','somsa']
buyurtmalar = ['osh', 'somsa','manti','shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menyuda {taom} bor" )
        else:
            print(f"Kechirasiz, menuda {taom} yo'q ")
else:
    print("savatcha bo'sh ")                