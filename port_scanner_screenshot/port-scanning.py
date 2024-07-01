print("CSN Script for Port Scanning!\n")
 
import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
target = "192.168.16.43"
port_range = (130, 140)
 
open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        open_ports.append(port)
        
    sock.close()

for port in range(port_range[0], port_range[1] + 1):
    print("Scanning port ", port)
    scan_port(port)

print("\nOpen Ports:")

for port in open_ports:
    print(port)
    
def ip_shots(url, filename):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    driver.save_screenshot(filename)
    driver.quit()

for port in open_ports:
    url = f"http://{target}:{port}"
    filename = f"ipshot_{target}_{port}.png"
    print("Taking IP Shot of port ", port)
    ip_shots(url, filename)