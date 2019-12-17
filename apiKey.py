import requests 
import json

f = open(" ", "r")

html = f.read()

apikey = '01e25055726d94d79756dc9f3d377722251c6a627564e8ad5ae5c9fac03dbb7c'
url = 'https://html2pdf.app/profile'

# putting the API key in as data

data = {'html': html, 'apikey':apikey}
response = requests.post(url, json=data)

newFile = open(" ", "wb")
newFile.write(response.content)
print(response.status_code)