beli1 = 'Tomat'
beli2 = 'Kangkung'
beli3 = 'Bayam'

beli = ['Tomat','Kangkung','Bayam']

cetak = beli[0] #ambil value di index ke 0

print(cetak) #output 'Tomat'

#perulangan untuk akses array
for x in beli:
    #tercetak semua value 
    print(x)

beli = ['Tomat','Kangkung','Bayam']
panjang = len(beli)
print(panjang) #output 3

#append
#menambahkan element array

ambil = []
ambil.append('Mangga')
ambil.append('Jeruk')

print(ambil) #output ['Mangga', 'Jeruk']

#remove element array
sayur = ['Kol','Wortel','Buncis','Toge']
#remove element di index ke 1
sayur.pop(1)

print(sayur) #output ['Kol','Buncis','Toge']

#remove array element
sayur.remove('Buncis')
print(sayur)

#remove all array element
bunga = ['Melati','Mawar','Anggrek']

#remove all
bunga.clear() #menghapus semua element

print(bunga) #output []

#copy array
motor = ['Yamaha','Honda','Suzuki']
#copy to motor2
motor2 = motor.copy()

print(motor2)

#count array
mahasiswa = ['Harry','John','Maya','Brisya','John']

#count
jumlah = mahasiswa.count('John')

print(jumlah) #output 2 

#extend array
siswa = ['Juki','Ahmad','Roni']
siswabaru = ['Maya','Ari','Aji']

siswa.extend(siswabaru)
print(siswa) #output ['Juki', 'Ahmad', 'Roni', 'Maya', 'Ari', 'Aji']

#index array element
kota = ['Jakarta','Bandung','Surabaya','Makasar']

#cek posisi element Bandung
x = kota.index('Bandung')

print(x) #output 1

#insert array specific position
fruits = ['apple', 'banana', 'cherry']

#insert element at index 1
fruits.insert(1, "orange")

print(fruits) #output ['apple', 'orange', 'banana', 'cherry']

#reverse
angka = [1,2,3,4,5]

angka.reverse()

print(angka) #output [5, 4, 3, 2, 1]

#sort array
cars = ['Ford', 'BMW', 'Volvo']

angka = [1,6,7,3,2,5]

cars.sort()
angka.sort()

print(cars) #output ['BMW', 'Ford', 'Volvo']
print(angka) #output [1, 2, 3, 5, 6, 7]