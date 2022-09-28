#4BDERAHIM
import socket
import os
import sys
import time
import urllib.request, json
SERVER = 'erver:' 
STATES = [" OPEN",
          " NOT OPEN",]
REQUEST = b'GET / HTTP/1.1\r\n'
output = {"PORT":["SERVICE","STATE","VERSION"]}
def connection():
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def startconnection(target_ip, port):
    state = 0
    if state==0:
        so = socket.socket()
        try:
            so.connect((target_ip, int(port)))
            so.send(REQUEST+b'Host:%s\r\n\r\n'%target.encode())
            recv_ = so.recv(33333)
        except TimeoutError: 
            recv_ = 0
        so.close()
        output[port] = [get_port(port),STATES[0],port_server(recv_,port)]
    else:
        output[port] = [get_port(port),STATES[1],' '] 
def port_server(data,port):
    if data==0:
        return ''
    data = str(data).replace("b'",'')
    if SERVER in data:
        data_ = data[int(data.find(SERVER)):]
        final_data = data_[0:int(data_.find("\\n"))].replace('\\r','')
        return final_data[data_.find(' ')+1:]
    if data.count('\\r\\n')==1:
        return str(data[0:data.find('\\')].replace('\\r\\n',''))
    return ''
def get_ip(target):
    try:
        return socket.gethostbyname(target)
    except Exception:
        print(f"[-] unvalid target ({target})")
        sys.exit()
    
def get_port(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "UNKNOWN"
def get_location(host):
        try:
            addr = urllib.request.urlopen("https://geolocation-db.com/json/"+ host +"&position=true")
        except urllib.error.URLError:
            print("[-] Connection Failed.")
            sys.exit()
        data = json.loads(addr.read().decode())
        country = 'country_name'
        city = 'city'
        country = data.get(country) if data.get(country) else "NOT FOUND"
        city = data.get(city) if data.get(city) else "NOT FOUND"
        return [country,city]
def RunTime(_time, minutes = None):# : ) 
    
    if minutes:
        _time = int(_time)
        x = str(_time/60)
        x = int(x[:x.find('.')])
        time_SEC = _time - ((60)*(x))
        return float("%s.%s"%(x,time_SEC)), 'Minutes'
    _time = str(_time)
    return float(_time [:_time.find('.')+3]), 'Seconds'

if __name__ == "__main__":
    scanned = False
    try:
        target = get_ip(sys.argv[1]) if len(sys.argv) > 1 else get_ip(input("Type Host (www.example.com):"))
    except KeyboardInterrupt:
        print("\n[KeyboardInterrupt]")
        sys.exit()
    
    print(f"\n[!] Starting..\n[!] Target : '{target}'\n")
    start = time.time()
    for port in list([80,443,21,110]):#,443,110,21,25,22] > add or remove Ports Here!
        target = socket.gethostbyname(target)
        startconnection(target,port)
        scanned  = True
        
    if scanned:
        for key,value in output.items():
            service,state,version = value
            print("{:<8}{:<14}{:<12}{:<10}".format(key, service,state,version))
        C,C1 = get_location(target)
        print("\n[+] Server IP      : %s"%target)
        print("[+] Server country : %s"%C)
        print("[+] Server city    : %s\n\n"%C1)
        runtime = time.time()-start
        RT = RunTime(runtime) if runtime < 60 else RunTime(runtime, True)
        print("[!] Scanned in %s %s\n"%(RT[0],RT[1]))

os.system("pause")

