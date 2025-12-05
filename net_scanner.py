import scapy.all as scapy
import argparse
import os

oui_data = {}

def load_oui_data(oui_file_path):
    global oui_data
    with open(oui_file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "(hex)" in line:
                parts = line.split("(hex)")
                oui = parts[0].replace('-', '').strip()
                vendor = parts[1].strip()
                oui_data[oui] = vendor

def get_vendor(mac_address):
    oui = mac_address.replace(':', '')[:6].upper()
    return oui_data.get(oui, "Unknown Vendor")

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        mac = element[1].hwsrc
        vendor = get_vendor(mac)
        client_dict = {"ip": element[1].psrc, "mac": mac, "vendor": vendor}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\t\t\tVendor\n-------------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"] + "\t\t" + client["vendor"])

script_dir = os.path.dirname(os.path.abspath(__file__))
oui_file = os.path.join(script_dir, "oui.txt")
load_oui_data(oui_file)

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)


