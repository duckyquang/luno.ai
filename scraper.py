import requests
import selenium
from bs4 import BeautifulSoup
import csv


https = "https://"
starterPack = "ibo.org/programmes/"
programmes = ["middle-years-programme/", "diploma-programme/"]

index = 0

page = requests.get(https + starterPack + programmes[index])
content = BeautifulSoup(page.content, 'html.parser')

print(https + starterPack + programmes[index])
print(content)
