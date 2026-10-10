def rata_rata(data):
    """Mengembalikan rata-rata dari kumpulan angka."""
    if not data:
        return 0
    return sum(data) / len(data)
