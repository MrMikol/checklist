import requests
import datetime

response = requests.get("https://github.com/paritytech/polkadot-sdk/releases/latest")
polkadot = response.url.split("/").pop()

print(polkadot)

f = open('output.txt', 'a')
f.write(polkadot)