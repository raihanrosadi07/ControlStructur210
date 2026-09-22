n = int(input("Masukkan nilai n: "))

print("Bilangan ganjil:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()
