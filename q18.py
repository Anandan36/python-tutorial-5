import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2023-01-01', periods=30)
places = ['New York', 'Chicago', 'Los Angeles', 'Houston', 'Phoenix', 'Philadelphia']
weather_types = ['Rainy', 'Cloudy', 'Sunny']

weather_data = {
    'date': [date.strftime('%Y-%m-%d') for date in np.random.choice(dates, 30)],
    'temperature': np.random.uniform(20, 35, 30).round(1),
    'humidity': np.random.uniform(30, 90, 30).round(1),
    'windSpeed': np.random.uniform(0, 30, 30).round(1),
    'precipitationType': np.random.choice(['None', 'Rain', 'Snow'], 30),
    'place': np.random.choice(places, 30),
    'weather': np.random.choice(weather_types, 30, p=[0.3, 0.3, 0.4])
}

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv('weather.csv', index=False)

weather_df = pd.read_csv('weather.csv')
max_temp = weather_df['temperature'].max()
min_temp = weather_df['temperature'].min()
cool_places = weather_df[weather_df['temperature'] < 28]['place'].unique()
cloudy_places = weather_df[weather_df['weather'] == 'Cloudy']['place'].unique()
weather_freq = weather_df['weather'].value_counts().sort_index()

plt.figure(figsize=(15, 6))
plt.bar(weather_df['date'], weather_df['temperature'], color='orange')
plt.title('Temperature by Day')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('daily_temperature.png')
plt.close()