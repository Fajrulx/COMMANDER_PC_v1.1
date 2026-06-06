import socket
import time

def Command():
    while True:
        try:
            print('''
___________________________________________________________________________________________
    (~) Pada program command for node ada pilihan program lagi :
    (1) Berikan perintah pada satu node saja
    (2) Berikan perintah pada beberapa node sekaligus''')
            pilih_program = input('''
    (>_<) Masukan program yang anda pilih (1/2) : ''').strip()
            print('''
___________________________________________________________________________________________''')
            if not pilih_program:
                print('''
    (!!!) Anda belum memasukan pilihan
___________________________________________________________________________________________''')
                continue
            elif pilih_program == '1':
                program_nomor_1()
            elif pilih_program == '2':
                program_nomor_2()
            else:
                print('''
    (!!!) Masukan nomor opsi program yang valid
___________________________________________________________________________________________''')
            break
        except KeyboardInterrupt:
            print('''
    (-_-) Anda menghentikan program secara paksa
___________________________________________________________________________________________''')
            return
def program_nomor_1():
    while True:
        try:
            minta_ip_node_program_1 = input('''
    (>_o) Masukan ip address node yang akan diberikan perintah : ''').strip()
            ip_node = minta_ip_node_program_1.split('.')
            ip_node_fix = len(ip_node)
            if ip_node_fix != 4:
                print('''
    (!!!) Masukan ip address yang valid
___________________________________________________________________________________________''')
                continue
            if not minta_ip_node_program_1:
                print('''
    (!!!) Anda belum memasukan ip address | silahkan masukan ip address node
___________________________________________________________________________________________''')
                continue
            break
        except KeyboardInterrupt:
            print('''

    (!!!) Anda membatalkan program command for node secara paksa (-_-)
___________________________________________________________________________________________''')
            return
    print('''
    (~) Perintah yang bisa di berikan kepada node :
    (1) SHUTDOWN
    (2) RESTART
    (3) SLEEP''')
    while True:
        try:
            minta_perintah_program_1 = input('''
    (^_^) Masukan nomor pilihan program yang ingin dijalankan pada node (1/2/3) : ''')
            if minta_perintah_program_1 == '1':
                minta_perintah_program_1 = 'POWEROFF'
            elif minta_perintah_program_1 == '2':
                minta_perintah_program_1 = 'REBOOT'
            elif minta_perintah_program_1 == '3':
                minta_perintah_program_1 = 'SUSPEND'
            else:
                print('''
    (!!!) Anda memasukan nomor program yang tidak valid | harap masukan nomor yang benar
___________________________________________________________________________________________''')
                continue
            break
        except KeyboardInterrupt:
            print('''
    (!!!) Anda membatalkan program secara paksa, bye...
___________________________________________________________________________________________''')
            return
    print('''
    (^_^) Target dan perintah telah dilengkapi | Mengirimkan perintah ke node...''')
    mengirim_perintah_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mengirim_perintah_node.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    mengirim_perintah_node.sendto(minta_perintah_program_1.encode(), (minta_ip_node_program_1, 5005))
    mengirim_perintah_node.close()

    mendengarkan_respon_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mendengarkan_respon_node.bind(('', 5005))
    durasi_menunggu_respon = 30
    mendengarkan_respon_node.settimeout(durasi_menunggu_respon)
    print('''
    (>_<) Perintah terkirim ke node | menunggu balasan dari node selama 30 detik''')
    try:
        pesan_node, alamat_node = mendengarkan_respon_node.recvfrom(1024)
        pesan_node = pesan_node.decode()
        if pesan_node == 'Siap_laksanakan!':
            print('''
    (^o^) Node says : Perintah bakal dieksekusi dalam 10 detik''')
    except socket.timeout:
        print('''
    Waktu menunggu respon telah habis | Node gagal menerima perintah
___________________________________________________________________________________________''')
    except KeyboardInterrupt:
        print('''
    (!!!) Anda membatalkan proses secara paksa banget!!!
___________________________________________________________________________________________''')
def program_nomor_2():
    while True:
        try:
            minta_ip_node_program_2 = input('''
    (!) Pisahkan ip address menggunakan "|" | contoh : 192.168.10.1|192.168.10.2|...
===========================================================================================
    (^_^) Masukan ip address node-node yang akan diberikan perintah : ''').strip()
            minta_ip_node_program_2 = minta_ip_node_program_2.split('|')
            if not minta_ip_node_program_2:
                print('''
    (!!!) Anda belum memasukan ip address
___________________________________________________________________________________________''')
                continue
            break
        except KeyboardInterrupt:
            print('''
    (-_-) Anda mengentikan progran secara paksa
___________________________________________________________________________________________''')
            return
    print('''
    (~) Perintah yang bisa di berikan kepada node :
    (1) SHUTDOWN
    (2) RESTART
    (3) SLEEP''')
    try:
        while True:
            minta_perintah_progam_2 = input('''
    (^_^) Masukan nomor program yang anda pilih (1/2/3) : ''')
            if minta_perintah_progam_2 == '1':
                minta_perintah_progam_2 = 'POWEROFF'
            elif minta_perintah_progam_2 == '2':
                minta_perintah_progam_2 =  'REBOOT'
            elif minta_perintah_progam_2 == '3':
                minta_perintah_progam_2 = 'SUSPEND'
            else:
                print('''
    (!!!) Anda memasukan nomor program yang tidak valid
___________________________________________________________________________________________''')
                continue
            break
    except KeyboardInterrupt:
        print('''
    (-_-) Anda menghentikan program secara paksa
___________________________________________________________________________________________''')
        return
    print('''
    (^_<) Target dan perintah telah dilengkapi | mengirimkan perintah ke node-node...''')
    for kirim in minta_ip_node_program_2:
        mengirim_perintah_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mengirim_perintah_node.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        mengirim_perintah_node.sendto(minta_perintah_progam_2.encode(), (kirim, 5005))
        mengirim_perintah_node.close()

    mendengarkan_respon_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mendengarkan_respon_node.bind(('', 5005))
    durasi_menunggu_respon = 15
    mendengarkan_respon_node.settimeout(durasi_menunggu_respon)
    print(f'''
    (>_<) Perintah terkirim ke node | menunggu balasan dari node selama {durasi_menunggu_respon} detik''')
    try:
        while True:
            pesan_node, alamat_node = mendengarkan_respon_node.recvfrom(1024)
            pesan_node = pesan_node.decode()
            if pesan_node == 'Siap_laksanakan!':
                print('''
    (^o^) Node says : Perintah bakal dieksekusi dalam 10 detik''')
    except socket.timeout:
        print('''
    Waktu menunggu respon telah habis
___________________________________________________________________________________________''')
    except KeyboardInterrupt:
        print('''
    (!!!) Anda membatalkan proses secara paksa banget!!!
___________________________________________________________________________________________''')