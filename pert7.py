# 1
angka = [10, 5, 7, 2, 1]
print("isi dari list awal", angka)
angka[0] = 111
print("isi dari list baru", angka)
angka[1] = angka[4]
print("isi dari list sekarang", angka)

# 2
angka = [9, 8, 7, 6, 5]
print(angka[3])
print(angka)

# 3
angka = [10, 5, 7, 2, 1]
print("Isi list:", angka)
print("\nPanjang list:", len(angka))

# 4
angka = [2, 3, 4, 5, 6]
del angka[1]
print(len(angka))
print(angka)

# 5
numbers = [111, 4, 7, 6, 1]
print(numbers[-1])
print(numbers[-2])

# 6
topi_list = [1, 2, 3, 4, 5]
topi_list[len(topi_list) // 2] = int(input("Masukkan angka integer: "))
topi_list.pop()
print("Panjang list:", len(topi_list))
print(topi_list)

# 7
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

angka.append(4)
print(len(angka))
print(angka)

angka.insert(0, 222)
print(len(angka))
print(angka)
angka[3] = 333
print(len(angka))
print(angka)

# 8
my_list = []
for i in range(5):
    my_list.append(i + 1)
print(my_list)

# 9
my_list = []
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)

# 10
variable_1 = 1
variable_2 = 2
variable_2 = variable_1
variable_1 = variable_2
print(variable_1)
print(variable_2)

# 11
variable_1 = 1
variable_2 = 2
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
print(variable_1)
print(variable_2)

# 12
my_List = [10, 1, 8, 3, 5]
my_List[0], my_List[4] = my_List[4], my_List[0]
my_List[1], my_List[3] = my_List[3], my_List[1]
print(my_List)
length = len(my_List)
for i in range(length // 2):
    my_List[i], my_List[length - i - 1] = my_List[length - i - 1], my_List[i]
print(my_List)

# 13
exo = []
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_baru:
    exo.append(anggota)
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
exo.insert(-2, "Xiumin")
print(exo)
print("Jumlah anggota:", len(exo))
