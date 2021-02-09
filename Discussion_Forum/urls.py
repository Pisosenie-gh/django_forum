from django.contrib import admin
from django.urls import path, include
from .views import PostDetail, PostList, like_post, like_review
from . import views
app_name = 'Discussion_forum'
urlpatterns = [

    path('c/question/<slug:slug>/', PostDetail.as_view(), name='home_detail'),
    path('', PostList.as_view(), name='posts'),
    path('like/', like_post, name = 'like_post'),
    path('like_review/', like_review, name = 'like_review'),
    path('cat/<int:pk>', views.post_category, name = 'post_category'),


]
