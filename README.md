*Tugas Analisis*

*Pertanyaan:* Apa yang terjadi jika kamu mengubah `hero1.hp` menjadi 500?
*Jawaban:* Nilai HP objek `hero1` akan langsung berubah menjadi 500 tanpa ada validasi. Hal ini terjadi karena atribut `hp` bersifat *Public*, sehingga dapat diakses dan dimodifikasi secara bebas dari luar class. Ini berisiko karena data bisa diubah menjadi nilai yang tidak logis (misal: HP menjadi negatif atau terlalu tinggi).

*Tugas Analisis 2*

*Pertanyaan:* Mengapa penting parameter `lawan` menerima objek utuh, bukan hanya string nama?
*Jawaban:* Karena dengan menerima *objek utuh*, kita memiliki akses ke seluruh status dan perilaku (*method*) dari objek tersebut. Kita bisa memanggil `lawan.diserang()` atau mengurangi `lawan.hp` secara langsung. Jika hanya mengirim string nama, kita tidak bisa mengubah data asli dari objek yang dituju.

*Tugas Analisis 3*

*Pertanyaan:* Error apa yang muncul? Mengapa error tersebut mengatakan `Mage object has no attribute 'name'`?
*Jawaban:* Error yang muncul adalah *AttributeError*. Hal ini terjadi karena saat `super().__init__` dihapus, class anak (`Mage`) tidak menjalankan proses inisialisasi milik class induk (`Hero`). Akibatnya, variabel `self.name` dan `self.hp` yang seharusnya dibuat di class induk tidak pernah terbentuk di objek `Mage`.
*Peran `super()`:* Sebagai penghubung untuk memanggil *constructor* class induk agar semua atribut dasar (seperti nama dan HP) dapat diwariskan dan diinisialisasi dengan benar pada class anak.

*Tugas Analisis 4*

*Pertanyaan 1 (Hacking):* Apakah nilai HP muncul atau Error? Jelaskan konsep Name Mangling!
*Jawaban:* Nilai HP *muncul*. Python menggunakan konsep *Name Mangling*, di mana atribut private `__hp` secara otomatis diubah namanya menjadi `_NamaClass__hp` (dalam hal ini `_HeroA4__hp`). Python tidak benar-benar mengunci data secara mutlak, namun ini adalah tanda bahwa atribut tersebut tidak boleh diakses langsung demi keamanan data.
*Pertanyaan 2 (Validasi):* Apa yang terjadi jika logika `if` dihapus dan kita set HP ke -100?
*Jawaban:* HP Hero akan menjadi -100. Hal ini membuktikan bahwa *Setter* sangat penting untuk menjaga *integritas data*. Tanpa Setter, objek bisa memiliki data yang tidak valid (seperti HP negatif dalam game).

*Tugas Analisis 5*

*Pertanyaan 1 (Melanggar Kontrak):* Error apa yang muncul? Apa arti pesan error tersebut?
*Jawaban:* Error yang muncul adalah `TypeError: Can't instantiate abstract class HeroA5 with abstract method serang`. Artinya, class `HeroA5` belum memenuhi "janji" atau kontrak untuk mengimplementasikan method `serang` yang ada di `GameUnit`. Selama method tersebut belum dibuat, class tersebut dianggap belum lengkap dan tidak bisa dibuat menjadi objek.
*Pertanyaan 2 (Mencetak Cetakan):* Mengapa `GameUnit` dilarang menjadi objek? Apa gunanya?
*Jawaban:* Karena `GameUnit` adalah *Abstract Class* yang berfungsi sebagai blueprint atau "kerangka" saja. Dia tidak memiliki detail implementasi. Gunanya adalah untuk memastikan semua karakter (Hero/Monster) memiliki standar method yang sama agar sistem game bisa berjalan seragam.

*Tugas Analisis 6*

*Pertanyaan 1 (Skalabilitas):* Apakah program berjalan lancar saat ditambah `Healer`? Apa keuntungannya?
*Jawaban:* Program berjalan lancar. Keuntungannya adalah *fleksibilitas*. Programmer bisa menambah puluhan karakter baru tanpa perlu mengubah kode utama (*looping*). Cukup buat class baru dengan method `serang()`, maka otomatis akan dikenali oleh sistem.
*Pertanyaan 2 (Konsistensi):* Apa yang terjadi jika nama method diganti? Mengapa harus sama?
*Jawaban:* Program akan *Error* (AttributeError) karena loop mencari method bernama `serang()`. Nama method harus persis sama agar sistem bisa memanggil fungsi tersebut secara otomatis tanpa peduli apa jenis objeknya. Inilah inti dari Polimorfisme: "Satu perintah, banyak bentuk aksi."

Berikut adalah hasil output daari analisi 1 -6 : 

<img width="1279" height="451" alt="Screenshot 2026-03-06 180426" src="https://github.com/user-attachments/assets/af3a26d8-7fd5-43a5-aca9-e6024345be7f" />

*Tugas Kelompok*

**📦 TechMaster Inventory System (OOP Implementation)**
Sistem Inventaris Sederhana ini dibangun menggunakan bahasa pemrograman Python untuk mendemonstrasikan penerapan pilar-pilar Object-Oriented Programming (OOP) secara nyata.

🛠️ Fitur & Implementasi OOP
Project ini mengintegrasikan empat konsep utama OOP sebagai berikut:

1. Abstraksi (Abstraction)
Menggunakan ABC (Abstract Base Class) untuk mendefinisikan kelas induk BarangElektronik. Kelas ini berfungsi sebagai blueprint atau kerangka kerja yang mewajibkan kelas turunannya (Laptop & Smartphone) untuk mengimplementasikan method hitung_total dan tampilkan_detail.

2. Enkapsulasi (Encapsulation)
Data sensitif seperti __stok dan __harga disembunyikan menggunakan akses private.
Validation: Penambahan stok melalui method tambah_stok() dilengkapi validasi agar tidak menerima nilai negatif.
Getter: Menggunakan dekorator @property untuk mengakses data stok secara aman.

3. Pewarisan (Inheritance)
Kelas Laptop dan Smartphone mewarisi seluruh fungsionalitas dari BarangElektronik. Hal ini meminimalisir redundansi kode (Reusability) karena atribut dasar hanya didefinisikan satu kali di kelas induk.

4. Polimorfisme (Polymorphism)
Implementasi perhitungan pajak yang berbeda untuk setiap kategori barang:
Laptop: Dikenakan pajak tambahan sebesar 10%.
Smartphone: Dikenakan pajak tambahan sebesar 5%.
Meskipun menggunakan nama method yang sama (hitung_total), setiap objek memberikan hasil kalkulasi yang berbeda sesuai dengan logika unik kelasnya.

Berikut hasil Output nya : 

<img width="1097" height="488" alt="Screenshot 2026-03-06 181710" src="https://github.com/user-attachments/assets/aa3a3948-d851-4959-956a-24691dae6b4e" />

