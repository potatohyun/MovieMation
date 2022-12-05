from django.db import models
from django.conf import settings
# from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=70, default='')

class Movie(models.Model):
    
    movie_id = models.IntegerField() # 영화 id
    title = models.CharField(max_length=100) # 제목
    adult = models.BooleanField()   # 연령대
    genre_ids = models.ManyToManyField(Genre)  # 장르
    poster_path = models.TextField() # 포스터
    overview = models.TextField() # 줄거리
    popularity = models.FloatField() # 인기
    release_date = models.DateField(auto_now=False, auto_now_add=False)     # 개봉일
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
  movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name='comments')  # 댓글단 영화(FK)
  title = models.CharField(max_length=10)   # 댓글제목
  content = models.CharField(max_length=300)    # 댓글내용
  grade = models.IntegerField() # 평점
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True) 
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')
