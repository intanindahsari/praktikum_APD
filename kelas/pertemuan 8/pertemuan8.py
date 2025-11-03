# num = int("42") # 42
# name = str(123) # "123"
# data = list("abc") # ['a', 'b', 'c']
# data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num))

# listAngka = [1,13,24,12,34,65]

# print (len(listAngka))

# for i, v in enumerate(['a', 'b']):
#     print(i, v)

# a = "intan"
# print(len(a))

# if len == 0:
#     print("data masih kosong")

# x = 42
# def fungsi():
#     x = 10
#     y = 20
#     z = 30
#     print(globals()['x']) # mendapatkan isi dari variabel x (global)
#     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
#     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# pilihan = input("apakah anda ingin lanjut?(ya/tidak)").lower()
# if pilihan == "ya":
#     print("terima kasih telah menggunakan program kami")
# elif pilihan == "TIDAK":
#     print("program lanjut")
# else:
#     print("input salah kocak")

# import math
# from math import sqrt
# import math as m

# import math
# print(math.sqrt(16))
# print(math.factorial(4))

# from math import sqrt
# from math import factorial
# print(sqrt(16))
# print(factorial(4))

# import math as intan
# print(intan.sqrt(15))
# print(intan.factorial(4))

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4 berhenti sebelum angka 5

# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize


# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang

# print(acak_kartu)

# from datetime import datetime
# while True:
#     print(datetime.now())

# import inquirer
# pertanyaan = [
# inquirer.List(
# 'size',
# message="What size do you need?",
# choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
# ),
# ]
# # mendapatkan jawaban
# answer = inquirer.prompt(pertanyaan)
# print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
# print(answer['size']) # Ambil value dari key 'size' (Large)

# from autentikasi import login  
# from create import tambah_data_siswa
# print("Selamat datang di aplikasi!") 
# # Menggunakan modul login
# if login("admin", "123"):
#     print("Login berhasil!")
# # Menggunakan modul create
#     tambah_data_siswa({"nama": "Budi", "nilai": 90})
# else:
#     print("Login gagal!")

import inquirer
# deklarasi struktur dictionary
data = {
'nama': [],
'nim': [],
'no_hp': []
}
def tambahData():
        questions = [
            inquirer.Text('nama', message="Input nama mu"),
            inquirer.Text('nim', message="Input NIM kamu"),
            inquirer.Text('no_hp', message="Input nomor hp kamu")
]
        answers = inquirer.prompt(questions)
# hasil input akan disimpan ke

# tambahkan isi dari list, sesuai key nya masing-masing
        data['nama'].append(answers['nama'])
        data['nim'].append(answers['nim'])
        data['no_hp'].append(answers['no_hp'])
# panggil fungsi
tambahData()
# contoh jika ingin melihat isi dari dictionary data dengan key 'nama'
# print(f"List nama:")
# for i, nama in enumerate(data['nama']):
#     print(f"{i+1}. {nama}")