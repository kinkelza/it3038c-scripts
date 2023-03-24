from bs4 import BeautifulSoup
import requests, re

url = "https://www.gamestop.com/consoles-hardware/xbox-series-x%7Cs/consoles/products/microsoft-xbox-series-x/11108371.html"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
content = response.text
soup = BeautifulSoup(content, "html.parser")
# Verification to verify URL can be hit and printed from
# print(soup.prettify())

NewPrice = soup.find("span", class_ = "actual-price")
print(NewPrice)

title = soup.find("h1", class_ = "product-name h2")
print(title)

print("Item %s has price %s" % (title, NewPrice))
