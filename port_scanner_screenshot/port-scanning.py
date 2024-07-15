import socket
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure logging to save to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='port_scanner.log',  # Specify the file to save logs
    filemode='w'  # 'w' to overwrite the log file each time script runs; use 'a' to append
)

logging.info("CSN Script for Port Scanning!")

# Define the target IP address and the port range to scan
target = "127.0.0.1"
port_range = (16992, 16995)

# List to store open ports
open_ports = []

# Function to scan a single port
def scan_port(port):
    logging.debug(f"Scanning port {port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        result = sock.connect_ex((target, port))
        
        if result == 0:
            open_ports.append(port)
            logging.info(f"Port {port} is open.")
        else:
            logging.info(f"Port {port} is closed.")
    except Exception as e:
        logging.error(f"Error scanning port {port}: {str(e)}")
    finally:
        sock.close()

# Loop through the specified port range and scan each port
for port in range(port_range[0], port_range[1] + 1):
    scan_port(port)

logging.info("Open Ports:")
for port in open_ports:
    logging.info(port)

# Function to take screenshots of the given URL   
def ip_shots(url, filename):
    logging.info(f"Taking IP Shot of {url}")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.save_screenshot(filename)
        driver.quit()
        logging.info(f"Screenshot saved as {filename}")
    except Exception as e:
        logging.error(f"Error taking screenshot of {url}: {str(e)}")

# Loop through all open ports and take screenshots of the respective URLs
for port in open_ports:
    url = f"http://{target}:{port}"
    filename = f"ipshot_{target}_{port}.png"
    ip_shots(url, filename)

logging.info("Script execution completed.")
