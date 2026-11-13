import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGERATE_API_KEY")
base_currency = input("Base currency (e.g., USD, EUR, GBP): ").strip().upper()
target_currency = input("Target currency (e.g., KES): ").strip().upper()

url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code == 200 and data.get("result") == "success":
        rate = data["conversion_rate"]
        print(f"\n=== Exchange Rate ===")
        print(f"1 {base_currency} = {rate:,.2f} {target_currency}")
    elif response.status_code == 403 or data.get("error-type") == "invalid-key":
        print("Error: Invalid API key. Check EXCHANGERATE_API_KEY in your .env file.")
    elif response.status_code == 404 or data.get("error-type") == "unsupported-code":
        print(f"Error: Unsupported currency code ({base_currency} or {target_currency}).")
    else:
        print(f"Unexpected API response ({response.status_code}): {data.get('error-type', response.text)}")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
