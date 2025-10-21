from tabulate import tabulate
print(" ********** selamat datang ********** ")
print("~~~~~~~~~~~PROGRAM PENJUALAN TIKET KONSER~~~~~~~~~~")
admin_terdaftar = { 1: {"nama" : "intan",
                        "pw"   :  "2354"},
                    2 : {"nama" : "indah",
                        "pw" : "kuning"},
                    3 : {"nama" : "sari",
                        "pw" : "yellow"},
                    4 : {"nama" : "lily",
                        "pw" : "sedapmalam"}
}
data_pembelian_tiket = {}
data_tiket_konser = {
    1 : {"nama konser":"NCT",
        "kategori tiket" :"reguler",
        "tempat" :"BSD",
        "harga tiket" :"1200000",
        "stock" :"17"
        },

    2  : { "nama konser":"AESPA",
        "kategori tiket" :"vip",
        "tempat" :"GBK",
        "harga tiket" :"1500000",
        "stock" :"10"
        },                

    3 : { "nama konser":"TXT",
        "kategori tiket" :"vvip",
        "tempat" :"JIS",
        "harga tiket" :"1900000",
        "stock" :"15" 
        }
}  
pilihan = input("login/daftar : ")
if pilihan == "login":
                login_berhasil = False
                nama = input("masukan username: ")
                pw = input ("masukan password: ")
                for admin_key, admin_data in admin_terdaftar.items():
                    if admin_data ["nama"] == nama and admin_data ["pw"] == pw:
                        print("login berhasil")
                        print(140*"=")
                        login_berhasil = True
                        break
                else:
                    print("login gagal, username/password yang anda masukan salah")
                    exit ()
elif pilihan == "daftar":
                    nama_baru = input("masukan nama baru : ")
                    pw_baru = input ("masukan pw baru : ")
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
                        print("pendaftaran berhasil")
                        
while True:
    status = input("admin/pengguna :  ")
    if status == "admin":
        login_berhasil = True
        if login_berhasil == True:
            while True:
                print("~~~~~~~~~~~~~~~MENU ADMIN~~~~~~~~~~~~~~~")
                print("OPSI 1 = MENAMBAHKAN DATA PENJUALAN TIKET")
                print("OPSI 2 = MENAMPILKAN DATA PENJUALAN TIKET")
                print("OPSI 3 = MENGUBAH DATA PENJUALAN TIKET")
                print("OPSI 4 = MENGHAPUS DATA PENJUALAN TIKET")
                print("OPSI 5 = KELUAR")
                opsi = int(input("masukan opsi yang ingin  di pilih: "))
                if opsi == 1:
                    print("OPSI 1 = MENAMBAHKAN DATA PENJUALAN TIKET")
                    print(" di opsi ini anda diminta untuk menambahkan data penjualan terbaru")
                    nama_konser_baru = input("masukan nama konser yang baru : ")
                    kategori_tiket_baru = input("masukan kategori tiket baru : ")
                    tempat_konser_baru = input("masukan tempat konser baru : ")
                    harga_tiket_baru = input("masukan harga tiket : ")
                    stock_tiket_baru = input("masukan stock tiket terbaru: ")
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
                    data_tiket_baru = {}
                    for nomor_tiket, tiket in data_tiket_konser.items():
                        tabel = {}
                        tabel["nomor tiket"] = str(nomor_tiket)
                        tabel["nama konser"] = tiket["nama konser"]
                        tabel["kategori tiket"] = tiket["kategori tiket"]
                        tabel["tempat"] = tiket["tempat"]
                        tabel["harga tiket"] = tiket["harga tiket"]
                        tabel["stock"] = tiket["stock"]
                        data_tiket_baru [nomor_tiket] = tabel
                    print(tabulate(data_tiket_baru.values(), headers="keys", tablefmt='grid'))
                elif opsi == 3:
                    print("OPSI 3 = MENGUBAH DATA PENJUALAN TIKET")
                    print(tabulate(data_tiket_baru.values(), headers="keys", tablefmt='grid'))
                    nomor_tiket = int(input("masukan nomor tiket yang ingin di ubah: "))
                    while True:
                        if nomor_tiket in data_tiket_konser:
                            print("pilih data tiket yang ingin di ubah: ")
                            print("[1] = nama konser")
                            print("[2] = kategori tiket")
                            print("[3] = tempat")
                            print("[4] = harga tiket")
                            print("[5] = stock") 
                        pilihan = int(input("masukan pilihan data yang ingin di ubah: "))
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
                            data_tiket_baru = input("masukan data tiket baru sesuai sama pilihan yang di pilih '{data_tiket_yang_di_ubah}': ")
                            data_tiket_konser[nomor_tiket][data_tiket_yang_di_ubah] = data_tiket_baru
                            pilihan = input("apakah masih ingin mengubah data? ya/tidak: ")
                            print("data berhasil di ubah")
                            if pilihan == "ya":
                                print("silahkan masukan data di pilihan yang ingin di ubah lagi sesuai dengan nomor tiket yang di pilih di awal")
                            elif pilihan == "tidak":
                                print("selsai mengubah data tiket konser")
                                break
                        else:
                            print("nomor tiket tidak ada, silahkan coba lagi")
                elif opsi == 4:
                    print("OPSI 4 = MENGHAPUS DATA PENJUALAN TIKET")
                    nomor_tiket = int(input("masukan nomor tiket yang akan di hapus: "))
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
    elif status == "pengguna":
        print("masukan username = nama dan password = nim")
        username = "intanindahsari"
        password = "088"
        username = input("masukan username: ")
        password = input("masukan password: ")
        if username == "intanindahsari" and password == "088":
            print("login berhasil")
            while True:
                print("~~~~~~~~~~~~~~MENU PENGGUNA~~~~~~~~~~~~~~~")
                print("OPSI 1 = UNTUK MELIHAT DATA TIKET KONSER")
                print("OPSI 2 = MENAMBAHKAN DATA PEMBELIAN TIKET")
                print("OPSI 3 = MENAMPILKAN PEMBELIAN TIKET")
                print("OPSI 4 = KELUAR") 
                opsi = int(input("masukan opsi yang ingin di pilih: "))
                if opsi == 1:
                    print("OPSI 1 = UNTUK MELIHAT DATA TIKET KONSER")
                    data_tiket_baru = {}
                    for nomor_tiket, tiket in data_tiket_konser.items():
                        tabel = {}
                        tabel["nomor tiket"] = str(nomor_tiket)
                        tabel["nama konser"] = tiket["nama konser"]
                        tabel["kategori tiket"] = tiket["kategori tiket"]
                        tabel["tempat"] = tiket["tempat"]
                        tabel["harga tiket"] = tiket["harga tiket"]
                        tabel["stock"] = tiket["stock"]
                        data_tiket_baru [nomor_tiket] = tabel
                    print(tabulate(data_tiket_baru.values(), headers="keys", tablefmt='grid'))
                    
                elif opsi == 2:
                    print("OPSI 2 = MENAMBAHKAN DATA PEMBELIAN TIKET")
                    nama_konser_yang_ingin_di_pesan = input("masukan nama konser yang ingin di pesan: ")
                    jumlah_tiket_yang_ingin_di_pesan = int(input("masukan jumlah tiket yang ingin di pesan: "))
                    total_harga_tiket = 0
                    pembelian_tiket = False
                    for data_tiket in data_tiket_konser.values():
                        if data_tiket ["nama konser"] == nama_konser_yang_ingin_di_pesan:
                            harga_tiket = int(data_tiket["harga tiket"])
                            total_harga_tiket = harga_tiket*jumlah_tiket_yang_ingin_di_pesan
                            pembelian_tiket = True
                            break
                    if pembelian_tiket == False:
                        print("data pembelian tidak di temukan")
                        continue
                    keys_baru = len(data_pembelian_tiket) + 1
                    data_pembelian_tiket[keys_baru] = { "nama konser" : nama_konser_yang_ingin_di_pesan,
                                                        "jumlah tiket" : jumlah_tiket_yang_ingin_di_pesan,
                                                        "total harga" : total_harga_tiket
                    }
                    print("data pembelian telah di tambahkan")
                elif opsi == 3:
                    print("OPSI 3 = MENAMPILKAN PEMBELIAN TIKET")
                    tampilan_pembelian = {}
                    for nomor_pembelian, beli in data_pembelian_tiket.items():
                        nama_konser_yang_disimpan = beli["nama konser"]
                        jumlah_tiket_konser_yang_disimpan = beli["jumlah tiket"]
                        data_pembelian_yang_disimpan = beli["total harga"]
                        tampilan_pembelian[nomor_pembelian] = { "nomor tiket" : str(nomor_pembelian),
                                                            "nama konser" : nama_konser_yang_disimpan,
                                                            "jumlah tiket" :  jumlah_tiket_konser_yang_disimpan,
                                                            "total harga" : f"Rp{data_pembelian_yang_disimpan}"
                        }
                    if len (tampilan_pembelian) > 0:
                        print(tabulate(tampilan_pembelian.values(), headers="keys", tablefmt='grid'))
                    else:
                        print("belum ada data pembelian")
                elif opsi == 4:
                    print("kamu keluar dari menu pengguna")
                    input("tekan entar untuk kembali ke halaman awal")
                    break
                else:
                    print("opsi tidak tersedia silahkan pilih 1-4")
        elif username != "intanindahsari" and password == "088":
            print("username/password salah, coba lagi")
            print("masukan data awal login")
        elif username == "intanindahsari" and password != "088":
            print("username/password salah, silahkan coba lagi")
        else:
            print("anda keluar dari program")
            print("ketik enter untuk kembali ke menu awal")
            input("ketik enter: ")
            break












