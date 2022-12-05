import requests
import json

API_KEY = '90fd11e81789473ce37dc17f57e12a12'

def getData():
    movies=[]
    for page in range(1,4):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={page}'
        data = requests.get(URL).json()['results']
        movies+=data
    with open('movies.json','w', encoding='utf=8') as file :
        json.dump(data,file,ensure_ascii=False, indent = '\t')
getData()