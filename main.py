import requests
import datetime


github = []
date = datetime.datetime.now()

with open('links.txt', 'r') as file:
    github = file.read().splitlines()

f = open('Versions today.txt', 'w')

def printVersions(github, date):
    f.write(str(date.strftime("%x")) + '\n')
    i = 0
    for version in github:
        response = requests.get(github[i])
        name1 = response.url.split("/").pop(3)
        name2 = response.url.split("/").pop(4)
        version = response.url.split("/").pop()

        f.write("Chain: " + str(name1) + " " + str(name2) + "\n")
        f.write("Latest version: " + str(version) + "\n")
        f.write("\n")

        i += 1

printVersions(github, date)