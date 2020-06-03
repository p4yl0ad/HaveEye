#!/usr/bin/python3

#api endpoint browser compatible https://www.dynarisk.com/home/data-breach-scanner

import requests
from pwn import *

topost = "https://dynarisk.com"
apiend = "/api/v1/scan/email"

token = "ICtqFI03Ne384S7LaN9XtuxiAqrwOZYeUiwNiiN1"
email = input("Input your email pls > ")

data = { '_token': token,
         'email': email }
r =  requests.post(url = topost + apiend, data = data)
output = r.text
#print(output)
if '"breach_contains":0' in output:
    log.success("Congrats You're Safe")
else:
    log.failure("You're Compromised Chief")

#TODO
#add option to send report to email :)
