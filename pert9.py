# 1
data = [8, 5, 7, 3, 9, 1, 4, 89, 5, 0]
for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Hasil:", data)

# 2
my_list = []
swapped = True
num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))
for i in range(num):
    val = float(input("Masukkan elemen list: "))
    my_list.append(val)
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("\nSorted:")
print(my_list)

# 3
my_list = []
num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))
for i in range(num):
    val = float(input("Masukkan elemen list: "))
    my_list.append(val)
my_list.sort()
print("\nSorted:")
print(my_list)

# 4
listsaya = [5, 2, 8, 1, 3]
print("Sebelum reverse:", listsaya)
listsaya.reverse()
print("Sesudah reverse:", listsaya)

# 5
my_list = [10, 20, 30, 40, 50]
print("List awal:", my_list)
# Mengakses elemen berdasarkan indeks
print("Elemen pertama:", my_list[0])
print("Elemen ketiga:", my_list[2])
# Mengubah nilai elemen
my_list[1] = 25
print("Setelah diubah:", my_list)
# Menambahkan elemen baru
my_list.append(60)
print("Setelah ditambah:", my_list)

# 6
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil elemen dari indeks 1 sampai 4
print("Slice [1:4]:", my_list[1:4])
# Mengambil elemen dari awal sampai indeks 3
print("Slice [:3]:", my_list[:3])
# Mengambil elemen dari indeks 2 sampai akhir
print("Slice [2:]:", my_list[2:])

# 7
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil dari indeks positif ke indeks negatif
print("Slice [1:-1]:", my_list[1:-1])
print("Slice [2:-2]:", my_list[2:-2])

# 8
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil dari indeks negatif ke indeks positif
print("Slice [-4:5]:", my_list[-4:5])
print("Slice [-3:6]:", my_list[-3:6])

# 9
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil dari awal sampai indeks tertentu
print("Slice [:3]:", my_list[:3])
print("Slice [:4]:", my_list[:4])

# 10
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil dari indeks tertentu sampai akhir
print("Slice [2:]:", my_list[2:])
print("Slice [3:]:", my_list[3:])

# 11
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Mengambil seluruh elemen list
new_list = my_list[:]
print("Hasil slice [:]:", new_list)

# 12
my_list = [10, 20, 30, 40, 50, 60]
print("List awal:", my_list)
# Menghapus elemen dari indeks 1 sampai 3
del my_list[1:4]
print("Setelah menghapus slice:", my_list)

# 13
my_list = [10, 20, 30, 40, 50]
print("List awal:", my_list)
# Menghapus semua elemen
my_list.clear()
print("Setelah dihapus:", my_list)

# 14
my_list = [10, 20, 30, 40, 50]
print("List awal:", my_list)
# Menghapus list
del my_list
# Catatan: print(my_list) sengaja tidak disertakan/dikomentari karena variabel sudah dihapus dan akan memicu Error

# 15
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
# Mengecek apakah nilai ada dalam list
print(20 in my_list)
print(60 in my_list)

# 16
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
# Mengecek apakah nilai tidak ada dalam list
print(60 not in my_list)
print(20 not in my_list)

# 17
my_list = []
num = int(input("Masukkan jumlah data: "))
for i in range(num):
    data = int(input("Masukkan angka: "))
    my_list.append(data)
print("Data dalam list:", my_list)
print("Nilai terbesar:", max(my_list))
print("Nilai terkecil:", min(my_list))

# 18
my_list = []
num = int(input("Masukkan jumlah data: "))
for i in range(num):
    data = int(input("Masukkan angka: "))
    my_list.append(data)
print("Data dalam list:", my_list)
print("Jumlah data:", len(my_list))
print("Total nilai:", sum(my_list))
print("Rata-rata:", sum(my_list) / len(my_list))

# 19
my_list = []
num = int(input("Masukkan jumlah data: "))
for i in range(num):
    data = int(input("Masukkan angka: "))
    my_list.append(data)
print("Data sebelum diurutkan:", my_list)
my_list.sort()
print("Data setelah diurutkan:", my_list)
my_list.reverse()
print("Data setelah dibalik:", my_list)

# 20
tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]
benar = 0
for angka in tebakan:
    if angka in hasil:
        benar += 1
print("Angka tebakan:", tebakan)
print("Angka yang keluar:", hasil)
print("Jumlah tebakan yang benar:", benar)

# 21
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
for angka in my_list:
    if angka not in unique_list:
        unique_list.append(angka)
print("List awal :", my_list)
print("List unik :", unique_list)
