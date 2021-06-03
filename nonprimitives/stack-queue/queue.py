kata = []

# tambahkan beberapa elemen dengan append()
kata.append('n') #0
kata.append('a') #1
kata.append('m') #2
kata.append('a') #3

# Sekarang dequeue elemen pertama
# 'n' di hapus
first_item = kata.pop(0)
print(first_item)

# dequeue kembali
# 'a' dihapus
first_item = kata.pop(0)
print(first_item)

# 'n' and 'a' terhapus
print(kata) # ['m', 'a']