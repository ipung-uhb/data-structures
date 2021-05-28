# importing "array" untuk membuat array
import array as arr
  
# array dengan tipe integer
a = arr.array('i', [1, 2, 3])
  
  
print ("Array Integer sebelum dilakukan insert : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
  
# menambahkan elemen dengan
# fungsi insert
a.insert(1, 4)
  
print ("Array Integer setelah dilakukan insert : ", end =" ")
for i in (a):
    print (i, end =" ")
print() 
  
# array dengan tipe float
b = arr.array('d', [2.5, 3.2, 3.3])
  
print ("Array Float sebelum dilakukan insert : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()
  
# menambahkan element dengan append
b.append(4.4)
  
print ("Array Float setelah dilakukan insert : ", end =" ")
for i in (b):
    print (i, end =" ")
print() 