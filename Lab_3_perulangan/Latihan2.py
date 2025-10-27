import random

print("===========================================")
print("= Bilangan acak yang lebih kecil dari 0.5 =")
print("===========================================")

# Input jumlah bilangan acak yang ingin ditampilkan
jum = int(input("Masukkan jumlah bilangan acak: "))

i = 0
while i in range(jum):
    i += 1
    # Menghasilkan bilangan acak antara 0 sampai 0.5
    angka_random = random.uniform(0, 0.5)
    print("Bilangan ke-", i, ":", angka_random)

print("===========================================")
print("Program selesai menampilkan", jum, "bilangan acak.")