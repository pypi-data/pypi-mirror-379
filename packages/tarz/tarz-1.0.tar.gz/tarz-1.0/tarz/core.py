import requests
from bs4 import BeautifulSoup

def gold():
    try:
        url = "https://www.tgju.org/profile/geram18"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('td', class_='text-left')
        
        if price_element:
            gold_price = price_element.text.strip()
            return f"{gold_price} IRR"  # یا تومان بسته به سایت
        else:
            return "Error: Gold price element not found"
    except Exception as e:
        return f"Error fetching gold price: {e}"

def crypto(coin_name):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        
        if coin_name in data:
            price = data[coin_name]["usd"]
            return price
        else:
            return f"Could not fetch data for {coin_name}."
    except Exception as e:
        return f"Error fetching cryptocurrency price: {e}"

def multiple_crypto(coin_list):
    prices = {}
    for coin in coin_list:
        prices[coin] = crypto(coin)
    
    return prices


