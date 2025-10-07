'''
try:
    son = int(input("Son kiriting: "))
    print(10 / son)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")
except ValueError:
    print("Xatolik: Iltimos, faqat son kiriting!")

try:
    x = int(input("Son kiriting: "))
except ValueError:
    print("Xato! Son kiriting.")
else:
    print("Hammasi yaxshi, siz kiritgan son:", x)


try:
    f = open("data.txt")
    # fayl bilan ishlash
except FileNotFoundError:
    print("Fayl topilmadi!")
finally:
    print("Jarayon tugadi.")
'''

yosh = int(input("Yoshingizni kiriting: "))
if yosh < 0:
    raise ValueError("Yosh manfiy bo‘lishi mumkin emas!")

'''
| Kalit so‘z | Ma’nosi                           |
| ---------- | --------------------------------- |
| `try`      | Xato bo‘lishi mumkin bo‘lgan kod  |
| `except`   | Xatoni ushlaydi va javob beradi   |
| `else`     | Xato bo‘lmagan holatda bajariladi |
| `finally`  | Har qanday holatda ham bajariladi |
| `raise`    | O‘zingiz xato chiqarasiz          |

'''