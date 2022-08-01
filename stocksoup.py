# This is a small-scale data scrape of the #1 trending stock on Yahoo Finance.
# The program scrapes information of the top trending stock from Yahoo Finance at the time.

from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://finance.yahoo.com/trending-tickers"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('table', class_="W(100%)")

with open('trending.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Symbol', 'Price', 'Time', 'Change', 'Volume']
    thewriter.writerow(header)
    for list in lists:
        symbol = list.find('a', class_="Fw(600) C($linkColor)").text
        price = list.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").text
        time = list.find('td', class_="Va(m) Ta(end) Pstart(20px) Miw(90px) Fz(s)").text
        change = list.find('fin-streamer', class_="Fw(600)").text
        volume = list.find('td', class_="Va(m) Ta(end) Pstart(20px) Fz(s)").text

        info = [symbol, price, time, change, volume]
        thewriter.writerow(info)
