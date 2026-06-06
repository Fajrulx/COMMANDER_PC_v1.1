import socket
import time

def Scan():
    while True:
        try:
            durasi_scanning = int(input('''
    (^_-) Masukan waktu durasi scan yang bakal di lakukan (Masukan angka saja) : '''))
            if durasi_scanning <= 0:
                print('''
    (!!!) Waktu durasi tidak valid''')
                continue
            break
        except ValueError:
            print('''
    (!!!) Waktu durasi tidak valid''')
        except KeyboardInterrupt:
            print('''

    (!!!) Anda membatalkan penggunaan program scan node (-_-)
___________________________________________________________________________________________''')
            return
    print(f'''
    Scanning selama {durasi_scanning} detik...
___________________________________________________________________________________________''')
    panggil_node = 'Node!'

    panggil = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    panggil.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    panggil.sendto(panggil_node.encode(), ('255.255.255.255', 5005))
    panggil.close()


    pendengar_balasan = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pendengar_balasan.bind(('', 5005))
    pendengar_balasan.settimeout(durasi_scanning)
    jumlah_node_kedetect = []
    try:
        while True:
            pesan_balasan, sumber_balasan = pendengar_balasan.recvfrom(100000)
            jumlah_node_kedetect.append(pesan_balasan.decode())
            print(f'''
    (!) Node terdeteksi : {pesan_balasan.decode()}
        Sumber_node     : {sumber_balasan}''')
    except socket.timeout:
        total_node_kedetect = len(jumlah_node_kedetect)
        print(f'''
___________________________________________________________________________________________

    Durasi scanning telah selesai | Jumlah node terdeteksi : ({total_node_kedetect})
___________________________________________________________________________________________
        ''')
    except KeyboardInterrupt:
        total_node_kedetect = len(jumlah_node_kedetect)
        print(f'''
    (!!!) Anda membatalkan proses scan secara paksa | jumlah node terdeteksi : ({total_node_kedetect})
___________________________________________________________________________________________''')
    finally:
        pendengar_balasan.close()