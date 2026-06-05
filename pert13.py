# 1. Membuat tuple dan tampilkan
my_tuple = (1, 2, 3)
print(my_tuple)

# 2. Menggunakan tuple
tuple_angka = (1, 20, 300, 4000)
print(tuple_angka[0])
print(tuple_angka[2])
print(tuple_angka[-1])
print(tuple_angka[1:3])

for elemen in tuple_angka:
    print(elemen)

# 3. Fungsi len pada tuple
angka = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(angka))

# 4. Operasi pertambahan dan perkalian tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
print(tuple1 * 3)

# 5. Operasi in dan not in pada tuple
tuple_huruf = ('a', 'b', 'c', 'd')
print('a' in tuple_huruf)
print('e' not in tuple_huruf)

# 6. Membuat dictionary kosong dan menampilkannya
my_dict = {}
print(my_dict)

# 7. Membuat dictionary dengan data dan menampilkannya
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
print(kamus)

# 8. Mengakses elemen dictionary menggunakan key
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
print(kamus["cat"])
print(kamus["dog"])

# 9. Menggunakan perulangan for untuk menampilkan key dalam dictionary
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
for key in kamus:
    print(key)

# 10. Menggunakan perulangan for untuk menampilkan key dan value menggunakan method items()
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
for key, value in kamus.items():
    print(key, "artinya", value)

# 11. Mengupdate nilai/value dari key tertentu
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
kamus["cat"] = "kucing lucu"
print(kamus)

# 12. Menambahkan pasangan key dan value baru ke dalam dictionary
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
kamus["bird"] = "burung"
print(kamus)

# 13. Menghapus elemen dictionary menggunakan keyword del
kamus = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
del kamus["dog"]
print(kamus)

# 14. Menangani exception dengan try dan except
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil pembagian:", hasil)
except Exception as e:
    print("Terjadi kesalahan:", e)

# 15. Menangani multiple exception
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
    print("Hasil:", hasil)
except (ValueError, ZeroDivisionError):
    print("Terjadi kesalahan: input tidak valid atau pembagian dengan nol")
