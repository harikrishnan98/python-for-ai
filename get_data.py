import requests
from datetime import datetime,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


today = datetime.now()
week_ago = today - timedelta(7)

# Format the dates for API
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)


#---------------------------------------

# PANDAS

# Extract the daily data
daily_data = data['daily']

# Create a data frame
# Data frame is an kind of excel consists of rows and column , we are creating a table kind of frame 
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min'],
})

# Convert date strings to datetime

df['date'] = pd.to_datetime(df['date'])

print(df)

# 3. Calculate average
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2

# 4. Create Visualization
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['max_temp'], 'r-o', label = 'Max temp')
plt.plot(df['date'], df['min_temp'], 'b-o', label = 'Min temp')
plt.plot(df['date'], df['avg_temp'],'g--', label = 'Avg temp')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Pairs Weather - Past Week')
plt.legend()
plt.grid(True, alpha = 0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

#---------------------------------------

# SAVE TO CSV FILE

# Create a data folder if data folder not exists
if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/pairs_weather_data.csv', index=False)
print("Data saved to data/pairs_weather_data.csv")
