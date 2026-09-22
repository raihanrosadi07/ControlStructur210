persen = int(input("Masukkan nilai persentase: "))

if persen >= 90:
    print("Excellent performance")
elif persen >= 80:
    print("Very Good performance")
elif persen >= 70:
    print("Good performance")
elif persen >= 60:
    print("Average performance")
else:
    print("Below Average performance")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print("Bilangan terbesar:", a)
elif b >= a and b >= c:
    print("Bilangan terbesar:", b)
else:
    print("Bilangan terbesar:", c)

n = int(input("Masukkan nilai n: "))
a = 0
b = 1

print("Deret Fibonacci:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

n = int(input("Masukkan nilai n: "))

print("Bilangan ganjil:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print() 