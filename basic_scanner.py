import socket
from colorama import init, Fore

#colors:
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

#determine whether a port is open:
def port_is_open(host, port):
    """ Determine if 'host' has an open port """
    #create socket:
    s = socket.socket()

    #connect to port, handle errors gracefully with try-except:
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True
    
host = input("Enter the host: ")
for port in range(1, 1025):
    if port_is_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is OPEN     {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed     {RESET}", end="\r")
   
