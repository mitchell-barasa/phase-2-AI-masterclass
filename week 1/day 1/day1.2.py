import requests
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids":"bitcoin,ethereum,solana",
    "vs_currencies": "usd,kes",
    "include_24hr_change": "true"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("====LIVE CRYPTO MARKET SUMMARY====\n")
    for coin, stats in data.items():
        usd_price = stats["usd"]
        kes_price = stats["kes"]
        change_24h = stats["usd_24h_change"]
        
        print(f"Asset:         {coin.capitalize()}")
        print(f"Price(USD):     ${usd_price:,.2f}")
        print(f"Price(KES):     KES{kes_price:,.2f}")
        print(f"24Hr Change:    {change_24h:+.2f}%")
        print("-"*34)
    
else:
    print(f"Request Failed. Status: {response.status_code}")