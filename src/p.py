#   This project is only for educational propsites!
#   In case for use this code for illegal conduct no is my responsibility
#
#   Python Pinger
#   This software is maden by Coded. Visit coded.today

import os
import sys
import colorama
import random
import time
from colorama import *
import urllib, json
colorama.init()

os.system("mode con cols=35 lines=5")

def ping():
    print(Fore.LIGHTCYAN_EX)
    hostname = sys.argv[1]
    print(" ")

    if "." in hostname:
        cont = 1
        while True:
            response = os.system("ping " + hostname + " -n 1 >nul")
            if response == 0:
                print(Fore.LIGHTGREEN_EX + "STATUS: OK! [" + str(cont) + "]" + Fore.WHITE + " from " + Fore.LIGHTBLACK_EX + hostname)
            else:
                print(Fore.LIGHTRED_EX + "STATUS: BAD! [" + str(cont) + "]" + Fore.WHITE + " from " + Fore.LIGHTBLACK_EX + hostname)
            cont += 1
            time.sleep(.5)
    else:
        print("Please input a valid hostname!")
        print(" ")
        ping()
        

ping()