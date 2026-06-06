#!/usr/bin/env python3

import scan
import command

def Commander_PC():
    print('''
___________________________________________________________________________________________

     ██████╗ ██████╗ ███╗   ███╗███╗   ███╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║██╔████╔██║██╔████╔██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║
     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                Commander_PC v1.1
                                   by: Fajrulx
___________________________________________________________________________________________

    Halo, kamu sedang menggunakan Commander_PC, tool ini dapat membantu kamu mengelola
    perangkat dalam satu jaringan. Seperti Sleep, Restart, dan Shutdown perangkat dari
    perankgat lain. Silahkan memiliki prgram yang telah tersedia!
___________________________________________________________________________________________
    ''')

def Opsi_program():
    print('''
    (~) Program yang tersedia :
    (0) Batalkan penggunaan Commander_PC
    (1) Scan area, untuk melihat node yang ada di dalam jaringan
    (2) Command for node, untuk memberikan perintah Sleep, Restart, dan Shutdown pada node
    ''')

def main():
    Commander_PC()
    try:
        while True:
            Opsi_program()
            pilihan = input('''
    (~) Masukan pilihan anda : ''')
            print('''
___________________________________________________________________________________________''')
        
            if pilihan == "1":
                print("\n (+) Scan area, terpilih")
                scan.Scan()
            elif pilihan == "2":
                print("\n (+) Command for node, terpilih ")
                command.Command()
            elif pilihan == "0":
                print("\n (+) Terima kasih telah menggunakan Commander_PC :) ")
                break
            else:
                print("\n (!!!) Pilihan tidak valid, masukan pilihan dengan benar!")
    except KeyboardInterrupt:
        print('''
    (!!!) Anda membatalkan program Commander_pc secara paksa (-_-)''')
if __name__ == "__main__":
    main()