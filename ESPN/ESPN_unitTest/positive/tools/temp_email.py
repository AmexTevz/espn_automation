import requests
import hashlib
import random
import string

domain = '@cevipsa.com'
random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15)) + domain
m = hashlib.md5()
m.update(random_email.encode('utf-8'))
final = m.hexdigest()
url = f"https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/{final}/"
headers = {
    "X-RapidAPI-Key": "86afbd5139mshb9de0f629487999p1013b8jsn5a93b76c17c9",
    "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
}
response = requests.get(url, headers=headers)
passcode = response.json()
