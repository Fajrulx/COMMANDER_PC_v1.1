#!/bin/bash

# ============================================
# Commander_PC - Smart Installer v1.1
# Mode: Commander atau Node
# ============================================

# Warna
MERAH='\033[0;31m'
HIJAU='\033[0;32m'
KUNING='\033[0;33m'
BIRU='\033[0;34m'
NETRAL='\033[0m'

echo -e "${BIRU}========================================${NETRAL}"
echo -e "${HIJAU}Commander_PC Smart Installer v1.1${NETRAL}"
echo -e "${BIRU}========================================${NETRAL}"

# Cek root
if [ "$EUID" -ne 0 ]; then
    echo -e "${MERAH}Gagal! Jalankan dengan: sudo bash install.sh${NETRAL}"
    exit 1
fi

# Install Python3 (jika belum)
echo -e "${KUNING}→ Mengecek Python3...${NETRAL}"
if ! command -v python3 &> /dev/null; then
    echo -e "${KUNING}→ Python3 tidak ditemukan. Menginstall...${NETRAL}"
    apt update && apt install python3 -y
    echo -e "${HIJAU}✓ Python3 berhasil diinstall.${NETRAL}"
else
    echo -e "${HIJAU}✓ Python3 sudah terinstall.${NETRAL}"
fi

# Pilih mode
echo ""
echo -e "${KUNING}Pilih mode instalasi:${NETRAL}"
echo "1) Commander_PC (Mengontrol node)"
echo "2) Node_PC (Node yang dikontrol)"
read -p "Masukkan pilihan (1/2): " mode

# ==================== COMMANDER MODE ====================
if [ "$mode" == "1" ]; then
    echo ""
    echo -e "${HIJAU}========================================${NETRAL}"
    echo -e "${HIJAU}Instalasi Commander_PC${NETRAL}"
    echo -e "${HIJAU}========================================${NETRAL}"
    
    echo -e "${KUNING}→ Membuat direktori /opt/Commander_PC...${NETRAL}"
    mkdir -p /opt/Commander_PC
    echo -e "${HIJAU}✓ Direktori berhasil dibuat.${NETRAL}"
    
    echo -e "${KUNING}→ Menyalin file commander...${NETRAL}"
    cp main.py scan.py command.py Commander /opt/Commander_PC/
    echo -e "${HIJAU}✓ File berhasil disalin.${NETRAL}"
    
    echo -e "${KUNING}→ Mengatur izin execute...${NETRAL}"
    chmod +x /opt/Commander_PC/Commander
    chmod +x /opt/Commander_PC/*.py
    echo -e "${HIJAU}✓ Izin berhasil diatur.${NETRAL}"
    
    echo -e "${KUNING}→ Membuat symlink ke /usr/local/bin/commander...${NETRAL}"
    ln -sf /opt/Commander_PC/Commander /usr/local/bin/commander
    echo -e "${HIJAU}✓ Symlink berhasil dibuat.${NETRAL}"
    
    echo -e "${KUNING}→ Membersihkan file node (jika ada)...${NETRAL}"
    rm -f /opt/Commander_PC/System_node.py 2>/dev/null
    rm -f /opt/Commander_PC/System_node.service 2>/dev/null
    echo -e "${HIJAU}✓ Pembersihan selesai.${NETRAL}"
    
    echo ""
    echo -e "${HIJAU}========================================${NETRAL}"
    echo -e "${HIJAU}Instalasi Commander_PC selesai!${NETRAL}"
    echo -e "${HIJAU}Ketik 'commander' untuk menjalankan.${NETRAL}"
    echo -e "${HIJAU}========================================${NETRAL}"

# ==================== NODE MODE ====================
elif [ "$mode" == "2" ]; then
    echo ""
    echo -e "${HIJAU}========================================${NETRAL}"
    echo -e "${HIJAU}Instalasi Node Agent${NETRAL}"
    echo -e "${HIJAU}========================================${NETRAL}"
    
    echo -e "${KUNING}→ Mengecek sudo...${NETRAL}"
    if ! command -v sudo &> /dev/null; then
        echo -e "${KUNING}→ Sudo tidak ditemukan. Menginstall...${NETRAL}"
        apt update && apt install sudo -y
        echo -e "${HIJAU}✓ Sudo berhasil diinstall.${NETRAL}"
    else
        echo -e "${HIJAU}✓ Sudo sudah terinstall.${NETRAL}"
    fi
    
    echo -e "${KUNING}→ Membuat direktori /opt/System_node...${NETRAL}"
    mkdir -p /opt/System_node
    echo -e "${HIJAU}✓ Direktori berhasil dibuat.${NETRAL}"
    
    echo -e "${KUNING}→ Menyalin file node...${NETRAL}"
    cp System_node.py /opt/System_node/
    cp System_node.service /opt/System_node/
    echo -e "${HIJAU}✓ File berhasil disalin.${NETRAL}"
    
    echo -e "${KUNING}→ Mengatur izin execute...${NETRAL}"
    chmod +x /opt/System_node/System_node.py
    echo -e "${HIJAU}✓ Izin berhasil diatur.${NETRAL}"
    
    echo -e "${KUNING}→ Memasang service systemd...${NETRAL}"
    cp /opt/System_node/System_node.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable System_node.service
    systemctl start System_node.service
    echo -e "${HIJAU}✓ Service berhasil dipasang dan diaktifkan.${NETRAL}"
    
    echo -e "${KUNING}→ Membersihkan file commander (jika ada)...${NETRAL}"
    rm -f /opt/System_node/main.py 2>/dev/null
    rm -f /opt/System_node/scan.py 2>/dev/null
    rm -f /opt/System_node/command.py 2>/dev/null
    rm -f /opt/System_node/Commander 2>/dev/null
    echo -e "${HIJAU}✓ Pembersihan selesai.${NETRAL}"
    
    echo -e "${KUNING}→ Menambahkan izin sudo untuk poweroff, reboot, suspend...${NETRAL}"
    if ! grep -q "poweroff" /etc/sudoers; then
        echo "%sudo ALL=(ALL) NOPASSWD: /usr/sbin/poweroff, /usr/sbin/reboot, /usr/bin/systemctl suspend" >> /etc/sudoers
        echo -e "${HIJAU}✓ Izin sudo berhasil ditambahkan.${NETRAL}"
    else
        echo -e "${HIJAU}✓ Izin sudo sudah ada.${NETRAL}"
    fi
    
    echo ""
    echo -e "${HIJAU}========================================${NETRAL}"
    echo -e "${HIJAU}Instalasi Node Agent selesai!${NETRAL}"
    echo -e "${HIJAU}Cek status: systemctl status System_node.service${NETRAL}"
    echo -e "${HIJAU}========================================${NETRAL}"

else
    echo -e "${MERAH}Pilihan tidak valid!${NETRAL}"
    exit 1
fi