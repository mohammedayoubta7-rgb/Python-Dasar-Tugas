# Bab 10: Menggunakan module standar dan module buatan sendiri
import math
from random import randint
import datetime as dt

from utils.hitung import rata_rata
from utils.teks import salam

print("Akar kuadrat 16:", math.sqrt(16))
print("Nilai pi:", math.pi)
print("Contoh angka acak dadu:", randint(1, 6))
print("Tahun sekarang:", dt.date.today().year)

nilai = [80, 90, 70]
print("Rata-rata nilai:", rata_rata(nilai))
print(salam("Mahasiswa"))
