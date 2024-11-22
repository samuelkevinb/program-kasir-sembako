class Produk:
    def __init__(self, nama, harga, kategori):
        self.nama = nama
        self.harga = harga
        self.kategori = kategori

    def __str__(self):
        return f"{self.nama} - Rp{self.harga:,} ({self.kategori})"


class KeranjangBelanja:
    def __init__(self):
        self.produk_list = []

    def tambah_produk(self, produk, jumlah):
        self.produk_list.append((produk, jumlah))

    def batalkan_pesanan(self, produk_index):
        if 0 <= produk_index < len(self.produk_list):
            produk_dihapus = self.produk_list.pop(produk_index)
            print(f"\nProduk {produk_dihapus[0].nama} berhasil dibatalkan dari keranjang.")
        else:
            print("\nNomor produk yang dimasukkan tidak valid.")

    def tampilkan_keranjang(self):
        if not self.produk_list:
            print("Keranjang belanja Anda kosong.")
        else:
            print("\nKeranjang Belanja:")
            print(f"{'No':<3} {'Nama Produk':<25} {'Jumlah':<7} {'Harga Satuan':<15} {'Subtotal':<15}")
            print("=" * 65)
            total_harga = 0
            for idx, (produk, jumlah) in enumerate(self.produk_list, start=1):
                subtotal = produk.harga * jumlah
                total_harga += subtotal
                print(
                    f"{idx:<3} {produk.nama:<25} {jumlah:<7} Rp{produk.harga:<14,} Rp{subtotal:<14,}"
                )
            print("=" * 65)
            print(f"{'Total Harga':<48} Rp{total_harga:<14,}")
            return total_harga

    def hitung_total(self):
        total = 0
        for produk, jumlah in self.produk_list:
            total += produk.harga * jumlah
        return total


class Pelanggan:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
        self.keranjang = KeranjangBelanja()

    def tambah_ke_keranjang(self, produk, jumlah):
        self.keranjang.tambah_produk(produk, jumlah)

    def tampilkan_keranjang(self):
        self.keranjang.tampilkan_keranjang()
        if self.keranjang.produk_list:
            self.batalkan_pesanan()

    def batalkan_pesanan(self):
        if not self.keranjang.produk_list:
            return
        pilihan_batal = input("\nIngin membatalkan produk di keranjang? (y/n): ").lower()
        if pilihan_batal == 'y':
            try:
                produk_index = int(input("\nMasukkan nomor produk yang ingin dibatalkan: ")) - 1
                self.keranjang.batalkan_pesanan(produk_index)
            except ValueError:
                print("Masukkan nomor produk yang valid.")
        elif pilihan_batal == 'n':
            print("\nPembatalan pesanan dibatalkan.")
        else:
            print("Pilihan tidak valid.")

    def bayar_tunai(self):
        total_harga = self.keranjang.hitung_total()
        if total_harga == 0:
            print("Keranjang Anda kosong. Silakan tambahkan produk terlebih dahulu.")
            return

        print("\nRincian Pembayaran:")
        self.keranjang.tampilkan_keranjang()
        uang_tunai = float(input("\nMasukkan jumlah uang tunai: Rp "))
        if uang_tunai >= total_harga:
            kembalian = uang_tunai - total_harga
            print(f"\nPembayaran berhasil! Kembalian Anda: Rp{kembalian:,}")
            self.keranjang = KeranjangBelanja()  # Reset keranjang setelah pembayaran
        else:
            print("\nUang tunai tidak cukup. Pembayaran dibatalkan.")

    def bayar_debit(self):
        total_harga = self.keranjang.hitung_total()
        if total_harga == 0:
            print("Keranjang Anda kosong. Silakan tambahkan produk terlebih dahulu.")
            return

        print("\nPilih Bank:")
        print("1. BCA")
        print("2. Mandiri")
        pilihan_bank = input("Pilih bank (1-2): ")
        if pilihan_bank in ['1', '2']:
            print("\nRincian Pembayaran (Debit):")
            self.keranjang.tampilkan_keranjang()
            print(f"\nPembayaran melalui {'BCA' if pilihan_bank == '1' else 'Mandiri'} berhasil.")
            self.keranjang = KeranjangBelanja()  # Reset keranjang setelah pembayaran
        else:
            print("Pilihan bank tidak valid. Pembayaran dibatalkan.")


# Daftar Produk di Toko
produk_toko = [
    # Food
    Produk("Beras", 15000, "Food"),
    Produk("Minyak Goreng", 20000, "Food"),
    Produk("Gula Pasir", 12000, "Food"),
    Produk("Tepung", 10000, "Food"),
    Produk("Telur", 24000, "Food"),
    Produk("Susu Full Cream", 25000, "Food"),
    Produk("Indomie Goreng (5 pack)", 15000, "Food"),
    Produk("Garam", 5000, "Food"),
    Produk("Air Mineral", 5000, "Food"),
    Produk("Makanan Kalengan", 8500, "Food"),
    # Non-Food
    Produk("Shampo", 15000, "Non-Food"),
    Produk("Sabun Mandi", 5000, "Non-Food"),
    Produk("Sabun Cuci Baju", 10000, "Non-Food"),
    Produk("Sabun Cuci Piring", 5000, "Non-Food"),
    Produk("Pasta Gigi", 8000, "Non-Food"),
    Produk("Sikat Gigi", 12000, "Non-Food"),
    Produk("Karbol", 8000, "Non-Food"),
    Produk("Batu Baterai", 20000, "Non-Food"),
    Produk("Kapas", 7500, "Non-Food"),
    Produk("Pembalut", 12000, "Non-Food"),
]


# Fungsi untuk menampilkan produk berdasarkan kategori
def tampilkan_produk(kategori=None):
    if kategori:
        print(f"\nDaftar Produk ({kategori}):")
        for index, produk in enumerate(produk_toko, start=1):
            if produk.kategori.lower() == kategori.lower():
                print(f"{index}. {produk}")
    else:
        print("\nDaftar Produk di Toko:")
        for index, produk in enumerate(produk_toko, start=1):
            print(f"{index}. {produk}")


# Menu Toko Sembako
def menu_toko():
    pelanggan = Pelanggan("Andi", 200000)
    while True:
        print("\nMenu Toko Sembako:")
        print("1. Tampilkan Semua Produk")
        print("2. Tambah Produk ke Keranjang")
        print("3. Lihat Keranjang Belanja")
        print("4. Bayar")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tampilkan_produk()
        elif pilihan == '2':
            print("\nKategori:")
            print("1. Food")
            print("2. Non-Food")
            kategori_pilihan = input("Pilih kategori (1-2): ")
            if kategori_pilihan == '1':
                kategori = "Food"
            elif kategori_pilihan == '2':
                kategori = "Non-Food"
            else:
                print("Pilihan kategori tidak valid.")
                continue

            while True:
                tampilkan_produk(kategori)
                try:
                    produk_id = int(input("Masukkan nomor produk yang ingin dibeli: ")) - 1
                    if 0 <= produk_id < len(produk_toko) and produk_toko[produk_id].kategori.lower() == kategori.lower():
                        jumlah = int(input("Masukkan jumlah produk: "))
                        pelanggan.tambah_ke_keranjang(produk_toko[produk_id], jumlah)
                        print(f"\nProduk {produk_toko[produk_id].nama} berhasil ditambahkan ke keranjang.")
                        break
                    else:
                        print("\nNomor produk tersebut tidak ada dalam kategori. Silakan coba lagi.")
                except ValueError:
                    print("\nMasukkan nomor produk yang valid.")
        elif pilihan == '3':
            pelanggan.tampilkan_keranjang()
        elif pilihan == '4':
            print("\nMetode Pembayaran:")
            print("1. Tunai")
            print("2. Debit")
            metode = input("Pilih metode pembayaran (1-2): ")
            if metode == '1':
                pelanggan.bayar_tunai()
            elif metode == '2':
                pelanggan.bayar_debit()
            else:
                print("Metode pembayaran tidak valid.")
        elif pilihan == '5':
            print("Terima kasih telah berbelanja!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Jalankan program
menu_toko()
