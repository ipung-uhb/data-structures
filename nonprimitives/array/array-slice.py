# importing array module
import array as arr
  
# membuat sebuah list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
a = arr.array('i', l)
print("Intial Array: ")
for i in (a):
    print(i, end =" ")
  
# cetak element dalam range tertentu
# Gunakan operasi slice
Sliced_array = a[3:8]
print("\nAmbil semua elemen pada range 3-8: ")
print(Sliced_array)
  
# Cetak elemen pada
# titik yang telah ditentukan ke akhir
Sliced_array = a[5:]
print("\nElemen dipotong mulai dari posisi 5 "
      "hingga elemen terakhir: ")
print(Sliced_array)
  
# Cetak elemen pada
# mulai sampai akhir
Sliced_array = a[:]
print("\nCetak semua element dengan operasi slice: ")
print(Sliced_array)