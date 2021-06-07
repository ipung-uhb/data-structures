#buat kelas node baru
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        

# Metode untuk menambahkan node pada root
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# To find the inorder successor which is the smallest node in the subtree
    # def findsuccessor(self, current_node):
    #     while current_node.left != None:
    #         current_node = current_node.left
    #     return current_node

# metode untuk mencari sebuah value 
    def findval(self, lkpval):
        #cari di node kiri dahulu
        if lkpval < self.data:
            #jika di kiri kosong
            if self.left is None:
                return str(lkpval)+" Tidak Ditemukan"
            return self.left.findval(lkpval)
        #jika di kiri tidak ada cari ke node kanan
        elif lkpval > self.data:
            #jika di kanan kosong
            if self.right is None:
                return str(lkpval)+" Tidak Ditemukan"
            return self.right.findval(lkpval)
        # node ditemukan
        else:
            return str(self.data) + " Ditemukan"


   # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # berfungsi untuk menghapus node 
    # diganti dengan node terdalam
    def deleteDeepest(self,d_node):
        q = []
        q.append(self)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)
    
    # Fungsi untuk menghapus node 
    def deletion(self, key):
        if self == None :
            return None
        if self.left == None and self.right == None:
            if self.data == key :
                return None
            else :
                return self
        key_node = None
        q = []
        q.append(self)
        while(len(q)):
            temp = q.pop(0)
            if temp.data == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node :
            x = temp.data
            self.deleteDeepest(temp)
            key_node.data = x
        return self


root = Node(27)
root.insert(14)
root.insert(35) 
root.insert(31)
root.insert(10)
root.insert(19)
print('Sebelum di hapus')
root.PrintTree()
# print(root.findval(13)) #tidak ditemukan
# print(root.findval(14)) #ditemukan
root.deletion(35)
print('Setelah di hapus')
root.PrintTree()


#root.PrintTree()

