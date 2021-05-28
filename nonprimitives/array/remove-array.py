# importing "array" module
import array
   
# inisialisasi array
# array dengan tipe integer
arr = array.array('i', [1, 2, 3, 1, 5]) 
  
# cetak array pertama
print ("Array pertama : ", end ="")
for i in range (0, 5):
    print (arr[i], end =" ")
  
print ("\r")
  
# menggunakan fungsi pop() untuk menghapus elemen pada posisi ke index ke-2
print ("Element yang dihapus adalah : ", end ="")
print (arr.pop(2))
  
# cetak array telah dilakukan pop()
print ("Array setelah di pop() : ", end ="")
for i in range (0, 4):
    print (arr[i], end =" ")
  
print("\r")
  
# Menggunakan remove() untuk menghapus yang pertama
arr.remove(1)
  
# cetak array setelah dihapus dengan remove()
print ("Array setelah proses remove ", end ="")
for i in range (0, 3):
    print (arr[i], end =" ")