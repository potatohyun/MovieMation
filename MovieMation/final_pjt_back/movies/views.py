from django.shortcuts import render
from .models import Movie, Genre, Comment
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer,MovieDetailSerializer,OneCommentSerializer,CommentPostSerializer,RecommendMovie, MycommentsSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

##############<<< 영화(게시글) >>>>#################

###영화전제
@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

### 단일영화(+해당영화 리뷰들)
@api_view(['GET'])
def movies_detail(request,movies_pk):
    movie = get_object_or_404(Movie,pk=movies_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

##############<<< 댓글 >>>>#################

### 단일 댓글
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = OneCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentPostSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

#댓글생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movies_pk):
    movie = get_object_or_404(Movie, pk=movies_pk)
    serializer = CommentPostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(movie=movie) # 로그인정보 병합되면 삭제
        serializer.save(movie=movie,user = request.user)  # 로그인한사람들 user정보 자동으로 집어넣어주게하는 코드
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 확인용


### 댓글 좋아요
# @require_POST  # @api_view(['POST']) 얘랑 별 다를거 없음
@api_view(['POST'])
def like(request,comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    # user = request.user
    like_users = comment.like_users.count()  # 좋아요 수
    if comment.like_users.filter(pk=request.user.pk).exists():      # 요청의 user.pk가 존재하면 comment의 like_users를 삭제하고 is_liked 값을 False로 해준다. 
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)                        # 그게아니라면 comment의 like_users를 추가해주고 is_liked 값을 True 해준다. 
        is_liked = True
    context = {
        'is_liked' : is_liked,  # 좋아요 여부
        'like_users' : like_users   # 좋아요 수                   # Front작업을 위해 알립니다!!! Vue에서 response.data에서 꺼내쓰면 됩니당
    }
    return Response(context)                                        # 궁금한 점1 : comment모델에 like_users추가해줬는데 이건 좋아요누른사람들이 리스트로 들어가있는거야?



### 영화 추천(인기순, 평점순, 개봉일순(최근))
@api_view(['GET'])
def popularity(request):
    popularity_movies = Movie.objects.order_by('-popularity')[:30]
    serializer = RecommendMovie(popularity_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def vote_average(request):
    vote_average_movies = Movie.objects.order_by('-vote_average')[:30]
    serializer = RecommendMovie(vote_average_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def random(request):
    random_movies = Movie.objects.order_by('?')[:5]
    serializer = RecommendMovie(random_movies, many=True)
    return Response(serializer.data)


### 마이페이지
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage(request):
    comments = get_list_or_404(Comment)
    serializer = MycommentsSerializer(comments,many=True)
    return Response(serializer.data)