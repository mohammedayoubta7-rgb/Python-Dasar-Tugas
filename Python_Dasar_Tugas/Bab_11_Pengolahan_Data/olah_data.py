# Bab 11: Pengolahan Data Sederhana dengan modul csv
import csv
from pathlib import Path

# Cari CSV relatif terhadap lokasi file ini, jadi bisa dijalankan dari folder mana pun.
file_csv = Path(__file__).with_name("nilai.csv")
data = []

with file_csv.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(f"Jumlah data: {len(data)} baris")
print("Data pertama:", data[0])

nilai = [baris["nilai"] for baris in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata nilai: {rata:.1f}")

lulus = [baris["nama"] for baris in data if baris["nilai"] >= 75]
print("Mahasiswa lulus:", lulus)

tertinggi = max(data, key=lambda baris: baris["nilai"])
print(f"Nilai tertinggi: {tertinggi['nama']} ({tertinggi['nilai']})")

# Rekap rata-rata per kelas
rekap = {}
for baris in data:
    kelas = baris["kelas"]
    rekap.setdefault(kelas, []).append(baris["nilai"])

print(f"{'Kelas':<8}{'Jumlah':>8}{'Rata-rata':>12}")
for kelas, daftar_nilai in sorted(rekap.items()):
    rata_kelas = sum(daftar_nilai) / len(daftar_nilai)
    print(f"{kelas:<8}{len(daftar_nilai):>8}{rata_kelas:>12.1f}")
