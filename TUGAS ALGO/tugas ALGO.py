import databarang

stok = [
    {"nama": "Gelas", "jumlah": 20},
    {"nama": "Piring", "jumlah":60},
    {"nama": "Mangkok", "jumlah": 40},
]

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama_benda = input("Masukan nama barang: ")
            jumlah_benda = int(input("Masukan jumlah barang: "))
            tambah = databarang.tambah_data_barang(stok, nama_benda, jumlah_benda)
            print("Data berhasil ditambah")
            
        elif pilihan == "2":
            indeks = int(input("Masukkan indeks data yang ingin diedit: "))
            nama_baru = input("Masukkan nama baru: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            sukses = databarang.edit_data(stok, indeks, nama_baru, jumlah_baru)
            if sukses:
                print("Data berhasil diedit.")
            else:
                print("Indeks tidak valid.")
        elif pilihan == "3":
            indeks = int(input("Masukkan indeks data yang ingin dihapus: "))
            berhasil = databarang.hapus_data(stok, indeks)
            if berhasil:
                print("Data berhasil dihapus")
            else:
                print("Indeks tidak valid")
        elif pilihan == "4":
            nama = input("Masukkan nama barang yang dicari = ")
            hasil = databarang.cari_data(stok, nama)
            if hasil:
                print(f"Ditemukan: Nama = {hasil['nama']}, Jumlah = {hasil['jumlah']}")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == "5":
            databarang.tampilkan_data(stok)
        elif pilihan == "6":
            jumlah_data = databarang.hitung_jumlah_data(stok)
            print(f"Jumlah data yang tersimpan = {jumlah_data}")
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()