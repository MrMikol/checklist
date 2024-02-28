import requests
import datetime

#print(polkadot)

#f = open('output.txt', 'a')
#f.write(polkadot)

github = ["https://github.com/paritytech/polkadot-sdk/releases/latest", "https://github.com/prysmaticlabs/prysm/releases/latest", "https://github.com/rocket-pool/smartnode-install/releases/latest", "https://github.com/ethereum/go-ethereum/releases/latest"]
date = datetime.datetime.now()

def printVersions(github, date):
    f.write(str(date.strftime("%x")) + '\n')
    response = requests.get(github[0])
    polkadot = response.url.split("/").pop()

    f = open('output.txt', 'w')
    f.write("The latest version of Polkadot is " + polkadot)

printVersions(github, date)