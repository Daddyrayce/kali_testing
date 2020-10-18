import time
import os
import sys
import socket 
import subprocess
import ipinfo
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


def Main():
    os.system(f"figlet -f slant GayNiggaSec |lolcat -a")

    time.sleep(2)
    os.system("clear")

    os.system(f"figlet -f slant GayNiggaSec |lolcat")
    print("Options\n(1)IP Scanner\n(2)IP Geolocation\n(3)DNS lookup\n(4)Phone Number Information\n(5)Nameserver for domain\n\n")
    option = input("Select>")
    if option == "1":
        option_1()
    if option == "2":
        option_2()
    if option == "3":
        option_3()
    if option == "4":
        option_4()
    if option == "5":
        option_5()




def option_1():
    for ping in range(1,225): 
        address = "192.168.1." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address]) 
        if res == 0: 
            print( "ping to", address, "OK") 
        elif res == 2: 
            print("no response from", address) 
        else: 
            print("ping to", address, "failed!") 

def option_2():
    handler = ipinfo.getHandler(access_token='Get Access Token from ipinfo.io')
    ip_address = input(str("IP>"))
    details = handler.getDetails(ip_address)
    print("*" * 60)
    print(f"IP INFO FOR {ip_address}")
    print("*" * 60)
    print("")
    print("*" * 30)
    print("City info!")
    print(f"City>{details.city}")
    print(f"Postal>{details.postal}")
    print(f"Timezone>{details.timezone}")
    print("*" * 30)
    print(f"Country>{details.country}")
    print(f"Country Name>{details.country_name}")
    print(f"Latitude>{details.latitude}")
    print(f"Longitude>{details.longitude}")
    time.sleep(5)

def option_3():
    DNS = input("Domain IP: ")
    addr = socket.gethostbyaddr(str(DNS))
    print(addr)

def option_4():
    phone_input = input("Phone number with country code: ")
    phone_number = phonenumbers.parse(phone_input) 

    print("Location>" + geocoder.description_for_number(phone_number,  
                                      'en'))    
    print("Carrier>" + carrier.name_for_number(phone_number, 
                                        "en"))


Main()