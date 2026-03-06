# SISTEM INVENTARIS SEDERHANA

from abc import ABC, abstractmethod

# == KELAS UTAMA ==
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.__stok = stok      # private
        self.__harga = harga    # private
    
    @property
    def stok(self):
        return self.__stok
    
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal! Stok tidak boleh negatif ({jumlah})")
            return False
        self.__stok += jumlah
        print(f"Berhasil tambah stok {self.nama}: {self.__stok} unit")
        return True
    
    @abstractmethod
    def tampilkan_detail(self):
        pass
    
    @abstractmethod
    def hitung_total(self, jumlah):
        pass

# == KELAS LAPTOP ==
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga, processor):
        super().__init__(nama, stok, harga)
        self.processor = processor
    
    def tampilkan_detail(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"
    
    def hitung_total(self, jumlah):
        pajak = self._BarangElektronik__harga * 0.10
        return (self._BarangElektronik__harga + pajak) * jumlah

# == KELAS SMARTPHONE ==
class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga, kamera):
        super().__init__(nama, stok, harga)
        self.kamera = kamera
    
    def tampilkan_detail(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"
    
    def hitung_total(self, jumlah):
        pajak = self._BarangElektronik__harga * 0.05
        return (self._BarangElektronik__harga + pajak) * jumlah

# == FUNGSI UTAMA ==
def main():
    print("=== SISTEM INVENTARIS TECHMASTER ===")
    
    # 1. Buat barang
    laptop = Laptop("ROG Zephyrus", 0, 20000000, "Ryzen 9")
    hp = Smartphone("iPhone 13", 0, 15000000, "12MP")
    
    # 2. Tambah stok
    print("\n--- SETUP DATA ---")
    laptop.tambah_stok(10)
    hp.tambah_stok(-5)   
    hp.tambah_stok(20)
    
    # 3. Beli barang
    print("\n--- TRANSAKSI ---")
    
    # Format rupiah
    def format_rp(angka):
        return f"Rp {angka:,}".replace(",", ".")
    
    # Beli 2 laptop dan 1 hp
    beli_laptop = 2
    beli_hp = 1
    
    print(f"1. {laptop.tampilkan_detail()}")
    print(f"   Beli: {beli_laptop} unit")
    print(f"   Total: {format_rp(laptop.hitung_total(beli_laptop))}")
    
    print(f"\n2. {hp.tampilkan_detail()}")
    print(f"   Beli: {beli_hp} unit")
    print(f"   Total: {format_rp(hp.hitung_total(beli_hp))}")
    
    total = laptop.hitung_total(beli_laptop) + hp.hitung_total(beli_hp)
    print(f"\nTOTAL TAGIHAN: {format_rp(total)}")

# == JALANKAN PROGRAM ==
if __name__ == "__main__":
    main()