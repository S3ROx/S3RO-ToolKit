#!/usr/bin/python
#
#       S3RO TOOLKIT v1.0
#       
#       Created By : S3RO
#       GitHub : https://github.com/S3ROx
#       
#       Disclaimer : Educational Purpose only

import os
import sys
import colorama
from colorama import Fore
import time

colorama.init(autoreset=True)


def quit():
    print(Fore.BLUE + "Thanks for using S3RO's Toolkit!. Goodbye")
    sys.exit()

def checkRoot():
    print("Checking root...")
    if os.geteuid() != 0:
        print("You need to run the script as root. Quitting program.")
        time.sleep(2)
        sys.exit()
    else:
        print(f"{Fore.GREEN}✔ You are root, running script. ✔")

checkRoot()


banner = f"""{Fore.CYAN}
███████╗██████╗ ██████╗  ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██╔════╝╚════██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
███████╗ █████╔╝██████╔╝██║   ██║   ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
╚════██║ ╚═══██╗██╔══██╗██║   ██║   ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
███████║██████╔╝██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝

{Fore.YELLOW}
<==================== Tools List ====================>
    [1] PassGenerator                   [2] Coming Soon!
    [3] Coming Soon!                    [4] Coming Soon!
    [5] Coming Soon!                    [6] Coming Soon!
    [q] Quit
"""

print(banner)

while True:
    choose = str(input(f"{Fore.YELLOW}Select an option>: "))

    if choose == "q":
        quit()
    
    elif choose == "1":
        try:
            f = open("password-generator/passgen.py")
            print(f"{Fore.CYAN}\n################### Running Password Generator ###################")
            f.close()
            os.system("python3 password-generator/passgen.py")
            sys.exit()
        except IOError:
            print("Downloading Password Generator from https://github.com/S3ROx/password-generator.")
            os.system("git clone https://github.com/S3ROx/password-generator.git")
    else:
        print(Fore.RED + "\n\nPlease choose an option from the list.\n")
        time.sleep(1.5)
        os.system("clear")
        print(banner)
