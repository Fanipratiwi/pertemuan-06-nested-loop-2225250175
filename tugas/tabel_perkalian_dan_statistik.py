print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan nilai n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan nilai n: "))

# Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# Loop luar untuk baris
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam untuk kolom
    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        # Menghitung hasil perkalian yang genap
        if hasil % 2 == 0:
            count_genap += 1

    # Ditampilkan setelah satu baris selesai
    print(f"   | jumlah baris = {total_baris}")

# Hasil akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")