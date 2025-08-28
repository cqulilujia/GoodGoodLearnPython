import requests
import json
province = input("输入省: ")
url = "http://t.weather.itboy.net/api/weather/city/"
with open("/Users/keithli/Downloads/Python/projects/china_weather_avg/weather_district_id.csv") as file:
    text = file.read()
list_data = []
lines = text.split("\n")
for i in lines:
    cols = i.split(",")
    list_data.append(cols)
del list_data[0]
stats = [[], [], [], [], [], [], []]
for i in list_data:
    if i[10] == province:
        try:
            response = requests.get(url + i[0])
            response = response.text
            dict_data = json.loads(response)
            data = dict_data["data"]["forecast"]
            for j in range(0, 7):
                temp = (int(data[j]["high"].replace("高温 ", "").replace("℃", "")) + int(data[j]["low"].replace("低温 ", "").replace("℃", "")))
                temp /= 2
                stats[j].append(temp)
        except KeyError:
            continue 
for i in range(0, 7):
    average = sum(stats[i]) / len(stats[i])
    print(f"第{i + 1}天: {average:.2f}C")
