# Membuat Array Baru 
  
# importing "array" untuk array baru
import array as arr
  
# membuat array dengan tipe integer (i)
a = arr.array('i', [1, 2, 3])
  
# cetak data array
print ("Array baru yang dibuat adalah: ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()