# 1
while True:
    print("nyangkut di perulangan tak hingga")

# 2
angka = 1
while angka < 5:
    print(angka)
    angka += 1

# 3
rahasia_angka = 66
angka = int(input("Masukan angka :"))
while angka != rahasia_angka:
    print("Bukan angka itu yang aku mau, masukan angka lain")
    angka = int(input("Masukan angka :"))
print("Hebat, kamu berhasil menebak angkanya")

# 4
for i in range(10):
    print("Nilai i saat ini adalah", i)

# 5
for i in range(2, 8):
    print("Nilai i saat ini adalah", i)

# 6
for i in range(2, 10, 3):
    print("Nilai i saat ini adalah", i)

# 7
import time
for i in range(1, 6):
    print(i, "Mississipi")
    time.sleep(1)
print("Ready or not, here I come!")

# 8
while True:
    kata = input("Masukan kata :")
    if kata == "chupacabra":
        break
print("Kamu berhasil keluar dari perulangan")

# 9
kata_input = input("Masukan kata :")
kata_input = kata_input.upper()
for huruf in kata_input:
    if huruf in ['A', 'E', 'I', 'O', 'U']:
        continue
    print(huruf)

# 10
kata_input = input("Masukan kata :")
kata_input = kata_input.upper()
kata_baru = ""
for huruf in kata_input:
    if huruf in ['A', 'E', 'I', 'O', 'U']:
        continue
    kata_baru += huruf
print(kata_baru)

# 11
angka = int(input("Masukan jumlah blok :"))
tinggi = 0
blok_dibutuhkan = 1
while angka >= blok_dibutuhkan:
    angka -= blok_dibutuhkan
    tinggi += 1
    blok_dibutuhkan += 1
print("Tinggi piramida :", tinggi)

# 12
c0 = int(input("Masukan angka non-negatif & non-nol: "))
langkah = 0
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    langkah += 1
print(c0)
print("langkah =", langkah)

# 13
x = 1
y = 4
print(x & y)
print(x | y)
print(~x)
print(x ^ y)

# 14
I = 8
kiri = I << 1
kanan = I >> 1
print(kiri)
print(kanan)

# 15
x = 4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = c << 2
print(a, b, c, d, e, f)
