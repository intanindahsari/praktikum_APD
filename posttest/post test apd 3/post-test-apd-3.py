nama = str(input("nama:"))
nim = str(input("nim:")) 
if nama == "Intan Indah Sari" and nim == "088": 
    print ("biaya berlangganan adalah = 1.500.000")    
    biaya_langganan = 1500000     
    print ("ketentuan biaya admin sebagai berikut:")    
    print ("paketBronze = biaya admin 1%, paketSilver = biaya admin 3%, paket Gold = biaya admin 5%, paketPlatinum = biaya admin 7%")     
    paket = str(input("masukan paket yang kamu pilih:")) 
# bagian percabangan 1     
    if paket == "paketBronze":        
        biaya_admin = 1/100         
        total_bayar = biaya_langganan + (biaya_langganan * 1/100)         
        print (total_bayar)         
        print ("keuntungannya yang kamu dapat: kamu bisa akses ke dasar lagu-lagu populer") 
# bagian percabangan 2     
    elif paket == "paketSilver" : 
        biaya_admin = 3/100        
        total_bayar = biaya_langganan + (biaya_langganan * 3/100)         
        print (total_bayar)         
        print ("keuntungannya yang kamu dapat: kamu bisa akses lagu premium dan playlist kostum") 
# bagian percabangan 3      
    elif paket == "paketGold" :
        biaya_admin = 5/100
        total_bayar = biaya_langganan + (biaya_langganan * 5/100)
        print (total_bayar)
        print ("keuntungannya yang kamu dapat: kamu bisa akses lagu premium, playlist kostum dan mode offline") 
# bagian percabangan 4     
    elif paket == "paketPlatinum" : 
        biaya_admin = 7/100         
        total_bayar = biaya_langganan + (biaya_langganan * 7/100)        
        print (total_bayar)         
        print ("keuntungannya yang kamu dapat: kamu bisa akses semua fitur, playlist kostum, mode offline dan konten eksklusif artis") 
else : 
    print("nama dan nim anda tidak sesuai")     
    print("login gagal") 
    

