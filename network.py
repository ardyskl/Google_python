import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
print("Everything ok")
# Everything ok

import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True
    return False
def check_connectivity():
    request = requests.get('http://www.google.com')
    response = request.status_code
    if response == 200:
        return True
		return False
