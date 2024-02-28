import requests
import datetime
import filecmp

f1 = "Versions today.txt"
f2 = "Versions yesterday.txt"

#shallow comparison
result = filecmp.cmp(f1, f2)
print(result)

#deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)

