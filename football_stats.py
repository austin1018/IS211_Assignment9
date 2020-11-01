import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
page = requests.get(url)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("tbody")
alists = results.find_all("a")
positions = results.find_all("span",class_="CellPlayerName-position")
teams = results.find_all("span",class_="CellPlayerName-team")
tds=results.find_all("td",class_="TableBase-bodyTd TableBase-bodyTd--number")
for x in range(0, 20):
    print (str(x+1)+". "+alists[x].text+" "+positions[x].text.strip()+" "+teams[x].text.strip()+" "+tds[x*12+7].text.strip())

