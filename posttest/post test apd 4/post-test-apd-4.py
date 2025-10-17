print  ("masukan username dan password kamu")
print  ("username=nama dan password=nim")
i = 1
while i <= 3:
    username = (input("username:"))
    password = (input("password:"))
    if username == "Intan Indah Sari" and password == "088":
        i = 3
        while True:
            print ("opsi tiket")
            print ("opsi 1")
            print ("opsi 2")
            print ("opsi 3")
            print ("opsi 4")
            opsi = int(input("opsi:"))
            if opsi == 1:
                print ("tiket reguler")
                print ("harga tiket = 50.000")
            elif opsi == 2:
                print ("tiket VIP")
                print ("harga tiket = 100.000")
            elif opsi == 3:
                print ("tiket VVIP")
                print ("harga tiket = 150.000")
            elif opsi == 4:
                print ("terima kasih telah membeli tiket di sini, anda akan keluar dari program")
                break
            print ("masukan jumlah tiket yang ingin kamu pesan!")
            jumlahtiket = int(input("jumlah tiket:"))
            
            for jumlahtiket in range (1,6):
                print ("harga tiket ke-")
                print (jumlahtiket)
                if opsi == 1:
                    hargatiket = 50000
                    totalbayar = hargatiket*jumlahtiket
                    print (totalbayar)
                    totalbayar = totalbayar - (totalbayar*0.08)
                    print ("kamu dapat diskon 8% karena telah berbelanja <= 200000")
                elif opsi ==2:
                    hargatiket = 100000
                    totalbayar = hargatiket*jumlahtiket
                    print (totalbayar)
                    totalbayar = totalbayar - (totalbayar*0.12)
                    print ("kamu dapat diskon 12% karena telah berbelanja <= 300000")
                elif opsi == 3:
                    hargatiket = 150000
                    totalbayar = hargatiket*jumlahtiket
                    print (totalbayar)
                    totalbayar = totalbayar - (totalbayar*0.12)
                    print ("kamu dapat diskon 12% karena telah berbelanja <= 300000")
            print ("total bayar kamu setelah dapat diskon")
            print (totalbayar)
    else :
        i = i+1
        print ("username atau nama kamu salah")
else :
    print ("login gagal")
    print ("kamu sudah mencoba sebanyak 3 kali")
