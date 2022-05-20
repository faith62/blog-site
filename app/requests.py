from .import requests

def random_quotes():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    quote=requests.get(url)
    quotes=quote.json()

    return quotes
