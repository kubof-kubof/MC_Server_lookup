import requests
import time
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.GREEN}
 ██████   ██████   █████████      █████████                                                   
░░██████ ██████   ███░░░░░███    ███░░░░░███                                                  
 ░███░█████░███  ███     ░░░    ░███    ░░░   ██████  ████████  █████ █████  ██████  ████████ 
 ░███░░███ ░███ ░███            ░░█████████  ███░░███░░███░░███░░███ ░░███  ███░░███░░███░░███
 ░███ ░░░  ░███ ░███             ░░░░░░░░███░███████  ░███ ░░░  ░███  ░███ ░███████  ░███ ░░░ 
 ░███      ░███ ░░███     ███    ███    ░███░███░░░   ░███      ░░███ ███  ░███░░░   ░███     
 █████     █████ ░░█████████    ░░█████████ ░░██████  █████      ░░█████   ░░██████  █████    
░░░░░     ░░░░░   ░░░░░░░░░      ░░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░     ░░░░░░  ░░░░░     
                                                                                              
 █████                         █████                                                          
░░███                         ░░███                                                           
 ░███         ██████   ██████  ░███ █████ █████ ████ ████████                                 
 ░███        ███░░███ ███░░███ ░███░░███ ░░███ ░███ ░░███░░███                                
 ░███       ░███ ░███░███ ░███ ░██████░   ░███ ░███  ░███ ░███                                
 ░███      █░███ ░███░███ ░███ ░███░░███  ░███ ░███  ░███ ░███                                
 ███████████░░██████ ░░██████  ████ █████ ░░████████ ░███████                                 
░░░░░░░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░  ░███░░░                                  
                                                     ░███                                     
                                                     █████                                    
                                                    ░░░░░
Minecraft server lookup tool made by Kubof
"""

def get_server_info(ip):
    url = f"https://api.mcsrvstat.us/2/{ip}"
    response = requests.get(url)
    data = response.json()
    
    print(f"{Fore.BLUE}[DEBUG] Request time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[DEBUG] Status Code: {response.status_code}")
    
    if data["online"]:
        print(f"\n{Fore.MAGENTA}Server IP: {ip}")
        print(f"{Fore.GREEN}Status: Online")
        print(f"Players: {data['players']['online']} / {data['players']['max']}")
        print(f"Version: {data['version']}")
        print("MOTD:", ' '.join(data['motd']['clean']))

        if "list" in data["players"]:
            print("Players online:")
            for player in data["players"]["list"]:
                print(f" - {player}")
    else:
        print(f"\n{Fore.MAGENTA}Server IP: {ip}")
        print(f"{Fore.GREEN}Status: Offline")

    print(f"\n{Fore.GREEN}For graphical details, copy the link below:")
    print(f"https://mcsrvstat.us/server/{ip}")

print(banner)

server_ip = input(f"{Fore.MAGENTA}Enter the IP address of the Minecraft server: ")

while True:
    response = os.system(f"ping -c 1 {server_ip}" if os.name != "nt" else f"ping -n 1 {server_ip}")
    
    if response == 0:
        print(f"\n{Fore.BLUE}[INFO] Server is reachable. Fetching data...")
        get_server_info(server_ip)
    else:
        print(f"\n{Fore.BLUE}[INFO] Server is unreachable. Retrying in 30 seconds...")

    time.sleep(30)
