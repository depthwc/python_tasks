import requests
import random

API_KEY = '509559fe70d1ddf64405dac6d0a247de'
BASE_URL = 'https://api.themoviedb.org/3'

url = f'{BASE_URL}/genre/movie/list'
params={"api_key":API_KEY, "language": "en-US"}
res=requests.get(url,params=params)
data=res.json()["genres"]
genres_name=[]
genres_id=[]
for i in data:
    genres_name.append(i["name"])
    genres_id.append(i["id"])

print("genres:")
for i in genres_name:
    print(i)
cgenre=input("choose : ")
cgenre=genres_id[genres_name.index(cgenre)]


url = f'{BASE_URL}/discover/movie'

params={
    "api_key": API_KEY,
    'with_genres': cgenre,
    "sort_by": 'popularity.desc',
    "page": 1
}
res = requests.get(url, params=params)
res.raise_for_status()
data2 = res.json()
total_pages = min(data2['total_pages'], 500)


params['page'] = random.randint(1, total_pages)
response = requests.get(url, params=params)
response.raise_for_status()
movies = response.json()['results']

print("Random Movie: ",random.choice(movies)["original_title"])


