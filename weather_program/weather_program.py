import requests
import json
url = "http://t.weather.itboy.net/api/weather/city/"
with open("weather_district_id.csv") as file:
    text = file.read()
list_data = []
lines = text.split("\n")
for i in lines:
    cols = i.split(",")
    list_data.append(cols)
del list_data[0]
stats = {}
for i in list_data:
    province = i[10]
    if province not in stats:
        stats.update({province: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}})
    try:
        response = requests.get(url + i[0])
        response = response.text
        dict_data = json.loads(response)
        data = dict_data["data"]["forecast"]
        for j in range(0, 7):
            temp = int(data[j]["high"].replace("高温 ", "").replace("℃", ""))
            temp += int(data[j]["low"].replace("低温 ", "").replace("℃", ""))
            temp /= 2
            stats[province][j + 1].append(temp)
    except KeyError:
        continue 
for province, days in stats.items():
    print(province)
    for day, temp in days.items():
        avg = sum(temp) / len(temp)
        print(f"第{day}天: {avg:.2f}C")
    print() 
