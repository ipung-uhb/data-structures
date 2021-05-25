x = "Sepeda"
y = "Motor"

#gabungkan dua buah string
z = x + y

#cetak string 
#output "SepedaMotor"
print(z)

#ulang string
a = x * 2
print(a)

#output SepedaSepeda

#slice atau potong string

#ambil string 2 di depan
b = x[:2]
#ambil string setelah 2 
c = x[2:]
#ambil string sesuai posisi
#semua string dimulai dari indeks ke 0
d = x[0] + x[5]

print(b)
#output 'Se'
print(c)
#output 'peda'
print(d)
#output 'Sa'

#string alphanumerik

f = '4'
g = '5'

h = f+g

print(h) #output "45"

#Kapitalisasi String
i = 'donat'
j = str.capitalize(i)

print(j) #output 'Donat'

#hitung panjang string
r = "Suka Makan"
s = 'Hobbi'

print(len(r)) #output 10 (spasi dihitung)
print(len(s)) #output 5

#cek apakah bernilai digit
digit = '404'
nondigit = 'Empat Kosong Empat'

print(digit.isdigit()) #output True
print(nondigit.isdigit()) #output False

#mengganti bagian string dengan string lain
nama = 'Joko Susanto'
ganti = nama.replace('Joko', 'Aldi')

print(ganti) #output 'Aldi Susanto'

#mencari string di string yang lain
menu = "Nasi Padang"
caristring = "Padang"
print(menu.find(caristring)) #output 5 karena dimulai dari index setelah 5



