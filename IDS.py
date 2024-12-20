import os
import re
import json
import base64
from datetime import datetime

# Constants
LOG_FILE = 'network.log'
ALERT_FILE = 'alerts.json'
SUSPICIOUS_IPS = ['192.168.1.5', '10.0.0.2']

# Check if an IP address is suspicious
def is_ip_suspicious(ip):
    return ip in SUSPICIOUS_IPS

# Generate an encoded alert message
def generate_alert_message(log_entry):
    message = f"Suspicious activity detected: {log_entry}"
    return base64.b64encode(message.encode()).decode()

# Save the alert to a file
def log_alert(encoded_alert):
    with open(ALERT_FILE, "a") as alert_file:
        alert_data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'alert': encoded_alert
        }
        json.dump(alert_data, alert_file)
        alert_file.write('\n')  # Newline for better formatting

# Main IDS functionality
def main():
    alerts = []

    # Read and analyze the log file
    with open(LOG_FILE, 'r') as file:
        for line in file:
            # Using regex to extract IP 
            ip_search = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)
            if ip_search:
                ip = ip_search.group()
                if is_ip_suspicious(ip):
                    alerts.append(line.strip())

    # Process and log alerts
    for alert in alerts:
        encoded_alert = generate_alert_message(alert)
        log_alert(encoded_alert)

    # Provide feedback to the user
    if alerts:
        print(f"[!] {len(alerts)} suspicious activities detected! Check {ALERT_FILE} for details.")
    else:
        print("[+] No suspicious activities detected.")

if __name__ == "__main__":
    main()
