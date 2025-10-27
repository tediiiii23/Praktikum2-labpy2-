# Program menentukan bilangan terbesar dari 4 bilangan

print("=== Program Mencari Bilangan Terbesar ===")

# Input 4 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

# Tentukan bilangan terbesar menggunakan if
terbesar = a  # misalnya a adalah yang terbesar

if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

# Tampilkan hasil
print("Bilangan terbesar adalah:", terbesar)