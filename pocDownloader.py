#!/usr/bin/python3

import requests
import time
import sys

url="https://URL={}".format(sys.argv[1])

for i in range (1,500,1):
    r = requests.get(url)
    print(r.text)
    if r.status_code == 200:
        print("[+] Done. Request #{}".format(i))
    else:
        print("[-] Houston, we've had a problem here -__-") 
    time.sleep(2)
