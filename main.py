from bs4 import BeautifulSoup
import requests

# recupère le cours du btc
url = "https://coinmarketcap.com/fr/currencies/bitcoin/"
responseUrl = requests.get(url).text
soup = BeautifulSoup(responseUrl, 'html.parser')
getCourseOfBtc = soup.find_all("div", class_="priceValue")

for span in getCourseOfBtc:
  courseOfBtc = span.text # prix du cours

 # suppe la virgule et le signe €, convertit en float
deleteTheSignEuro = courseOfBtc[1:]
deleteTheComma = float(deleteTheSignEuro.replace(',', ''))
courseOfBtcFinal = deleteTheComma

print("Le prix du btc est de", courseOfBtcFinal, "€")