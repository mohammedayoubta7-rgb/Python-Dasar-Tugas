# Bab 11: Cara ringkas mengolah CSV menggunakan pandas
# Instalasi terlebih dahulu: python -m pip install -r requirements.txt
import pandas as pd
from pathlib import Path

file_csv = Path(__file__).with_name("nilai.csv")
df = pd.read_csv(file_csv)

print("Data:")
print(df)
print("\nRata-rata nilai per kelas:")
print(df.groupby("kelas")["nilai"].mean())
print("\nMahasiswa dengan nilai minimal 75:")
print(df[df["nilai"] >= 75]["nama"].tolist())
print("\nBaris dengan nilai tertinggi:")
print(df.sort_values("nilai").tail(1))
