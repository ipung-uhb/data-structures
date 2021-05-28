# importing array module
import array
   

# siapkan array integer
arr = array.array('i', [1, 2, 3, 1, 2, 5]) 
  
# cetak array asli
print ("Array asli adalah : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
  
print ("\r")
  
# Gunakan index() untuk mencetak element dengan nilai 2
print ("Index array untuk element dengan nilai 2 adalah : ", end ="")
print (arr.index(2))
  
# # Gunakan index() untuk mencetak element dengan nilai 1
print ("Index array untuk element dengan nilai 2 adalah ", end ="")
print (arr.index(1))