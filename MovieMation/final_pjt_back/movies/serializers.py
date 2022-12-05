from rest_framework import serializers
from .models import Movie,Comment

#### 영화리스트
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title','poster_path')

#### 단일영화+리뷰리스트
class CommentTitleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'title','grade','movie')

class MovieDetailSerializer(serializers.ModelSerializer):
    comments = CommentTitleListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


#### 단일리뷰
class OneMovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class OneCommentSerializer(serializers.ModelSerializer):
    movie = OneMovieTitleSerializer(read_only=True)
    username = serializers.CharField(source = 'user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)## 이게 참조로들고온 movie인가? 위에서 readonly해준거랑 이거랑 다른걸까?같으면 언제readonlyt?



class CommentPostSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source = 'user.username', read_only=True) # 출력값으로는 username이 나오게 하는 코드

    class Meta:
        model = Comment
        # fields = '__all__'
        # read_only_fields = ('movie',)   # 로그인정보 병합되면 삭제
        # read_only_fields = ('movie','user', ) # 로그인정보 병합되면 user는 read만 되야하니까 이걸로 바꿔주기
        fields = ('title','content', 'grade','user')
        read_only_fields = ('movie', 'user')



#### 영화추천
'''
class PopularMovie(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','title','popularity','poster_path','overview','release_date')

class AverageMovie(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','title','vote_average','poster_path','overview','release_date')

class ReleaseDateMovie(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','title','vote_average','poster_path','overview','release_date')
'''

class RecommendMovie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','popularity','vote_average','poster_path','overview','release_date')


#### 마이페이지
class MycommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','title','user','content','grade','like_users',)
        # fields = '__all__'
