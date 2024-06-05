class Stack:
    def _init_(self):
        self.stack = []
    
    def push(self, berkas):
        self.stack.append(berkas)
        print(f'berkas "{berkas}" telah ditambahkan ke dalam laci.')

    def pop(self):
        if not self.is_empty():
            removed_berkas = self.stack.pop()
            print(f'berkas "{removed_berkas}" telah diambil dari dalam laci.')
            return removed_berkas
        else:
            print('berkas.pdf')
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Laci kosong, tidak ada berkas yang dapat dilihat.'

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if not self.is_empty():
            print("Isi laci saat ini (dari bawah ke atas):")
            for berkas in self.stack:
                print(f'- {berkas}')
        else:
            print('Laci kosong.')
            

def main():
    laci = Stack()
    
    while True:
        print("\nMenu:")
        print("1. Tambah berkas ke dalam laci")
        print("2. Ambil berkas dari dalam laci")
        print("3. Lihat berkas paling atas dalam laci")
        print("4. Tampilkan semua berkas dalam laci")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            berkas_name = input("Masukkan nama berkas yang ingin ditambahkan: ")
            laci.push(berkas_name)
        elif pilihan == '2':
            laci.pop()
        elif pilihan == '3':
            print(f'berkas paling atas dalam laci: {laci.peek()}')
        elif pilihan == '4':
            laci.display()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("tidak ada dalam pilihan. Silakan coba lagi.")

if __name__== "__main__":
    main()