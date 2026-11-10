import time
import psutil
import requests

API_URL = "http://127.0.0.1:8000/metrics"

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    metrics = {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
    }

    try:
        response = requests.post(API_URL, json=metrics, timeout=5)
        if response.status_code == 200:
            print(f"Sent -> CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")
        else:
            print(f"Server error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send metrics: {e}")

    time.sleep(4)