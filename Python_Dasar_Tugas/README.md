# Tugas Praktik Python Dasar — 11 Bab

Proyek ini berisi latihan coding berdasarkan materi dalam PDF **Python Dasar.pdf**, dari Bab 01 sampai Bab 11.

## Isi proyek
- `Bab_01_Pengenalan_Python/pengenalan.py`
- `Bab_02_Variabel_Tipe_Data/variabel_tipe_data.py`
- `Bab_03_Input_Output/input_output.py`
- `Bab_04_Operator/operator.py`
- `Bab_05_Percabangan/percabangan.py`
- `Bab_06_Perulangan/perulangan.py`
- `Bab_07_Koleksi_Data/koleksi_data.py`
- `Bab_08_Function/function.py`
- `Bab_09_Error_Handling/error_handling.py`
- `Bab_10_Module_Package/main.py` dan modul `utils/`
- `Bab_11_Pengolahan_Data/olah_data.py`, `nilai.csv`, dan `pakai_pandas.py`

## Cara menjalankan
1. Ekstrak file ZIP.
2. Buka folder `Python_Dasar_Tugas` di VS Code.
3. Buka terminal di VS Code.
4. Jalankan satu bab, misalnya:
   ```bash
   python Bab_01_Pengenalan_Python/pengenalan.py
   ```
5. Untuk Bab 03, program akan meminta nama dan umur. Masukkan jawaban saat diminta.
6. Untuk Bab 11 versi CSV biasa:
   ```bash
   python Bab_11_Pengolahan_Data/olah_data.py
   ```
7. Untuk Bab 11 versi pandas, instal paket satu kali:
   ```bash
   python -m pip install -r requirements.txt
   ```
   Lalu jalankan:
   ```bash
   python Bab_11_Pengolahan_Data/pakai_pandas.py
   ```

> Jika perintah `python` tidak berfungsi di Windows, coba ganti dengan `py`.

## Catatan penting
- Setiap bab dijalankan secara terpisah agar mudah dipelajari.
- Bab 10 menggunakan modul buatan sendiri dalam folder `utils`.
- Bab 11 membaca file `nilai.csv` yang disertakan. Jalankan perintah dari folder utama proyek agar jalur file CSV ditemukan dengan benar.
- `pandas` hanya diperlukan untuk menjalankan `pakai_pandas.py`. Bab lain menggunakan Python standar.

## Ringkasan materi
1. Pengenalan Python: `print`, komentar, indentasi.
2. Variabel dan tipe data: `int`, `float`, `str`, `bool`, casting, string.
3. Input dan output: `input`, `print`, f-string.
4. Operator: aritmatika, perbandingan, logika, penugasan, keanggotaan.
5. Percabangan: `if`, `elif`, `else`, nested if, ternary, `match-case` (contoh match-case memakai Python 3.10+).
6. Perulangan: `for`, `range`, `while`, `break`, `continue`, `pass`.
7. Koleksi data: list, tuple, set, dictionary.
8. Function: parameter, `return`, default argument, `*args`, `lambda`, scope.
9. Error handling: `try`, `except`, `else`, `finally`, `raise`.
10. Module dan package: `import`, modul sendiri, `pip`, virtual environment.
11. Pengolahan data: CSV, filter, rata-rata, nilai tertinggi, rekap per kelas, pandas.

## Pengumpulan tugas
Unggah folder proyek ini ke Google Drive atau GitHub, lalu kirim tautan yang dapat diakses dosen melalui e-learning. Pastikan izin Google Drive disetel agar dosen dapat melihat atau mengunduh file.
