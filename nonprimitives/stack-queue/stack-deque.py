from collections import deque

# menyiapkan list dengan deque
numbers = deque()

# tambahkan elemen baru ke dalam numbers
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# Jalankan pop() untuk mengeluarkan elemen yang terakhir dimasukan
last_item = numbers.pop()
print(last_item) # 47
print(numbers) # deque([99, 15, 82, 50])