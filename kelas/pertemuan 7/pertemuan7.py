# def perkenalan():
#     print("hallo aku intaan, nisaa")
#     print("aku sedang haluu, jaemin jadi future")
# perkenalan()

# def menu ():
#     print("~~~ ayam betutu = 12.000")
#     print("~~~ bebek bakar = 15.000")
#     print("~~~ mie ayam bakso = 13.000")
# retrun ini buat ngembaliin pilihan (kaya while)
# kalau retrunnya di hapus di bakalan none (pilihan tidak valid)

def menu():
    print("=== Menu Utama ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    return pilihan

def tambah_data():
    print("Menambahkan data")
    print("Data berhasil ditambahkan")
    
def hapus_data():
    print("Menghapus data")
    print("Data berhasil dihapus")

def tampilkan_data():
    print("Menampilkan data")
    print("Data ditampilkan")

while True:
    pilihan = menu()
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        hapus_data()
    elif pilihan == '3':
        tampilkan_data()
    elif pilihan == '4':
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")


# def salam():
#     print ("Halo, Ridho")
# def kali():
#     X = 5*5
#     print(X)

# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

# def nama_fungsi(parameter):
#     print (parameter)
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas persegi panjang adalah ", luas)

# def nama_fungsi(parameter):
#     print (parameter)

# #Pembuatan Fungsi Dengan Parameter
# # 

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas


# nama = "intan" #global

# def salam():
#     nama = "indah" #lokal
#     print("halo", nama)

# # print(nama)
# salam()

# def tambah (a, b):
#     return a + b 

# tambah(3, 4)
# tambahlagi = tambah(3, 4)
# print(tambahlagi)

# tambahlagi -= 1
# print(tambahlagi)

# def lpersegi(s):
#     c = s * s
#     print(lpersegi(6))

# def lpersegi(s):
#     c = s * s
#     return c
# print(lpersegi(6))

# def luas_persegi():
#     sisi = int(input("masukan angkanya: "))
#     luas = sisi * sisi 
#     return luas
# print (luas_persegi())

# angka = int(input('Masukkan Angka : '))
# print(angka) #input 'Hai'

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(f'angka yang kamu input: {angka:}')
# finally:
#     print ('block try selesai')



