import requests

api_key = "MF4CVFCULWU2HQRJ" 
symbol = input("enter your symbol: ")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(url)

print(response.status_code)
print(response.text)

data = response.json()

if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]
    latest_date = list(time_series.keys())[0]
    latest_data = time_series[latest_date]

    print("\nLatest data for", symbol, "on", latest_date)

    
    print("Open Price :", latest_data["1. open"])
    print("High Price :", latest_data["2. high"])
    print("Low Price  :", latest_data["3. low"])
    print("Close Price:", latest_data["4. close"])
    print("Volume     :", latest_data["5. volume"])

else:
    print("Invalid symbol")
    print(data)