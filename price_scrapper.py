from bs4 import BeautifulSoup
import requests


class price_scrapper:
    @staticmethod
    def get_price(quote):

        nbc_business = "https://www.cnbc.com/quotes/" + quote
        res = requests.get(nbc_business)
        soup = BeautifulSoup(res.content, 'html.parser')

        headlines = soup.find_all(attrs={'class': 'QuoteStrip-lastPrice'})
        return headlines[0].text

    @staticmethod
    def get_all_prices(list_of_quotes):
        dict_of_prices = {}
        for quote in list_of_quotes:
            price = float(price_scrapper.get_price(quote))
            dict_of_prices[quote] = price
        return dict_of_prices

news = price_scrapper.get_all_prices(["AAPL", "AR", "FB"])
print(news)