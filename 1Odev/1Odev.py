#---------------------------------------------------------------------------------------------
# 1.SORU
# Kulanıcıdan iki sayı alarak bu sayıları toplayan bir programın pseudo kodunu yazın.

while True:
    try:#Kullanıcı sayısal değerler dışında bir değer girdiğinde programın hata vermemesi için try-except blokları kullanılmıştır.
        sayi1 = int(input("Toplama işlemi için birinci sayıyı giriniz: "))
        break
    except:
        print("Sadece sayısal değerler kabul edilir!!! \n")

while True:
    try:#Kullanıcı sayısal değerler dışında bir değer girdiğinde programın hata vermemesi için try-except blokları kullanılmıştır.
        sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
        break
    except:
        print("Sadece sayısal değerler kabul edilir!!! \n")

print("Toplama işlemi sonucu: ",(sayi1 + sayi2))
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# 2.SORU
#  1'den 100'e kadar olan sayıları toplayan bir programın pseudo kodunu yazın.

toplam=0
for i in range(1,101,1):
    toplam+=i

print("1 den 100 e kadar olan sayıların toplamı :",toplam)
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# 3.SORU
# Kulanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın pseudo kodunu yazın.

while True:
    try: #Kullanıcı sayısal değerler dışında bir değer girdiğinde programın hata vermemesi için try-except blokları kullanılmıştır.
        sayi=int(input("Asal olup olmadığını kontrol etmek için bir sayı giriniz : "))
        break
    except:
        print("Sadece sayısal değerler kabul edilir !!!")
asalmi=False
i=2
while (sayi/2) >= i:
    if(sayi%i==0):
        asalmi=True
        break
    else:
        i+=1
if sayi<=1:
    print("Girdiğiniz değer '2' sayısından küçüktür. '2' sayısından küçük sayılar asal değildir.",)
elif asalmi==True:
    print(sayi," Sayısı asal değildir.")
else:
    print(sayi," Sayısı asal bir sayıdır.")
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# 4.SORU
# Bir dizideki (array) elemanların tekrar edip etmediğini kontrol eden bir programın pseudo kodunu yazın.

#Aşağıda iki adet statik tanımlı dizi bulunmaktadır. Kontrolleri gerçekleştirmek için aşağıdaki diziler kullanılmıştır.

sayilar = [10, 25, 37, 42, 56, 22, 74, 81, 55, 102]
numbers = [5, 12, 7, 99, 19, 23, 42, 57, 31, 5]

kontroledilen=set()
sonuc=False

for sayi in numbers:
    if sayi in kontroledilen:
         sonuc=True
         print("Tekrar eden değer ", sayi)
    kontroledilen.add(sayi)

if sonuc==False:
    print("Tekrar eden değer bulunamadı.")
#---------------------------------------------------------------------------------------------



