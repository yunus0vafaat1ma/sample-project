"""
1-topshiriq: Ikki sonni parametr sifatida qabul qiladigan va ularning yig‘indisini
qaytaruvchi funksiya yozing. Funktsiyani turli argumentlar bilan chaqirish orqali sinab ko'ring.
"""
# def yigindi(a, b):
#     return a + b

# print("5 + 3 =", yigindi(5, 3))
# print("10 + (-2) =", yigindi(10, -2))
# print("7 + 7 =", yigindi(7, 7))

"""
2-topshiriq: Satrni parametr sifatida qabul qiladigan va satr uzunligini qaytaruvchi
funksiyani loyihalash. Funktsiyani turli qatorlar bilan sinab ko'ring.
"""
# def satr_uzunligi(satr):
#     return len(satr)

# print("'Dasturlashga xush kebsan Faatima' uzunligi:", satr_uzunligi("Dasturlashga xush kebsan Faatima"))
# print("uzunligi:", satr_uzunligi("Seni nimalar kutib turibdiyaa...."))
"""
3-topshiriq: Berilgan sonning juft yoki toq ekanligini tekshiradigan funksiya yarating.
Funktsiya parametr sifatida butun sonni olishi va mantiqiy qiymatni qaytarishi kerak.
Funktsiyani turli raqamlar bilan sinab ko'ring.
"""
# def juft_tekshirish(son):
#     return son % 2 == 0
# raqamlar = [5, 7, 10, 13, 22, 24]

# for raqam in raqamlar:
#     print(f"{raqam} juftmi? {juft_tekshirish(raqam)}")
"""
4-topshiriq: Berilgan sonning faktorialini hisoblaydigan funksiyani yozing.
Funktsiya parametr sifatida butun sonni qabul qilishi va faktorial qiymatini qaytarishi kerak.
Funktsiyani turli raqamlar bilan sinab ko'ring.
"""
# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# print("5! =", faktorial(5))  # 5! = 120
# print("7! =", faktorial(7))  # 7! = 5040
# print("10! =", faktorial(10))  # 10! = 3628800
"""
5-topshiriq: Berilgan satrning palindrom ekanligini tekshiradigan funksiya tuzing.
Funktsiya parametr sifatida satrni olishi va mantiqiy qiymatni qaytarishi kerak.
Funktsiyani turli qatorlar bilan sinab ko'ring.(maslahat: satrni teskari o'zgartirish.
"""
# def palindrommi(satr):
#     palindrom_satr = satr[::-1]
#     return satr == palindrom_satr

# print(palindrommi("nok"))
# print(palindrommi("level"))
# print(palindrommi("radar"))
# print(palindrommi("hello"))
# print(palindrommi("non"))
# print(palindrommi("world"))
"""
6-topshiriq: Haroratni Selsiy shkalasiga aylantiruvchi funksiya yarating Farengeyt. 
Funktsiya parametr sifatida Selsiy bo'yicha haroratni olishi va Farengeytdagi 
o'zgartirilgan haroratni qaytarishi kerak. Funktsiyani turli qiymatlar bilan hisoblang.
"""
# def selsiydan_farengeytga(selsiy):
#     farengeyt = (selsiy * 9/5) + 32
#     return farengeyt

# print("0°C = ", selsiydan_farengeytga(0), "°F")
# print("25°C = ", selsiydan_farengeytga(25), "°F")
# print("100°C = ", selsiydan_farengeytga(100), "°F")
# print("37°C = ", selsiydan_farengeytga(37), "°F")
"""
7-topshiriq: Parametr sifatida raqamlar ro‘yxatini oladigan va barcha sonlar yig‘indisini 
qaytaruvchi funksiya yozing. Funktsiyani turli raqamlar ro'yxati bilan sinab ko'ring.
"""
# def raqamlar_yigindisi(raqamlar):
#     yigindi = sum(raqamlar)
#     return yigindi

# print(raqamlar_yigindisi([0, 0, 0, 0]))
# print(raqamlar_yigindisi([1, 2, 3, 4, 5]))
# print(raqamlar_yigindisi([10, 20, 30, 40]))
# print(raqamlar_yigindisi([-5, 5, -10, 10]))
# print(raqamlar_yigindisi([150, 200, 370]))
"""
8-topshiriq: To‘g‘ri to‘rtburchakning maydonini hisoblaydigan funksiyani loyihalash. 
Funktsiya uzunlik va kenglikni parametr sifatida qabul qilishi va maydonni qaytarishi kerak. 
Funktsiyani turli qiymatlar bilan sinab ko'ring.
"""
# def togritortburchak_maydoni(uzunlik, kenglik):
#     maydon = uzunlik * kenglik
#     return maydon

# print("Uzunlik 5, Kenglik 10: Maydon =", togritortburchak_maydoni(5, 10))
# print("Uzunlik 7, Kenglik 3: Maydon =", togritortburchak_maydoni(7, 3))
# print("Uzunlik 15, Kenglik 20: Maydon =", togritortburchak_maydoni(15, 20))
# print("Uzunlik 9, Kenglik 8: Maydon =", togritortburchak_maydoni(9, 8))
# print("Uzunlik 12, Kenglik 4: Maydon =", togritortburchak_maydoni(12, 4))
"""
9-topshiriq: Berilgan son tub son ekanligini tekshiradigan funksiya tuzing. 
Funktsiya parametr sifatida butun sonni olishi va mantiqiy qiymatni qaytarishi kerak. 
Funktsiyani turli raqamlar bilan sinab ko'ring.
"""
# def tubmi(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print("2 tub sonmi?", tubmi(2))
# print("4 tub sonmi?", tubmi(4))
# print("7 tub sonmi?", tubmi(7))
# print("9 tub sonmi?", tubmi(9))
# print("11 tub sonmi?", tubmi(11))
# print("15 tub sonmi?", tubmi(15))

"""
10-topshiriq: Berilgan qatorni teskari aylantiruvchi funksiya yozing. 
Funktsiya parametr sifatida satrni olishi va teskari satrni qaytarishi kerak. 
Funktsiyani turli qatorlar bilan sinab ko'ring.
"""
# def teskari_satr(satr):
#     return satr[::-1]

# print(teskari_satr("hello"))
# print(teskari_satr("python"))
# print(teskari_satr("12345"))
# print(teskari_satr("Dasturlash"))
# print(teskari_satr("Faatima"))
