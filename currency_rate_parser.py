from bs4 import BeautifulSoup
import requests


def get_kurs():
    url = " https://ru.investing.com/currencies/usd-rub "

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all('span', class_='text-2xl')
    for quote in quotes:
        print(" 1 доллар равен:", quote.text, 'Рублей')


get_kurs()
