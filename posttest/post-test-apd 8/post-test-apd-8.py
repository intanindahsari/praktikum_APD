from prettytable import PrettyTable
data_tiket_konser = {
    1 : {"nama konser":"NCT",
        "kategori tiket" :"reguler",
        "tempat" :"BSD",
        "harga tiket" : 1200000,
        "stock" : 17
        },
    2  : { "nama konser":"AESPA",
        "kategori tiket" :"vip",
        "tempat" :"GBK",
        "harga tiket" : 1500000,
        "stock" :10
        },                
    3 : { "nama konser":"TXT",
        "kategori tiket" :"vvip",
        "tempat" :"JIS",
        "harga tiket" :1900000,
        "stock" : 15 
        }
}  
data_pembelian_tiket = {}
judul_program = "PROGRAM PENJUALAN TIKET KONSER"
def sapaan_awal (judul_program):
    sapaan = " ************************ SELAMAT DATANG ************************* "
    print(sapaan)
    sapa = "                             di dalam                          "
    print(sapa)
    print(f"~~~~~~~~~~~~~~~~~~{judul_program}~~~~~~~~~~~~~~~~~~")

def hitung_total_harga (harga_tiket, jumlah_tiket_yang_ingin_di_pesan):
    harga = harga_tiket
    jumlah = jumlah_tiket_yang_ingin_di_pesan
    total = harga_tiket*jumlah_tiket_yang_ingin_di_pesan
    return total

def cek_stock_tiket (sisa_stock_tiket, jumlah_tiket_yang_ingin_di_pesan):
    if sisa_stock_tiket >= jumlah_tiket_yang_ingin_di_pesan:
        return True
    else:
        return False


def data_tiket_tersedia():
    table_konser = PrettyTable()
    table_konser.field_names = ["no", "nama konser", "kategori tiket", "tempat", "harga tiket", "stock"]
    data_tiket_baru = {}
    for nomor_tiket, tiket in data_tiket_konser.items():
        table_konser.add_row([
            nomor_tiket, 
            tiket["nama konser"], 
            tiket["kategori tiket"], 
            tiket["tempat"], 
            tiket["harga tiket"], 
            tiket["stock"]
        ])
    return table_konser

def tampilan_data_pembelian_tiket():
    table_tampilan = PrettyTable()
    table_tampilan.field_names = ["no", "nama konser", "jumlah tiket", "total harga"]
    for nomor_pembelian, beli in data_pembelian_tiket.items():
        total_harga_angka = beli['total harga'] 
        table_tampilan.add_row([
            nomor_pembelian,
            beli["nama konser"],
            beli["jumlah tiket"],
            total_harga_angka
        ])
    return table_tampilan
sapaan_awal(judul_program)
def jumlah_admin_terdaftar():
    jumlah = len(admin_terdaftar)
    return jumlah
admin_terdaftar = { 1: {"nama" : "intan",
                        "pw"   :  "2354"},
                    2 : {"nama" : "indah",
                        "pw" : "kuning"},
                    3 : {"nama" : "sari",
                        "pw" : "yellow"},
                    4 : {"nama" : "lily",
                        "pw" : "sedapmalam"}
}
print(f" total admin terdaftar: {jumlah_admin_terdaftar()}")
def menuadmin():
        print("~~~~~~~~~~~~~~~MENU ADMIN~~~~~~~~~~~~~~~")  
        print("OPSI 1 = MENAMBAHKAN DATA PENJUALAN TIKET")
        print("OPSI 2 = MENAMPILKAN DATA PENJUALAN TIKET")
        print("OPSI 3 = MENGUBAH DATA PENJUALAN TIKET")
        print("OPSI 4 = MENGHAPUS DATA PENJUALAN TIKET")
        print("OPSI 5 = KELUAR")
while True:
    pilihan = input("login/daftar/keluar : ")
    if pilihan == "login":
        login = admin_terdaftar
        if login == admin_terdaftar:
                    login_berhasil = True
                    nama = input("masukan username: ")
                    pw = input ("masukan password: ") 
                    for admin_key, admin_data in admin_terdaftar.items():
                        if admin_data ["nama"] == nama and admin_data ["pw"] == pw:
                            print("anda adalah admin")
                            print(140*"=")
                            login_berhasil = True
                            break
                    else:
                            print("login gagal, username/password yang anda masukan salah")
                            exit ()
        while True:
                    menuadmin()
                    try:
                        opsi = int(input("masukan opsi yang ingin  di pilih: "))
                    except ValueError:
                        print ("opsi yang ada masukan harus berupa angka tidak boleh string, coba lagi")
                    if opsi == 1:
                        print("OPSI 1 = MENAMBAHKAN DATA PENJUALAN TIKET")
                        print(" di opsi ini anda diminta untuk menambahkan data penjualan terbaru")
                        nama_konser_baru = input("masukan nama konser yang baru : ")
                        kategori_tiket_baru = input("masukan kategori tiket baru : ")
                        tempat_konser_baru = input("masukan tempat konser baru : ")
                        harga_tiket_baru = 0
                        stock_tiket_baru = 0
                        input_valid = True
                        try:
                            harga_tiket_baru = int(input("masukan harga tiket : "))
                            stock_tiket_baru = int(input("masukan stock tiket terbaru: "))
                        except ValueError: 
                            print("harga dan stock yang anda masukan itu harus berupa angka bukan string, coba lagii")
                            input_valid = False
                        if input_valid:
                            keys_baru = len(data_tiket_konser) + 1
                            data_tiket_konser[keys_baru] = {"nama konser": nama_konser_baru,
                                "kategori tiket" : kategori_tiket_baru,
                                "tempat" : tempat_konser_baru,
                                "harga tiket" : harga_tiket_baru,
                                "stock" : stock_tiket_baru
                            }
                            print("data tiket konser berhasil di tambahkan") 
                    elif opsi == 2:
                        print("OPSI 2 = MENAMPILKAN DATA PENJUALAN TIKET")
                        table_baru = data_tiket_tersedia()
                        print(table_baru)
                    elif opsi == 3:
                        print("OPSI 3 = MENGUBAH DATA PENJUALAN TIKET")
                        table_baru = data_tiket_tersedia()
                        print(table_baru)
                        nomor_tiket = int(input("masukan nomor tiket yang ingin di ubah: "))
                        while True:
                            if nomor_tiket in data_tiket_konser:
                                print("pilih data tiket yang ingin di ubah: ")
                                print("[1] = nama konser")
                                print("[2] = kategori tiket")
                                print("[3] = tempat")
                                print("[4] = harga tiket")
                                print("[5] = stock") 
                                try:
                                    pilihan = int(input("masukan pilihan data yang ingin di ubah: "))
                                except ValueError: 
                                    ("pilihan yang anda masukan harus berupa angka bukan string, coba lagi ya")
                            data_tiket_yang_di_ubah = ""
                            if pilihan == 1:
                                data_tiket_yang_di_ubah = "nama konser"
                            elif pilihan == 2:
                                data_tiket_yang_di_ubah = "kategori tiket"
                            elif pilihan == 3:
                                data_tiket_yang_di_ubah = "tempat"
                            elif pilihan == 4:
                                data_tiket_yang_di_ubah = "harga tiket"
                            elif pilihan == 5:
                                data_tiket_yang_di_ubah = "stock"
                            if data_tiket_yang_di_ubah != "":
                                data_tiket_baru = input(f"masukan data tiket baru sesuai sama pilihan yang di pilih '{data_tiket_yang_di_ubah}': ")
                                if data_tiket_yang_di_ubah == "harga tiket" or data_tiket_yang_di_ubah == "stock":
                                    try:
                                        data_tiket_baru = int(data_tiket_baru)
                                    except ValueError:
                                        print("harga dan stock yang di masukan harus berupa angka tidak boleh string, coba lagi")
                                data_tiket_konser[nomor_tiket][data_tiket_yang_di_ubah] = data_tiket_baru
                                pilihan = input("apakah masih ingin mengubah data? ya/tidak: ")
                                if pilihan == "ya":
                                    print("silahkan masukan data di pilihan yang ingin di ubah lagi sesuai dengan nomor tiket yang di pilih di awal")
                                elif pilihan == "tidak":
                                    print("selsai mengubah data tiket konser")
                                    break
                            else:
                                print("nomor tiket tidak ada, silahkan coba lagi")
                    elif opsi == 4:
                        print("OPSI 4 = MENGHAPUS DATA PENJUALAN TIKET")
                        table_baru = data_tiket_tersedia()
                        try:
                            nomor_tiket = int(input("masukan nomor tiket yang akan di hapus: "))
                        except ValueError:
                            print("nomor tiket yang anda masukan harus berupa angka yaa bukan string, coba lagi")
                        if nomor_tiket in data_tiket_konser:
                            del data_tiket_konser[nomor_tiket]
                            print ("data tiket berhasil di hapus")
                        else: 
                            print("nomor tiket tidak di temukan dalam daftar tiket")
                    elif opsi == 5:
                        print("berhasil keluar dari menu admin")
                        input("ketik enter untuk kembali ke halaman awal: ")
                        break
                    else: 
                        print("opsi tidak tersedia, silahkan pilih opsi 1-5")
                        continue
    elif pilihan == "daftar":
        nama_baru = input("masukan username baru : ")
        pw_baru = input ("masukan password baru : ")
        data_admin = False
        for admin_data_baru in admin_terdaftar.values():
            if admin_data_baru ["nama"] == nama_baru:
                data_admin = True
                print ("username/password sudah ada")
                exit ()
        else: 
            keys_baru = 5
            keys_baru = len(admin_terdaftar.keys()) + 1
            admin_terdaftar [keys_baru] = {"nama" : nama_baru, "pw" : pw_baru}
        print("anda adalah pengguna")
        print(140*"=")
        def menupengguna():
            print("~~~~~~~~~~~~~~MENU PENGGUNA~~~~~~~~~~~~~~~")
            print("OPSI 1 = UNTUK MELIHAT DATA TIKET KONSER")
            print("OPSI 2 = MENAMBAHKAN DATA PEMBELIAN TIKET")
            print("OPSI 3 = MENAMPILKAN PEMBELIAN TIKET")
            print("OPSI 4 = KELUAR")
        while True:
            menupengguna()
            try:
                opsi = int(input("masukan opsi yang ingin di pilih: "))
            except ValueError:
                print("opsi yang anda masukan harus berupa angka bukan string, coba lagi")
            if opsi == 1:
                print("OPSI 1 = UNTUK MELIHAT DATA TIKET KONSER")
                table_baru = data_tiket_tersedia()
                print(table_baru)
            elif opsi == 2:
                print("OPSI 2 = MENAMBAHKAN DATA PEMBELIAN TIKET")
                try:
                    nama_konser_yang_ingin_di_pesan = input("masukan nama konser yang ingin di pesan: ")
                    jumlah_tiket_yang_ingin_di_pesan = int(input("masukan jumlah tiket yang ingin di pesan: "))
                except ValueError:
                    print("ini harus sesuai nama konser itu string perhatikan juga huruf besar kecilnya, dan jumlah itu angka bukan string yaa, coba lagi")
                jumlah_tiket = 0
                nama_konser = ""
                input_valid = True
                if input_valid:
                    total_harga_pembelian = 0
                    pembelian_berhasil = False
                    nomor_tiket_terpilih = -1
                    for key, data_tiket in data_tiket_konser.items():
                        if data_tiket ["nama konser"] == nama_konser_yang_ingin_di_pesan:
                            nomor_tiket_terpilih = key
                            if cek_stock_tiket(data_tiket["stock"], jumlah_tiket_yang_ingin_di_pesan):
                                data_tiket_konser[nomor_tiket_terpilih]["stock"]-= jumlah_tiket_yang_ingin_di_pesan
                                total_harga_pembelian = hitung_total_harga(data_tiket["harga tiket"], jumlah_tiket_yang_ingin_di_pesan)
                                pembelian_berhasil = True
                                break
                            else:
                                print("stock tiket tidak cukup")
                    if pembelian_berhasil:
                        keys_baru = len(data_pembelian_tiket) + 1
                        data_pembelian_tiket[keys_baru] = { "nama konser" : nama_konser_yang_ingin_di_pesan,
                                                    "jumlah tiket" : jumlah_tiket_yang_ingin_di_pesan,
                                                    "total harga" : total_harga_pembelian 
                }
                        print("data pembelian telah di tambahkan")
                    
                else:
                    if nomor_tiket_terpilih == -1:
                        print(f"nama konser '{nama_konser_yang_ingin_di_pesan}' tidak di temukan, periksa tulisan nama konsernya huruf besar atau kecil")
            elif opsi == 3:
                print("OPSI 3 = MENAMPILKAN PEMBELIAN TIKET")
                table_pembelian = tampilan_data_pembelian_tiket()
                if len(data_pembelian_tiket) > 0:
                    print(table_pembelian)
                    total_pendapatan_semua = 0
                    for beli in data_pembelian_tiket.values():
                        total_pendapatan_semua += beli['total harga']
                else:
                    print("belum ada data pembelian")
            elif opsi == 4:
                print("kamu keluar dari menu pengguna")
                input("tekan entar untuk kembali ke halaman awal")
                break
            else:
                print("opsi tidak tersedia, silahkan masukan opsi 1-4")
                continue
    elif pilihan == "keluar":
        print("anda keluar dari program")
        print("bye bye, jumpa lagi")
        exit()
    else:
        print("login/daftar/keluar, gagal")
        print("coba lagii")
        continue











