# Port Scanner Automation

## Introduction
This project is a simple port scanner script that scans a range of ports on a specified target IP address and takes screenshots of accessible web interfaces.

## Prerequisites

- Python 3x
- Selenium WebDriver for Chrome

## Installation - install the required Python packages

```pip install selenium```

## Usage 
1. Run the script
2. The script will scan the specified port range and log the results in `port_scanner.log`
3. Screenshots of accessible web interfaces will be saved in the current directory

## Explanation of the code
The code is divided into several parts, each handling different aspects of the port scanning, screenshot, and logging process.

### Importing Necessary Libraries
```
import socket
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
```
- `socket`: This library creates network configurations and performs port scanning.
- `logging`: This module logs information, errors, and debugging messages to a file.
- `selenium`: This library automates web browser interactions, which helps in taking screenshots of web interfaces.

### Configuring Logging
```
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='port_scanner.log',
    filemode='w'
)

logging.info("CSN Script for Port Scanning!")

```
- Logging is configured to save logs to a file named `port_scanner.log`. The log level is set to `INFO`, and the log file is overwritten each time the script runs.

### Defining Target and Port Range
```
target = "127.0.0.1"
port_range = (16992, 16995)
```
- `target`: Specifies the IP address to scan. In this example, it is set to the local host `(127.0.0.1)`.
- `port_range`: Defines the range of ports to scan. Here, the range is set from 16992 to 16995.

### List to Store Open Ports
```open_ports = []
```
- An empty list to store the ports that are found to be open during the scan.

### Function to Scan a Single Port
```
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
```
- `scan_port(port)`: This function connects to a specified port on the target IP address.
- If the connection is successful (returns 0), the port is considered open and added to the open_ports list.
- If the connection fails, the port is considered closed.
- Any errors encountered during the connection attempt are logged.

### Scanning the Specified Port Range
```
for port in range(port_range[0], port_range[1] + 1):
    scan_port(port)
```
- This loop iterates through the specified range of ports and calls the scan_port function for each port.

### Logging Open Ports
```
logging.info("Open Ports:")
for port in open_ports:
    logging.info(port)
```
- This section logs the list of open ports found during the scan.

### Function to Take Screenshots of Given URL
```
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
```
- `ip_shots(url, filename)`: This function uses Selenium to open a web browser and take a screenshot of the specified URL.
- The browser runs in headless mode, which means it operates without a graphical user interface.
- If the URL is accessible, a screenshot is saved with the specified filename.

 ###  Taking Screenshots of Open Ports
 ```
for port in open_ports:
    url = f"http://{target}:{port}"
    filename = f"ipshot_{target}_{port}.png"
    ip_shots(url, filename)
```
- This loop iterates through the list of open ports and takes screenshots of the web interfaces running on those ports.

### Completion Message
```
logging.info("Script execution completed.")
```
- Logs a message indicating that the script has finished executing.

## Conclusion
This script demonstrates how to perform port scanning using Python and how to automate the process of taking screenshots of web interfaces on open ports. The results are logged for review and analysis.







