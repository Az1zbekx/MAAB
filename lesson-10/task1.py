import requests

weather_api_key = "e83fed15a3008e2c83e0b768268ee7d8"
city_name = "Tashkent"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric"

try:
    response = requests.get(weather_url)
    response.raise_for_status()
    weather_data = response.json()

    temp = weather_data.get("main", {}).get("temp")
    humidity = weather_data.get("main", {}).get("humidity")
    pressure = weather_data.get("main", {}).get("pressure")
    description = weather_data.get("weather", [{}])[0].get("description")
    wind_speed = weather_data.get("wind", {}).get("speed")

    print("Ob-havo (", city_name, ")")
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Pressure:", pressure, "hPa")
    print("Weather:", description)
    print("Wind Speed:", wind_speed, "m/s")

except requests.exceptions.RequestException as e:
    print("Tarmoq xatosi:", e)
except Exception as e:
    print("Noma'lum xato:", e)
