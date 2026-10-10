# Bab 05: Percabangan

nilai = 80
if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Ayo remedial dulu")
print("Program selesai")

nilai = 78
if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"
print(f"Nilai {nilai} -> grade {grade}")

# Nested if (if di dalam if)
umur, punya_ktp = 20, True
if umur >= 17:
    if punya_ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")
else:
    print("Belum cukup umur")

# Ternary: if dalam satu baris
umur = 16
status = "dewasa" if umur >= 17 else "anak"
print(status)

# match-case tersedia pada Python 3.10 atau lebih baru
hari = "sabtu"
match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")
