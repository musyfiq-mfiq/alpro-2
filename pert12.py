# 1. Variable local: variable yang berada di dalam fungsi
def penjumlahan(x):
    bilangan = 20
    return x + bilangan

print(penjumlahan(4))
print(penjumlahan)

# 2. Variable di luar fungsi -1
bilangan = 12
def perkalian(x):
    return x * bilangan

print(perkalian(5))
print(perkalian)

# 3. Variable di luar fungsi -2
def perkalian_bilangan(x):
    bilangan = 10
    return x * bilangan

print(perkalian_bilangan(3))

# 4. Variable global dengan keyword 'global'
bilangan = 7
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 7
    return bilangan

print(return_bilangan())
print(bilangan)

# 5. Kuis IMT
def hitung_IMT(berat, tinggi):
    IMT = berat / (tinggi ** 2)
    return IMT

berat = 65
tinggi = 1.75
index_massa_tubuh = hitung_IMT(berat, tinggi)
kategori = ("kurus", "normal", "gemuk") #kategori IMT

#kategorikan nilai IMT yang sudah didapat
if index_massa_tubuh < 18.5:
    kategori = "Kurus"
    print("index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[0])
elif 18.5 <= index_massa_tubuh < 25:
    print("index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[1])
else:
    print("index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[2], ".anda harus diet")

# 6. Fungsi segitiga -1
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(cek_segitiga(3, 4, 5))
print(cek_segitiga(1, 2, 3))

# 7. Fungsi segitiga -2
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(3, 4, 5))
print(cek_segitiga(1, 2, 3))

# 8. Fungsi segitiga -3
def cek_segitiga(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(cek_segitiga(3, 4, 5))
print(cek_segitiga(1, 2, 3))

# 9. Kuis faktorial
def faktorial(n):
    #bilangan yang akan difaktorial harus lebih besar atau sama dari 0
    if n < 0:
        return None
    #0! dan 1! sama dengan 1
    if n
