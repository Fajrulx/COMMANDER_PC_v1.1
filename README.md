Commander_PC
Commander_PC adalah alat untuk mengelola perangkat dalam satu jaringan lokal. Bisa shutdown, restart, atau sleep dari perangkat lain.
Cocok buat lab komputer, sekolah, atau network lokal.

📌 Fitur
  Scan area – Cari node aktif dalam jaringan
  Command for node – Kirim perintah ke satu atau banyak node sekaligus
  Konfirmasi eksekusi – Node balas "Siap_laksanakan!" sebelum eksekusi
  Multi target – Kirim perintah ke banyak node dalam satu waktu
  Service otomatis – Node agent jalan di background (systemd)

🖥️ Cara Install
  1. Login sebagai root / super user
  2. Masuk pada direktori root/
  3. Clone repo ini, jalankan command : git clone https://github.com/Fajrulx/COMMANDER_PC_1.1.git (kalian harus punya service git untuk pakai git)
  4. Setelah clone repo, akan terinstall sebuauh direktory COMMANDER_PC_1.1, yang isinya file sistem commander dan node
  5. Masuk pada direktori tersebut (COMMANDER_PC_1.1)
  6. Dalam direktori tersebut ada file Install.sh, jalankan file itu dengan masukan perintah pada terminal :  bash Install.sh atau sudo bash install.sh
  7. Setelah file tersebut run, maka kamu akan memilih peran untuk perangkat yang kamu gunakan sekarang
  8. pilih sesuai yang kamu tentukan
  9. setelah semua proses telah selesai, hapus file Install.sh tersebut (opsional sihh)
  10. oke semua hal telah terinstall

🖥️ node settings
  1. pada bagian node itu perlu kalian atur identitasnya secara manual, jadi setelah proses instalasi dari Install.sh
     kalian perlu mengatur nama node dan id nya secara manual, dengan cara edit langsung pada file System_node.py
  2. lokasi file System_node.py berada /opt/System_node, jadi lokasi nya /opt/System_node/System_node.py
  3. pada file tersebut, kalian cukup edit pada baris kode nomor 10 yaitu pada :
     Identitas_node = 'Nama_Node = PC_NODE_1 | ID_Node = 000001'
     dalam 'Nama_Node = PC_NODE_1 | ID_Node = 000001' itu kalian bisa ganti terserah kalian mau isi seperti apa, contoh :
     'Nama_Node = PC_GAMING | ID_Node = 99999999999' atau 'PC_chihuahua | 10', intinya terserah kalian
  4. Setelah mengedit file, kalian perlu restart toolnya, jalankan perintah pada terminal :
     systemctl restart System_node.service
  5. setelah itu node udah bekerja seperti biasa
  6. selmat menggunakan

⚠️ Catatan
  Tool ini lebih bekerja pada perangkat linux, tepatnya Debian dari versi 11 - seterusnya tergantung dari packet python yang terinstall pada debian
  Port 5005 UDP pada perangkat atau jaringan harus terbuka
  Commander dan node harus satu jaringan
