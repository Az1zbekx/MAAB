
from bs4 import BeautifulSoup


with open('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')


forecast = []
rows = soup.find('table').find('tbody').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace('°C', ''))
    condition = cols[2].text.strip()
    forecast.append({'day': day, 'temperature': temp, 'condition': condition})


print("5-Day Weather Forecast:")
for entry in forecast:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")


max_temp = max(entry['temperature'] for entry in forecast)
hottest_days = [entry['day'] for entry in forecast if entry['temperature'] == max_temp]
print("\nDay(s) with the highest temperature:")
print(", ".join(hottest_days))


sunny_days = [entry['day'] for entry in forecast if entry['condition'].lower() == 'sunny']
print("\nSunny day(s):")
print(", ".join(sunny_days))


avg_temp = sum(entry['temperature'] for entry in forecast) / len(forecast)
print(f"\nAverage temperature: {avg_temp:.2f}°C")
