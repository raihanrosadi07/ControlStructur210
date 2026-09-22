a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print("Bilangan terbesar:", a)
elif b >= a and b >= c:
    print("Bilangan terbesar:", b)
else:
    print("Bilangan terbesar:", c)

    