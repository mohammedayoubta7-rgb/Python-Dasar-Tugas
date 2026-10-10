# Bab 08: Function

def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas

print(hitung_luas(5, 3))
print(hitung_luas(10, 2))

# Parameter default dan keyword argument
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

# *args menerima banyak argumen dalam bentuk tuple
def total(*angka):
    return sum(angka)

print("Total:", total(1, 2, 3, 4))

# Lambda adalah function sederhana satu baris
kuadrat = lambda x: x ** 2
print("Kuadrat 4:", kuadrat(4))

siswa = [("Ani", 80), ("Budi", 95)]
print("Nilai tertinggi:", max(siswa, key=lambda s: s[1]))

# Scope: variabel lokal berbeda dari variabel global
x = "global"
def tes():
    x = "lokal"
    print("Di dalam function:", x)

tes()
print("Di luar function:", x)
