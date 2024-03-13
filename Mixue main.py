class Pesanan:
    def __init__(self, nama_menu, harga, next=None):
        self.nama_menu = nama_menu
        self.harga = harga
        self.next = next

class DaftarPesanan:
    def __init__(self):
        self.head = None
    
    def tambahkan_pesanan(self, nama_menu, harga):
        pesanan = Pesanan(nama_menu, harga)

        if self.head is None:
            self.head = pesanan
            return

        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = pesanan
    
    def print(self):
        if self.head is None:
            print("Daftar Pesanan masih Kosong")
            return
        
        pesanan = self.head
        while pesanan:
            print(f"{pesanan.nama_menu}: {pesanan.harga}")
            pesanan = pesanan.next
        
       
