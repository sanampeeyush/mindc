#!/bin/bash

# Backup directory
backup_dir="/home/pi/Desktop/mindCharger/backup"

# Function to restore backups
restore_backup() {
    local file="$1"
    local backup_file="$backup_dir/$(basename $file).bak"
    if [ -f "$backup_file" ]; then
        cp "$backup_file" "$file"
    fi
}

# Step 1: Revert Changes

# Restore dhcpcd.conf
restore_backup "/etc/dhcpcd.conf"

# Restore hostapd.conf
restore_backup "/etc/hostapd/hostapd.conf"

# Restore dnsmasq.conf
restore_backup "/etc/dnsmasq.conf"

# Stop and disable services
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq

# Restore sysctl.conf
restore_backup "/etc/sysctl.conf"

# Disable IP Forwarding
sudo sed -i '/net.ipv4.ip_forward=1/s/^/#/' /etc/sysctl.conf
sudo sysctl -p

# Flush iptables rules
sudo iptables -F

# Remove iptables save file
sudo rm /etc/iptables.ipv4.nat

# Remove iptables-restore command from rc.local
sudo sed -i '/iptables-restore < \/etc\/iptables.ipv4.nat/d' /etc/rc.local

# Reboot
echo "Reverting changes. Rebooting your Raspberry Pi..."
sudo reboot
