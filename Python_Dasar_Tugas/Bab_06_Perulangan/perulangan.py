# Bab 06: Perulangan

# for dan range
for i in range(1, 4):
    print(f"Putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item.upper())

print("Angka genap:", list(range(0, 10, 2)))

# while: kondisi harus berubah agar loop berhenti
hitung = 3
while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung -= 1
print("Meluncur!")

# continue melewati putaran tertentu; break menghentikan loop
for n in range(1, 10):
    if n == 3:
        continue
    if n == 6:
        break
    print(n)

# pass adalah placeholder yang tidak melakukan apa-apa
for i in range(3):
    pass
print("Contoh pass selesai")
