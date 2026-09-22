n = int(input("Masukkan nilai n: "))
a = 0
b = 1

print("Deret Fibonacci:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()