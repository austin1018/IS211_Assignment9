import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL&guccounter=1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
page = requests.get(url, headers=headers)
# print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find("tbody",class_="historical-data__table-body")
#
# print(results)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("table",class_="W(100%) M(0)")
tbody = results.find("tbody")
spans = tbody.find_all("span")
x=0
print("Date\t\t\tClose Price")
printout=""
for span in spans:
    # print(span.text)
    x=x+1
    if span.text=="Stock Split" or span.text=="Dividend":
        x=0
    if x%7==1:
        printout=span.text
    if x%7==5:
        print(printout+"\t"+span.text)


# print(results)
# alists = results.find_all("a")
# positions = results.find_all("span",class_="CellPlayerName-position")
# teams = results.find_all("span",class_="CellPlayerName-team")
# tds=results.find_all("td",class_="TableBase-bodyTd TableBase-bodyTd--number")
# for x in range(0, 20):
#     print (str(x+1)+". "+alists[x].text+" "+positions[x].text.strip()+" "+teams[x].text.strip()+" "+tds[x*12+7].text.strip())

