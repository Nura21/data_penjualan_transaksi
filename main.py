import csv

# TOTAL PENJUALAN
total_penjualan = 0

# Baca file CSV
with open('data_penjualan_transaksi.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        jumlah_produk = int(row['jumlah_produk'])
        total_penjualan += jumlah_produk

# Cetak total penjualan
print("Total Penjualan: ", total_penjualan, "\n\n")



# TRANSAKSI PENJUALAN TERTINGGI
penjualan_tertinggi = 0
transaksi_tertinggi = None

# Baca file CSV
with open('data_penjualan_transaksi.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Iterasi setiap baris transaksi
    for row in reader:
        jumlah_produk = int(row['jumlah_produk'])
        
        # Cek jika jumlah penjualan saat ini lebih besar dari yang tertinggi sejauh ini
        if jumlah_produk > penjualan_tertinggi:
            penjualan_tertinggi = jumlah_produk
            transaksi_tertinggi = row

# Cetak transaksi dengan penjualan tertinggi
print("Transaksi dengan Penjualan Tertinggi:")
print(transaksi_tertinggi, "\n\n")



# JUMLAH TRANSAKSI
jumlah_transaksi = 0

# Baca file CSV
with open('data_penjualan_transaksi.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Iterasi setiap baris transaksi
    for row in reader:
        jumlah_transaksi += 1

# Karena baris pertama mungkin berisi header, kurangi satu dari jumlah transaksi
jumlah_transaksi -= 1

# Cetak jumlah transaksi
print("Jumlah Transaksi:", jumlah_transaksi, "\n\n")



# DAFTAR PRODUK YANG TERJUAL
daftar_produk = []

# Baca file CSV
with open('data_penjualan_transaksi.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Iterasi setiap baris transaksi
    for row in reader:
        produk = row['nama_produk']
        
        # Tambahkan produk ke daftar jika belum ada di dalamnya
        if produk not in daftar_produk:
            daftar_produk.append(produk)

# Cetak daftar produk yang terjual
print("Daftar Produk yang Terjual:")
for produk in daftar_produk:
    print(produk)