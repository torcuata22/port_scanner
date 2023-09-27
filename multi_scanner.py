import argparse
import socket
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

#number of threads:
N_THREADS = 200
#thread queue:
q = Queue()
print_lock = Lock()

host = None

def port_scan(port):
    """ Scans a port belonging to 'host' """
    try:
        s = socket.socket()
        s.connect((host, port))
    
    except:
        with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is CLOSED    {RESET}")
    
    else:   
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is OPEN    {RESET}")

    finally:
        s.close()


#populate queue:
def scan_thread():
    """Get port numbers from the queue and scan them, then add to tasks"""
    global q
    while True:
        worker = q.get() #get port number from the queue
        port_scan(worker) #scan that port number
        q.task_done() #indicates that task is finished

def main(host, ports):
    """fills up the queue with port numbers and spawns threads to consume the port numbers"""
    global q
    for t in range(N_THREADS):
        t = Thread(target = scan_thread)
        #create daemon thread to run in background
        t.daemon = True 
        #start daemon thread:
        t.start()
    for worker in ports:
        q.put(worker) #places each port in the queue
    #wait for threads to finihs:
    q.join()

#Argument parser to pass host and port number from command line:
if __name__ == "__main__":
    #parse parameters:
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("host", help="Host to scan")
    parser.add_argument("--ports", "-p", dest = "port_range", default="1-65535", help="Port range to be scanned. Default: all ports (1 - 65535)")
    args = parser.parse_args()

    if args.host:
        host = args.host
    

    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [p for p in range(start_port, end_port)]

    main(host, ports)

#run and print scan results: python multi_scanner.py <ip address> | tee scan_results.txt