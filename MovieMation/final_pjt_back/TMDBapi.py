import requests
import json
import copy
from pprint import pprint

API_KEY = '90fd11e81789473ce37dc17f57e12a12'

popular_movies = 'popular_movie.json'
movies_genre = 'genre.json'


def TMDBapi():
    result = []
    idx = 0
    pages = 10

    for page in range(1,pages+1):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page='+str(page)
        response = requests.get(URL).json()['results']
        for i in range(len(response)):
            if response[i]["overview"] == "":
                response[i]["overview"] = "줄거리 정보가 없습니다."
            del response[i]["backdrop_path"]
            del response[i]["original_title"]
            del response[i]["original_language"]
            del response[i]["video"]
            response[i]["movie_id"] = response[i]["id"]
            del response[i]["id"]
            if response[i]["release_date"] == "":
                response[i]["release_date"] = '2001-01-01'
            # del response[i]["genre_ids"]
            response[i]["poster_path"] = 'https://image.tmdb.org/t/p/w500'+response[i]["poster_path"]
            templates = {
                "model": "movies.movie",
                "pk": 0,
                "fields": {
                }
            }
            idx += 1
            templates["pk"] = idx
            templates["fields"] = response[i]
            result.append(templates)

    return result


def TMDBapiGenre():
    URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
    response = requests.get(URL).json()['genres']
    for genre in response:
        temp= copy.deepcopy(genre)
        del genre['id']
        del genre['name']
        genre['model'] = 'movies.genre'
        genre['fields'] = temp
    return response

with open(popular_movies, 'w',encoding='utf=8') as file:
    json.dump(TMDBapi(),file,ensure_ascii=False,indent=4)
with open(movies_genre, 'w',encoding='utf=8') as file:
    json.dump(TMDBapiGenre(),file,ensure_ascii=False,indent=4)


'''
 {'adult': False,
  '###backdrop_path': '/xJHokMbljvjADYdit5fK5VQsXEG.jpg',
  'genre_ids': [12, 18, 878],
  'id': 157336,
  '###original_language': 'en',
  '###original_title': 'Interstellar',
  'overview': '세계 각국의 정부와 경제가 완전히 붕괴된 미래가 다가온다. 지난 20세기에 범한 잘못이 전 세계적인 식량 부족을 '
              '불러왔고, NASA도 해체되었다. 나사 소속 우주비행사였던 쿠퍼는 지구에 몰아친 식량난으로 옥수수나 키우며 살고 '
              '있다. 거센 황사가 몰아친 어느 날 알 수 없는 힘에 이끌려 딸과 함께 도착한 곳은 인류가 이주할 행성을 찾는 '
              '나사의 비밀본부. 이 때 시공간에 불가사의한 틈이 열리고, 이 곳을 탐험해 인류를 구해야 하는 임무를 위해 쿠퍼는 '
              '만류하는 딸을 뒤로한 채 우주선에 탑승하는데...',
  'popularity': 212.5,
  'poster_path': '/zDNAeWU0PxKolEX1D8Vn1qWhGjH.jpg',
  'release_date': '2014-11-05',
  'title': '인터스텔라',
  '###video': False,
  'vote_average': 8.4,
  'vote_count': 29785},
'''