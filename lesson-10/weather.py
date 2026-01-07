import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=Toshkent&appid=6b72fe2616a9e936983dbe6384caaca4&units=metric"

res=requests.get(url)
data=res.json()
#print(data)

print("teperature:",data["main"]["temp"])
print("humidity:",data["main"]["humidity"])

