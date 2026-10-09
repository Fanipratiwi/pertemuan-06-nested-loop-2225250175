## Identitas
Nama: Fani Pratiwi Nur Indah
NIM: 2225250175
Kelas: 3B

## Tujuan
Mempelajari nested loop, pola, akumulasi, dan pencacahan
menggunakan bahasa pemrograman Python.

## Struktur Program
1. Latihan 1: Pasangan indeks.
2. Latihan 2: Pola segitiga.
3. Latihan 3: Jumlah per baris.
4. Latihan 4: Menghitung pasangan.
5. Tugas 3: Tabel perkalian dan statistik.

## Cara Menjalankan
Jalankan setiap file Python melalui terminal VS Code.

Contoh:
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
1. Memasukkan bilangan bulat positif n.
2. Memvalidasi input menggunakan while.
3. Menginisialisasi total_semua dan count_genap.
4. Menggunakan nested loop untuk membuat tabel perkalian.
5. Menghitung jumlah setiap baris dan jumlah keseluruhan.
6. Menghitung banyak hasil perkalian yang genap.
7. Menampilkan seluruh hasil perhitungan.

## Hasil Pengujian

| Input n | Total Semua | Banyak Hasil Genap |
|---|---:|---:|
| 1 | 1 | 0 |
| 2 | 9 | 3 |
| 3 | 36 | 5 |

Status: Sesuai hasil yang diharapkan.

## Analisis Efisiensi
Untuk input n positif, loop luar berjalan n kali
dan loop dalam berjalan n kali pada setiap iterasi
loop luar. Dengan demikian, badan loop dalam
berjalan sebanyak n x n atau n² kali.

## Refleksi
total_baris diinisialisasi di dalam loop luar agar
jumlah dimulai kembali dari nol pada setiap baris.
Sementara itu, total_semua diinisialisasi sebelum
kedua loop agar jumlah seluruh baris tetap terkumpul.

Kesalahan yang perlu dihindari adalah salah indentasi
dan menempatkan inisialisasi akumulator pada lokasi
yang tidak sesuai.

## Sumber
Bahan Ajar Algoritma dan Pemrograman,
Pertemuan 6: Nested Loop, Pola, Akumulasi,
dan Pencacahan dalam Python di VS Code.