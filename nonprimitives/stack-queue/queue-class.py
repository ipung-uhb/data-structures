#buat kelas baru
class Queue:

    #fungsi yang pertama kali dijalankan
    #siapkan dengan list kosong
    def __init__(self):
        self.queue = []

    #tambahkan elemen ke antria
    def enqueue(self, item):
        self.queue.append(item)

    #proses antrian yang pertama
    def dequeue(self):
        #jika panjang antrian kurang dari satu maka abaikan
        if len(self.queue) < 1:
            return None
        #jika lebih dari satu maka hapus elemen pertama
        return self.queue.pop(0)

    #fungsi cek panjang antrian
    def size(self):
        return len(self.queue) 

#buat objek baru dari class Queue
#mewarisi semua sifat class induknya
antrian = Queue()

# Tambahkan antrian
antrian.enqueue('Salman')
antrian.enqueue('Hari')
antrian.enqueue('Keenar')
antrian.enqueue('Zira')
antrian.enqueue('Noval')

# lakukan dequeue 
# 'hapus Salman' => posisi 0
prosesantrian = antrian.dequeue() 

# dequeue kembali
# 'hapus Hari' => posisi 0
prosesantrian = antrian.dequeue() 

# dequeue kembali
# 'hapus Keenar' => posisi 0
prosesantrian = antrian.dequeue() 

print(antrian.queue) # ['Zira','Noval']