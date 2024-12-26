import requests



api_key = "enter your API key here"

parameters = {
    'lat': 32.814,
    'lon': -96.9489,
    "appid":api_key,
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)
status = response.status_code
print(status)
data = response.json()
# print(data)
list_of_hourly_data = []
list_of_time_stamp = []
for data in data['list']:
    hourly_data = data['weather'][0]['description']
    time_stamp = data["dt_txt"]
    list_of_hourly_data.append(hourly_data)
    list_of_time_stamp.append((time_stamp))

    # hourly_data = data['list'][0]['weather'][0]['id']
    # print(hourly_data)
# print(list_of_time_stamp)
_12_hours_data = [list_of_hourly_data[1],list_of_hourly_data[2],list_of_hourly_data[3],list_of_hourly_data[4],
                  list_of_hourly_data[5],list_of_hourly_data[6],list_of_hourly_data[7],list_of_hourly_data[8],
                  list_of_hourly_data[9]]
_12_time_stamp = [list_of_time_stamp[1],list_of_time_stamp[2],list_of_time_stamp[3],list_of_time_stamp[4],
                  list_of_time_stamp[5],list_of_time_stamp[6],list_of_time_stamp[7],list_of_time_stamp[8],
                  list_of_time_stamp[9]]

_24_hour_forecast = [(list_of_hourly_data[1],list_of_time_stamp[1]),
                     (list_of_hourly_data[2],list_of_time_stamp[2]),
                     (list_of_hourly_data[3],list_of_time_stamp[3]),
                     (list_of_hourly_data[4],list_of_time_stamp[4]),
                     (list_of_hourly_data[5],list_of_time_stamp[5]),
                     (list_of_hourly_data[6],list_of_time_stamp[6]),
                     (list_of_hourly_data[7],list_of_time_stamp[7]),
                     (list_of_hourly_data[8],list_of_time_stamp[8]),
                     (list_of_hourly_data[9],list_of_time_stamp[9])]
clear_data = open("daily forecast.txt",'w')
clear_data.close()

daily_forecast = open("daily forecast.txt",'a')
daily_forecast.write(f"{_24_hour_forecast[0][1]} {_24_hour_forecast[0][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[1][1]} {_24_hour_forecast[1][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[2][1]} {_24_hour_forecast[2][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[3][1]} {_24_hour_forecast[3][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[4][1]} {_24_hour_forecast[4][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[5][1]} {_24_hour_forecast[5][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[6][1]} {_24_hour_forecast[6][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[7][1]} {_24_hour_forecast[7][0]}\n")
daily_forecast.write(f"{_24_hour_forecast[8][1]} {_24_hour_forecast[8][0]}\n")
daily_forecast.close()

print("The required file has been created.")
