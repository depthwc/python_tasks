weather="""
html
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
"""
from bs4 import BeautifulSoup


soup=BeautifulSoup(weather, "html.parser")

rows = soup.find_all('tr')[1:]  

days=[]
temps=[]
weah=[]

for row in rows:
    cells = row.find_all('td')
    day = cells[0].text
    temp = int(cells[1].text.replace('°C', ''))
    condition = cells[2].text
    days.append(day)
    temps.append(temp)
    weah.append(condition)


print("5-Day Weather:")
for j in range(len(days)):
    print(f"{days[j]}: {temps[j]}°C, {weah[j]}")


print("Max temp:", days[temps.index(max(temps))] , max(temps),"°C")

print("Sunny days:")
for i in range(len(weah)):
    if weah[i]=="Sunny":
        print(days[i])

print("Average temperature:",sum(temps)/len(temps))
