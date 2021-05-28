# importing array module
import array
  
# siapkan data array integer
arr = array.array('i', [1, 2, 3, 1, 2, 5]) 
  
# cetak array asli
print ("Array sebelum update : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
  
print ("\r")
  
# Update array index ke 2 dengan nilai element 6
arr[2] = 6
print("Array setelah update : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
print()
  
# Update array index ke 4 dengan nilai elemen 8
arr[4] = 8
print("Array setelah update : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")