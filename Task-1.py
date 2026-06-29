import requests
import matplotlib.pyplot as plt

# Replace with your OpenWeatherMap API key
API_KEY = "fe73c3f4b29c89c81d6fd80b0c986e2d"

# Enter city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    dates = []
    temperatures = []
    humidity = []

    # Collect first 8 records (24 hours)
    for item in data["list"][:8]:
        dates.append(item["dt_txt"])
        temperatures.append(item["main"]["temp"])
        humidity.append(item["main"]["humidity"])

    # Temperature Plot
    plt.figure(figsize=(10,5))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f"Temperature Forecast - {city}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Humidity Bar Chart
    plt.figure(figsize=(10,5))
    plt.bar(dates, humidity)
    plt.title(f"Humidity Forecast - {city}")
    plt.xlabel("Date & Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("Error:", response.status_code)
    print("Invalid city name or API key.")
