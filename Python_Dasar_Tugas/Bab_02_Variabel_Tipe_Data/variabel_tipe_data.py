# Bab 02: Variabel dan Tipe Data

nama = "Budi"        # str: teks
umur = 20            # int: bilangan bulat
tinggi = 170.5       # float: bilangan desimal
aktif = True         # bool: benar/salah

umur = umur + 1
x, y, z = 1, 2, 3    # multiple assignment

print("Nama:", nama)
print("Umur tahun depan:", umur)
print("Tinggi:", tinggi)
print("Aktif:", aktif)
print("Tipe nama:", type(nama))
print("Tipe umur:", type(umur))
print("Jumlah x + y + z:", x + y + z)

# Casting / konversi tipe
angka = int("25")
harga = float("12500.75")
print("Angka + 5:", angka + 5)
print("Tipe harga:", type(harga))
print("Umur sebagai teks: " + str(umur))
print("Nilai bool:", bool(0), bool("hai"))

# String: panjang, huruf besar, slicing, split, f-string
judul = "Python Dasar"
print("Panjang judul:", len(judul))
print(judul.upper())
print("Potongan teks:", judul[0:6])
print("Hasil split:", judul.split(" "))
bab = 2
print(f"Belajar {judul} bab {bab}")
