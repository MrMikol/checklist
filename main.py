import requests
import datetime

#print(polkadot)

#f = open('output.txt', 'a')
#f.write(polkadot)

def printVersions():
    response = requests.get("https://github.com/paritytech/polkadot-sdk/releases/latest")
    polkadot = response.url.split("/").pop()

    f = open('output.txt', 'w')
    f.write("The latest version of Polkadot is " + polkadot)

printVersions()