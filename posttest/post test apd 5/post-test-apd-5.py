print ("selamat datang")
while True:
    status = input("admin/pengguna:")
    if status == "admin":
        username = "IntanIndahSari"
        password = "088"
        login = 3
        while login <= 3:
            username = input("username:")
            password = input("password:")
            if username == "IntanIndahSari" and password == "088":  
                print("login berhasil, anda adalah admin")
                from tabulate import tabulate
                tiket_konser = [
                                ['NCT','REGULER', 'BSD', '1200000', '5'],
                                ['AESPA', 'VIP', 'GBK', '1500000', '14'],
                                ['TXT', 'VVIP', 'JIS', '1900000', '34']
                                ]
                while True:
                    print ("~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~")
                    print ("opsi 1 : menambahkan data penjualan tiket ")
                    print ("opsi 2 : menampilkan data penjualan tiket")
                    print ("opsi 3 : mengubah data penjualan tiket ")
                    print ("opsi 4 : menghapus data penjualan tiket")
                    print ("opsi 5 : keluar")
                    opsi = int(input("opsi:"))
                    if opsi == 1:
                        while True:
                            print ("~~~~~MENAMBAHKAN DATA PENJUALAN TIKET~~~~~")
                            nama_konser = input("nama konser : ")
                            kategori_tiket = input("kategori : ")
                            tempat = input("tempat konser : ")
                            harga = int(input("harga tiket : "))
                            stock = int(input("sisa tiket yang tersedia:"))
                            tiket_konser.append([nama_konser,kategori_tiket,tempat,harga,stock])
                            tambah = input("apakah anda ingin menambahkan data penjualan lagi?")
                            print("data penjualan berhasil di tambahkan")
                            if tambah == "ya":
                                print("silahkan masukan data penjualan tiket yang ingin anda tambahkan")
                            
                            elif tambah == "tidak":
                                print("anda keluar dari program menambahkan data penjualan tiket")
                                break
                        
                    elif opsi == 2: 
                        print ("~~~~~MENAMPILKAN DATA TIKET~~~~~")
                        if tiket_konser: 
                            header = ['Nama konser','Kategori','Tempat','Harga','Stock']
                            print(tabulate(tiket_konser, headers=header, tablefmt='grid'))
                        
                        else:
                            print("data tidak di temukan di penjualan")
                        print("ini adalah tampilan dari data penjualan tiket yang telah di perbarui")
                    elif opsi == 3 :
                        print ("~~~~~MENGUBAH DATA PENJUALAN TIKET~~~~~")
                        tiket_konser_baru = input("masukan data penjualan tiket yang ingin di ubah: ")
                        for tiket in tiket_konser:
                            if tiket[0] == tiket_konser_baru :
                                tiket[0] = input("nama konser baru : ")
                                tiket[1] = input("kategori tiket baru  :")
                                tiket[2]= input("tempat konser  baru : ")
                                tiket[3] = int(input("harga tiket baru : "))
                                tiket[4] = int(input ("stock tiket baru : "))
                                print("data penjualan tiket telah di perbarui")
                                
                        else:
                            print('data penjualan tidak di temukan')
                    elif opsi == 4:
                        print ("~~~~~MENGHAPUS DATA PENJUALAN TIKET~~~~~")
                        nama_konser = input("nama konser yang ingin di hapus: ")
                        kategori_tiket = input("kategori yang ingin di hapus: ")
                        tempat = input("tempat konser yang ingin di hapus : ")
                        harga = int(input("harga tiket yang ingin di hapus: "))
                        stock = int(input("sisa tiket yang tersedia:"))
                        for tiket in tiket_konser:
                            if (tiket[0] == nama_konser and
                                tiket[1] == kategori_tiket and
                                tiket[2] == tempat and
                                int(tiket[3]) == harga and
                                int(tiket[4]) == stock ):
                                tiket_konser.remove(tiket)
                                print("data penjualan tiket berhasil di hapus")
                        else:
                            print("data penjualan tiket yang ingin di hapus tidak di temukan")
                    elif opsi == 5:
                        print("anda akan kembali ke menu awal program")
                        break
            elif username == "IntanIndahSari"  and password != "088":
                print("login gagal, silahkan coba lagi!")
            elif username != "IntanIndahSari"  and password == "088":
                print("login gagal, silahkan coba lagi!")
            else:
                print("login gagal, anda bukan admin")
            break
    if status == "pengguna":
        username = "IntanIndahSari"
        password = "088"
        login = 3
        while login <= 3:
            username = input("username:")
            password = input("password:")
            if username == "IntanIndahSari" and password == "088":
                print ("login berhasil, anda pengguna")
                print("selamat datang di tempat pembelian tiket")
                from tabulate import tabulate
                tiket_konser  = [
                                ['NCT','REGULER', 'BSD', '1200000', '5'],
                                ['AESPA', 'VIP', 'GBK', '1500000', '14'],
                                ['TXT', 'VVIP', 'JIS', '1900000', '34'],
                                ['TREASURE','REGULER','JIS', '1300000','7']
                                ]
                tiket_konser_yang_akan_dibeli = []
                while True:
                    print ("~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~")
                    print ("opsi 1 : menambahkan pembelian tiket ")
                    print ("opsi 2 : menampilkan pembelian tiket")
                    print ("opsi 3 : mengubah pembelian tiket ")
                    print ("opsi 4 : menghapus pembelian tiket")
                    print ("opsi 5 : keluar")
                    opsi = int(input("opsi:"))
                    if opsi == 1:
                        if tiket_konser: 
                            header = ['Nama konser','Kategori','Tempat','Harga','Stock']
                            print(tabulate(tiket_konser, headers=header, tablefmt='grid'))
                        while True:
                            print ("~~~~~MENAMBAHKAN PEMBELIAN TIKET~~~~~")
                            nama_konser = input("nama konser : ")
                            kategori_tiket = input("kategori : ")
                            tempat = input("tempat konser : ")
                            jumlah_tiket = int(input("masukan jumlah tiket yang ingin di pesan:"))
                            tiket_konser_yang_akan_dibeli.append([nama_konser,kategori_tiket,tempat,jumlah_tiket])
                            tambah = input("apakah anda ingin menambahkan pembelian tiket lagi?")
                            print("pembelian tiket berhasil di tambahkan")
                            if tambah == "ya":
                                print("silahkan masukan data pembelian tiket yang ingin anda tambahkan")
                            
                            elif tambah == "tidak":
                                print("anda keluar dari program menambahkan pembelian tiket")
                                break
                    elif opsi == 2: 
                        print ("~~~~~MENAMPILKAN PEMBELIAN TIKET~~~~~")
                        if tiket_konser_yang_akan_dibeli: 
                            header = ['Nama konser','Kategori','Tempat','jumlah tiket']
                            print(tabulate(tiket_konser_yang_akan_dibeli, headers=header, tablefmt='grid'))
                        
                        else:
                            print("ini adalah tampilan dari pembelian yang anda tambahkan sebelumnya")
                    elif opsi == 3 :
                        print ("~~~~~MENGUBAH PEMBELIAN TIKET~~~~~")
                        tiket_konser_baru = input("masukan data pembelian tiket yang ingin di ubah: ")
                        for tiket in tiket_konser_yang_akan_dibeli:
                            if tiket[0] == tiket_konser_baru :
                                tiket[0] = input("nama konser baru : ")
                                tiket[1] = input("kategori tiket baru  :")
                                tiket[2]= input("tempat konser  baru : ")
                                tiket[3] = int(input ("jumlah tiket baru : "))
                                print("data penjualan tiket telah di perbarui")
                            else:
                                print("data pembelian tidak di temukan")
                    elif opsi == 4:
                        print ("~~~~~MENGHAPUS PEMBELIAN TIKET~~~~~")
                        nama_konser = input("nama konser yang ingin di hapus: ")
                        kategori_tiket = input("kategori yang ingin di hapus: ")
                        tempat = input("tempat konser yang ingin di hapus : ")
                        jumlah_tiket = int(input("jumlah tiket yang ingin di  hapus:"))
                        for tiket in tiket_konser_yang_akan_dibeli:
                            if (tiket[0] == nama_konser and
                                tiket[1] == kategori_tiket and
                                tiket[2] == tempat and
                                int(tiket[3]) == jumlah_tiket ):
                                tiket_konser_yang_akan_dibeli.remove(tiket)
                                print("data penjualan tiket berhasil di hapus")
                                break
                        else:
                            print("data penjualan tiket yang ingin di hapus tidak di temukan")
                            break
                    elif opsi == 5:
                        print("anda akan keluar dari perogram pembelian tiket")
                        break
            elif username == "IntanIndahSari" and password != "088":
                print ("login gagal, silahkan coba lagi")
            elif username != "IntanIndahSari" and  password == "088": 
                print ("login gagal, silahkan coba lagi")
            else:
                print("login gagal, anda keluar dari program")
                print("silahkan masukan status dan username/password yang benar")
                break
            print("login gagal")
            break








