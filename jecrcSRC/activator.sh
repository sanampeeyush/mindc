#!/bin/bash

# Backup directory
backup_dir="/home/pi/Desktop/mindCharger/backup"

# Function to create backups
create_backup() {
    local file="$1"
    local backup_file="$backup_dir/$(basename $file).bak"
    cp "$file" "$backup_file"
}

# Step 1: Initial Setup

# Create a backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Install required packages
sudo apt update
sudo apt install -y hostapd dnsmasq

# Backup dhcpcd.conf
create_backup "/etc/dhcpcd.conf"

# Configure static IP for wlan0
cat <<EOL | sudo tee -a /etc/dhcpcd.conf
interface wlan0
static ip_address=192.168.4.2/24
static routers=192.168.4.1
static domain_name_servers=8.8.8.8 8.8.4.4
EOL

# Backup hostapd.conf
create_backup "/etc/hostapd/hostapd.conf"

# Configure HostAPD
cat <<EOL | sudo tee -a /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=mindCharger
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=Mind1234
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOL

# Backup dnsmasq.conf
create_backup "/etc/dnsmasq.conf"

# Configure dnsmasq
cat <<EOL | sudo tee -a /etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.4.100,192.168.4.200,255.255.255.0,24h
EOL

# Start and enable services
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo systemctl start hostapd
sudo systemctl start dnsmasq

# Backup sysctl.conf
create_backup "/etc/sysctl.conf"

# Enable IP Forwarding
sudo sed -i '/net.ipv4.ip_forward=1/s/^#//' /etc/sysctl.conf
sudo sysctl -p

# Set up NAT
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

# Save iptables rules
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

# Backup rc.local
create_backup "/etc/rc.local"

# Add iptables-restore command to rc.local
sudo sed -i -e '$i \iptables-restore < /etc/iptables.ipv4.nat\n' /etc/rc.local

# Reboot
echo "Configuration completed. Rebooting your Raspberry Pi..."
sudo reboot
