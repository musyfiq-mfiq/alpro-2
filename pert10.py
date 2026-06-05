# 1. List Comprehensions
pangkat = [x**2 for x in range(10)]
print(pangkat)

dua_pangkat = [2**i for i in range(8)]
print(dua_pangkat)

ganjil = [x for x in pangkat if x % 2 != 0]
print(ganjil)

# 2. Array 2 Dimensi
kosong = "_"
benteng = 'B'
kuda = 'K'

papan_catur = [[kosong for i in range(8)] for j in range(8)]

papan_catur[2][6] = benteng
papan_catur[6][2] = benteng
papan_catur[1][7] = benteng
papan_catur[7][6] = benteng
papan_catur[4][1] = kuda

for baris in papan_catur:
    print(baris)

# 3. List Multidimensi
musyfiq = [
    ["ganteng", ["imut", "pintar"], "jujur"],
    ["rajin", "hemat", ["amanah", "baik"]],
    ["sopan", ["suka_membantu", "rendah_hati"]]
]

print('musyfiq orang yang:', musyfiq[1][2][0], "dan", musyfiq[2][1][1])

# 4. Fungsi Berparameter
def kali(a, b):
    return a * b

hasil = kali(4, 5)
print("Hasil perkalian:", hasil)

# 5. Kuis 1
angka = [i for i in range(1, 11)]
genap_kali_tiga = [x * 3 for x in angka if x % 2 == 0]
print(genap_kali_tiga)

# 6. Kuis 2
array = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]

for baris in array:
    for kolom in baris:
        print(kolom, end=" ")
    print()

# 7. Kuis 3
data = [[2, 4], [6, 8], [10, 12]]
flatten = [angka for baris in data for angka in baris]
print(flatten)

# 8. Slice 4 (Fungsi Luas Persegi Panjang)
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = luas_persegi_panjang(8, 5)
print("Luas persegi panjang:", hasil)
