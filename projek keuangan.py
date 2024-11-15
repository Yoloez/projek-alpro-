import calendar
import os

# Membuat folder "pengeluaran" jika belum ada di direktori kerja
if not os.path.exists("pengeluaran"):
    os.makedirs("pengeluaran")

def main():
    while True:
        print('''Pilih menu:
1. Lihat pengeluaran
2. Catat pengeluaran
''')
        kegiatan = int(input("Masukkan pilihan kegiatan: "))
        if kegiatan == 1:
            lihat_pengeluaran()
        elif kegiatan == 2:
            catat_pengeluaran()

def lihat_pengeluaran():
    print('''Pilih jenis tampilan pengeluaran:
1. Total pengeluaran bulanan
2. Pengeluaran per tanggal
''')
    pilihan = int(input("Masukkan pilihan: "))
    tahun = input("Masukkan tahun (e.g., 2023): ")
    bulan = input("Masukkan bulan (1-12): ")
    file_name = os.path.join("pengeluaran", f"{tahun}_{bulan}.txt")

    # Cek apakah file untuk bulan tersebut ada
    if not os.path.exists(file_name):
        print(f"Data untuk bulan {bulan}/{tahun} tidak ditemukan.")
        return

    if pilihan == 1:
        total_pengeluaran_bulanan(file_name)
    elif pilihan == 2:
        tanggal = input("Masukkan tanggal (DD): ")
        pengeluaran_per_tanggal(file_name, tanggal)

def total_pengeluaran_bulanan(file_name):
    total = 0
    # Baca file dan hitung total pengeluaran bulanan
    with open(file_name, 'r') as file:
        next(file)  # Lewati header
        for line in file:
            data = line.strip().split('\t')
            total += float(data[2])  # Harga barang

    print(f"Total pengeluaran bulan ini adalah: {total}")

def pengeluaran_per_tanggal(file_name, tanggal):
    total_harian = 0
    found = False
    print(f"Pengeluaran pada tanggal {tanggal}:")
    # Baca file dan cari pengeluaran sesuai tanggal
    with open(file_name, 'r') as file:
        next(file)  # Lewati header
        for line in file:
            data = line.strip().split('\t')
            if data[0] == tanggal:
                print(f"Nama Barang: {data[1]}, Harga Barang: {data[2]}")
                total_harian += float(data[2])
                found = True
    if found:
        print(f"Total pengeluaran pada tanggal {tanggal}: {total_harian}")
    else:
        print(f"Tidak ada data pengeluaran pada tanggal {tanggal}.")

def catat_pengeluaran():
    print("Pilih bulan dan tahun untuk melihat kalender dan mencatat pengeluaran:")
    tahun = int(input("Masukkan tahun (e.g., 2023): "))
    bulan = int(input("Masukkan bulan (1-12): "))

    # Tampilkan kalender bulan yang dipilih
    print("\n", calendar.month(tahun, bulan))

    tanggal = input("Masukkan tanggal (DD): ")
    file_name = os.path.join("pengeluaran", f"{tahun}_{bulan}.txt")

    # Cek apakah file untuk bulan tersebut sudah ada
    if not os.path.exists(file_name):
        print(f"File untuk bulan {bulan}/{tahun} belum ada, membuat file baru...")
        with open(file_name, 'w') as file:
            file.write("Tanggal\tNama Barang\tHarga Barang\tTotal Transaksi\n")
    else:
        print(f"File untuk bulan {bulan}/{tahun} sudah ada.")

    # Masukkan jumlah barang yang dibeli
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli hari ini: "))

    total_harian = 0
    transaksi = []
    for i in range(jumlah_barang):
        nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
        harga_barang = float(input(f"Masukkan harga barang '{nama_barang}': "))
        transaksi.append((tanggal, nama_barang, harga_barang))
        total_harian += harga_barang

    # Tulis transaksi ke file
    with open(file_name, 'a') as file:
        for entry in transaksi:
            file.write(f"{entry[0]}\t{entry[1]}\t{entry[2]}\t{total_harian}\n")
    
    print("Pengeluaran telah dicatat.")

if __name__ == "__main__":
    main()
