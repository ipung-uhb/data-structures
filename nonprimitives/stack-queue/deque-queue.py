from collections import deque

# siapkan dequeue list kosong
numbers = deque()

# Tambahkan beberapa elemen dengan append
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)


# lakukan queue untuk menghapus elemen pertama 
# gunakan fungsi popleft()
first_item = numbers.popleft()
print(first_item) # 99
print(numbers) # deque([15, 82, 50,47])