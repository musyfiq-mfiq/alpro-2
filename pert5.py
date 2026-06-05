# 1
x = 1
y = 2
z = 3
print(x == y)
print(x == z)
print(z == y)
print(x != y)
print(x != z)
print(z != y)
print(x > y)
print(x > z)
print(x > y)
print(x < y)
print(x < z)
print(z < y)
print(x >= y)
print(x >= z)
print(z >= y)
print(x <= y)
print(x <= z)

# 2
angka = 2
print(angka > 0)
print(angka < 0)

# 3
persen = 82
print(persen >= 80)
print(persen < 80)

# 4
n = int(input("masukan nilai n :"))
print(n >= 100)

# 5
angka = int(input("masukan nilai angka :"))
if angka > 100:
    print("angka diatas 100")

# 6
angka = int(input("masukan nilai angka :"))
if angka > 100:
    print("angka diatas 100")
else:
    print("angka dibawah 100")

# 7
angka = int(input("masukan nilai angka :"))
if angka > 100:
    print("angka diatas 100")
elif angka == 100:
    print("angka adalah 100")
else:
    print("angka dibawah 100")

# 8
angka1 = int(input("masukan angka pertama :"))
angka2 = int(input("masukan angka kedua :"))
if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2
print("angka yang paling besar adalah :", angka_besar)

# 9
angka1 = int(input("masukan angka pertama :"))
angka2 = int(input("masukan angka kedua :"))
angka3 = int(input("masukan angka ketiga :"))
angka_besar = max(angka1, angka2, angka3)
print("angka yang paling besar adalah :", angka_besar)

# 10
pendapatan = int(input("masukan pendapatan pertahun :"))
if pendapatan <= 50000000:
    pajak = 0.05 * pendapatan
elif pendapatan <= 250000000:
    pajak = 0.15 * pendapatan
elif pendapatan <= 500000000:
    pajak = 0.25 * pendapatan
else:
    pajak = 0.30 * pendapatan
print("Pajak yang harus dibayar adalah :", pajak, "rupiah")

# 11
tahun = int(input("masukan tahun :"))
if tahun < 1582:
    print("Bukan tahun kabisat (bukan kalender Gregorian)")
elif tahun % 4 != 0:
    print("Tahun Kabisat")
elif tahun % 100 != 0:
    print("Tahun kabisat")
elif tahun % 400 != 0:
    print("Tahun Kabisat")
else:
    print("Tahun kabisat")
