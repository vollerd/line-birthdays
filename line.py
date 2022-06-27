from bs4 import BeautifulSoup
import requests
import urllib.request
import time

### Message to send
peeps = "\n↓It is these peoples birthday today!↓\n"

### URL to scrape from
url = "https://www.thefamouspeople.com/famous-people-born-today.php"

response = requests.get(url)  #check if page exists or not
if str(response) == "<Response [200]>": #only do stuff if exists, otherwise just skip
    time.sleep(0.040)
    #parse html and save to beautiful soup object
    soup = BeautifulSoup(response.text, "html.parser")


### pick out the names only (first 11)
soop = str(soup).split("Listed In")  ### split the page into chunks around "Listed In"
for i in range(0,11):
    peeps=peeps+(soop[i].split("column")[1].split(">")[2].split("<")[0])  ### Remove the trim around the name from each block
    if i<10:
        peeps=peeps+("\n") ### Append the message with persons name and a line break

### Line bit
url = "https://notify-api.line.me/api/notify"
token = ''
payload = {'message' : peeps}
headers = {"Authorization" : "Bearer "+ token}
r = requests.post(url
                , headers={'Authorization' : 'Bearer {}'.format(token)}
                , params = payload)
files = {"imageFile":open('gazo.jpeg','rb')}
post = requests.post(url ,headers = headers ,params=payload,files=files)