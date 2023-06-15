#youtube efe apak
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""

██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      @apakbilisim
"""+red)
print (lgreen+bold+"         <===[[ Alem Küçüktür İtibar Büyüktür ]]===> \n"+clear)
print (yellow+bold+"   <---(( YOUTUBE : EFE APAK ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[KURBAN]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[TELEKOMUNİKASYON]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Şehir]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Şehir Kodu]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[BOYLAM]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[ENLEM]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Saat Dilimi]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Posta Kodu]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('hoşçakal'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" internet bağlantınızı kontrol edin!"+clear)
sys.exit(1)
