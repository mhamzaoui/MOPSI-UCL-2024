from bs4 import BeautifulSoup
import requests

#UEFA clubs ranking extraction

url = 'https://kassiesa.net/uefa/data/method5/trank2023.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
data = soup.find_all('tr', class_ = 'clubline')
data_adap = [list(filter(None,data[i].getText().split('\n'))) for i in range(36)]

Teams = []
for e in data_adap:
    if len(e[0]) > 2:
        Teams.append(e[:2])
    else:
        Teams.append(e[1:][:2])
#Pots
PotA = Teams[:9]
PotB = Teams[9:18]
PotC = Teams[18:27]
PotD = Teams[27:36]
