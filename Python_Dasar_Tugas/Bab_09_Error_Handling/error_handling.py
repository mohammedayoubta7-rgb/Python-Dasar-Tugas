# Bab 09: Error Handling

# try-except-else-finally
try:
    teks = input("Masukkan angka untuk menghitung 100 dibagi angka tersebut: ")
    angka = int(teks)
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Proses selesai.")

# raise: membuat error secara sengaja jika data tidak valid
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    print("Umur:", set_umur(20))
    set_umur(-5)
except ValueError as error:
    print(f"Error: {error}")
