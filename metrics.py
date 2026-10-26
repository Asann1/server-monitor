import time
import psutil
 
while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    count = psutil.cpu_count()
 
    print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}% | Count: {count}")
 
    time.sleep(1)
 
