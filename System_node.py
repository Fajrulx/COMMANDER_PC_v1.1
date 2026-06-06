#!/usr/bin/env python3

import socket
import subprocess
import sys
import time

def Node():

    Identitas_Node = 'Nama_Node = PC_Node_1 | ID_Node = 000001'
    print('''
    (^_^) Node aktif!
    (-_-) Node menunggu panggilan dari commander...''')

    mendengarkan_panggilan = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mendengarkan_panggilan.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mendengarkan_panggilan.bind(('', 5005))

    while True:
        pesan_panggilan, sumber_panggilan = mendengarkan_panggilan.recvfrom(100000)
        pesan_commander = pesan_panggilan.decode()
        ip_address_commander = sumber_panggilan[0]

        if pesan_commander == 'Node!':
            print('''
    (>_<) Pesan panggilan telah diterima | Mengirimkan informasi node ke commander
    (-_-) Node menunggu panggilan baru lagi dari commander...''')
            balas_panggilan = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            balas_panggilan.sendto(Identitas_Node.encode(), (ip_address_commander, 5005))
            balas_panggilan.close()


        elif pesan_commander in ["POWEROFF", "REBOOT", "SUSPEND"]:
            print('''
    (^_^) Perintah telah di terima
    (>_o) Mengirim respon kembali ke commander sebelum menjalanakan perintah commander''')
            jawab_commander = 'Siap_laksanakan!'
            balas_perintah = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            balas_perintah.sendto(jawab_commander.encode(), (ip_address_commander, 5005))
            balas_perintah.close()

            time.sleep(10)

            if pesan_commander == "POWEROFF":
                subprocess.run(["sudo", "poweroff"])
            elif pesan_commander == "REBOOT":
                subprocess.run(["sudo", "reboot"])
            elif pesan_commander == "SUSPEND":
                subprocess.run(["sudo", "systemctl", "suspend"])
Node()