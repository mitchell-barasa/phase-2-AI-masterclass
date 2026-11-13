import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-1.2921&longitude=36.8219&current_weather=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    time = weather["time"]
    temperature = weather["temperature"]
    windspeed = weather["windspeed"]
    winddirection = weather["winddirection"]

    print("Location: Nairobi")
    print(f"Time: {time}")
    print(f"Temperature: {temperature} Degress Celcius")
    print(f"Wind Speed: {windspeed} Km/hr")
    print(f"Wind Direction: {winddirection} Degrees")
else:
    print("Resquest failed. Status:", response.status_code)