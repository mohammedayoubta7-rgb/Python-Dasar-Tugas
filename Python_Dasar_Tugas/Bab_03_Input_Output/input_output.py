# Bab 03: Input dan Output
# Program ini meminta pengguna memasukkan nama dan umur.

print("Halo", "Dunia")
print("A", "B", "C", sep="-")
print("Loading", end="...")
print("selesai")

harga = 15000 / 7
print(f"Harga: Rp{harga:.2f}")
print(f"Total: {1500000:,}")

nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))

tahun_depan = umur + 1
print(f"Halo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")
