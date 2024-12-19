import requests
from datetime import datetime


menyala = 'ff82e0163010784183285b31515d7d37'
city = 'Jakarta'

url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={menyala}&units=metric'

response = requests.get(url)
data = response.json()

if data.get('cod') != '200':
    print(f"Error banh: {data.get('message', 'Unknown error')} (Code: {data.get('cod')})")
else:
 
    daily_forecast = {}
    for entry in data['list']:
        dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        date = dt.date()
        if date not in daily_forecast:
            daily_forecast[date] = entry['main']['temp']

    print("Weather Forecast:")
    for date, temp in daily_forecast.items():
        day_name = date.strftime('%a')  
        formatted_date = date.strftime('%d %b %Y')  
        print(f"{day_name}, {formatted_date}: {temp:.2f}°C")
