#buat kelas dengan nama Stack
class Stack:

    #fungsi yang pertama kali dijalankan
    #fungsi pernyiapan class dimulai dengan list kosong []
    def __init__(self):
        self.stack = []

    #fungsi untuk menghapus elemen terakhir
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    #fungsi untuk menambahkan elemen
    def push(self, item):
        self.stack.append(item)

    #fungsi untuk melihat ukuran dari Stack
    def size(self):
        return len(self.stack)

input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')
input_queue.enqueue('RIGHT')
input_queue.enqueue('B')

# Now we can process each item in the queue by dequeueing them
key_pressed = input_queue.dequeue() # 'DOWN'

# We'll probably change our player position
key_pressed = input_queue.dequeue() # 'RIGHT'

# We'll change the player's position again and keep track of a potential special move to perform
key_pressed = input_queue.dequeue() # 'B'