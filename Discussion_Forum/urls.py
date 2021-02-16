from django.contrib import admin
from django.urls import path, include
from .views import PostDetail, PostList, like_post, like_review, q_author
from . import views
app_name = 'Discussion_forum'
urlpatterns = [

    path('c/question/<int:pk>/', PostDetail.as_view(), name='home_detail'),
    path('', PostList.as_view(), name='posts'),
    path('like/', like_post, name = 'like_post'),
    path('like_review/', like_review, name = 'like_review'),
    path('cat/<int:pk>', views.CategoryViewSet.as_view(), name = 'post_category'),
    path('cate/', views.CategoryViewSet.as_view(), name = 'post_category'),
    path('my_q/', views.q_author, name = 'my_q'),


]
