# Bab 07: List, Tuple, Set, dan Dictionary

# List: berurutan, bisa diubah, dan boleh memiliki duplikat
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85
print("List:", nilai)
print("Item terakhir dan jumlah item:", nilai[-1], len(nilai))
print("Urutan nilai:", sorted(nilai))

# Tuple: berurutan, tetapi tidak bisa diubah
titik = (3, 7)
warna = (255, 128, 0)
x, y = titik
print(f"Koordinat: x={x}, y={y}")
print("Warna pertama dan jumlah komponen:", warna[0], len(warna))

# Set: kumpulan nilai unik
angka = {1, 2, 2, 3, 3, 3}
print("Set angka:", angka)
ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi", "Dodi"}
print("Gabungan:", ipa | ips)
print("Irisan:", ipa & ips)
print("Selisih:", ipa - ips)

# Dictionary: pasangan key-value
siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print("Nama:", siswa["nama"])
print("Hobi:", siswa.get("hobi", "-"))
for key, value in siswa.items():
    print(f"{key}: {value}")
