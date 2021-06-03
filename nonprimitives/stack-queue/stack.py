kata = []

# tambahkan beberapa elemen dengan append()
kata.append('n') #0
kata.append('a') #1
kata.append('m') #2
kata.append('a') #3

# Kita jalankan pop() 
# huruf a di dapatkan dan di keluarkan
kata_terakhir = kata.pop()
print(kata_terakhir)

# Kita Jalankan pop() kembali
# huruf terakhir sekarang adalah m
kata_terakhir = kata.pop()
print(kata_terakhir)

# cetak isi tumpukan yang masih tersedia
print(kata) #output ['n', 'a']

fruits = []

# Let's enqueue some fruits into our list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# Now let's dequeue our fruits, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

# If we dequeue again we'll get 'grapes'
first_item = fruits.pop(0)
print(first_item)

# 'mango' and 'orange' remain
print(fruits) # ['c', 'a']