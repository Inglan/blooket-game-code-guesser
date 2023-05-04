import requests

bsid = input('Enter BSID: ')

from requests.structures import CaseInsensitiveDict

url = "https://fb.blooket.com/c/firebase/id?id=1234567"

headers = CaseInsensitiveDict()
headers["cookie"] = "bsid="+bsid


resp = requests.get(url, headers=headers)

print(resp.text)

