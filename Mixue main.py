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
        
      def total_pesanan(self):
        total = 0
        
        pesanan = self.head
        while pesanan:
            total += pesanan.harga
            pesanan = pesanan.next
        
        print(f"Total Harga Pesanan: Rp{total}")

daftar_pesanan = DaftarPesanan()

MENU = [["Mixue Ice Cream", 5_000], ["Boba Shake", 16_000], ["Mie Sundae", 14_000], ["Mie Ganas", 11_000], ["Creamy Manggo Boba", 22_000]]

print(
"""
1. Mixue Ice Cream:     Rp.5.000
2. Boba Shake:          Rp.16.000
3. Mie Sundae:          Rp.14.000
4. Mie Ganas:           Rp.11.000
5. Creamy Mango Boba:   Rp.22.000
""")
pesanan = int(input("Silahkan memesan dari menu (input nomer): "))
daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])

while True:

    pesanan = input("apakah anda ingin memesan lagi? (y/t):")

    if pesanan == "y":

        pesanan = int(input("Silahkan memesan dari menu (input nomer): "))

        daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])



    elif pesanan == "t":

        break



    else:

        print("Input salah, silahkan ulangi lagi")





    pesanan = int(pesanan)

    daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])



daftar_pesanan.print()

daftar_pesanan.total_pesanan()

