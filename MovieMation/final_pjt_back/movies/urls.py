from django.urls import path,include
from . import views

urlpatterns = [
    path('movies/', views.movies_list),
    path('movies/<int:movies_pk>/', views.movies_detail),
    # path('movies/comments/<int:comment_pk>/', views.comment_detail),
    # path('movies/<int:movies_pk>/comments/', views.comment_create),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movies_pk>/createcomments/', views.comment_create),
    path('comments/<int:comment_pk>/like/', views.like), # 게시글 좋아요(context로 전송)

    path('recommend/popularity/', views.popularity), # 인기순  
    path('recommend/average/', views.vote_average), # 평점 
    path('recommend/random/', views.random), # 평점 

    path('mypage/', views.mypage), # 마이페이지


    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
