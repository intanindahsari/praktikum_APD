print ("daftar menu: pecel lele = Rp 10.000 dengan pajak 5%, mie ayam = Rp 15.000 dengan pajak 8%, nasi padang = Rp 18.000 dengan pajak 10%")
print ("masukan nama dan nim kamu untuk memesan")

input ("nama:")
input ("nim:")

print ("kamu pesan pecel lele seharga Rp 10.000 dengan pajak 5%")
harga_pecel_lele = int(input("masukan harga pecel lele:"))
hasil_pajak = harga_pecel_lele * (5/100)
total_bayar = harga_pecel_lele + hasil_pajak
print ("total yang harus kamu bayar setelah terkena pajak 5% dari memesan pecel lele adalah:")
print (total_bayar) 
print (f"{"MENU":<20}{"HARGA":>15}{"PAJAK":>10}{"TOTAL":>15}") 
print (f"{'pecel lele':<20}{harga_pecel_lele:>15}{hasil_pajak:>10}{total_bayar:>15}")

print ("kemudian kamu pesan lagi mie ayam seharga Rp 15.000 dengan pajak 8%")
harga_mie_ayam = int(input("masukan harga mie ayam:"))
hasil_pajak = harga_mie_ayam * (8/100)    
total_bayar = harga_mie_ayam + hasil_pajak
print ("total yang harus kamu bayar setelah terkena pajak 8% dari memesan mie ayam adalah:")
print (total_bayar)
print (f"{"MENU":<20}{"HARGA":>15}{"PAJAK":>10}{"TOTAL":>15}")
print (f"{'mie ayam':<20}{harga_mie_ayam:>15}{hasil_pajak:>10}{total_bayar:>15}")

print ("lalu kamu pesan lagi nasi padang seharga Rp 18.000 dengan pajak 10%")
harga_nasi_padang = int(input("masukan harga nasi padang:"))
hasil_pajak = harga_nasi_padang * (10/100)
total_bayar = harga_nasi_padang + hasil_pajak
print (total_bayar)
print ("total yang harus kamu bayar setelah terkena pajak 10% dari memesan nasi padang adalah:")
print (total_bayar)
print (f"{"MENU":<20}{"HARGA":>15}{"PAJAK":>10}{"TOTAL":>15}")
print (f"{'nasi padang':<20}{harga_nasi_padang:>15}{hasil_pajak:>10}{total_bayar:>15}")
