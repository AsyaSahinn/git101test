sayi =str(input("Lütfen bir sayı giriniz") )
dizi = []
toplam = 0
for i in range(len(sayi)):
    dizi.append(sayi[i])

for i in range(len(dizi)):
    dizi[i] = int(dizi[i])
    toplam += dizi[i] ** len(dizi)

if toplam == int(sayi):
    print("ARMSTRONG SAYI")
else:
    print("değil")