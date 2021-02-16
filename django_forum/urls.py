"""django_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Discussion_Forum.views import *
from .views import index
from authapp import views
from authapp.views import edit
from Discussion_Forum import views
from django.contrib import admin
from Discussion_Forum.views import ArticleView
from django.conf import settings
from django.conf.urls.static import static
from  Discussion_Forum.views import  AddPost
from  courses.views import AddZayavka, CoursesView, mission, franchise
from Discussion_Forum.views import PostDetail, PostList, CallView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home'),
    path('add/addInForum/', AddPost.as_view(), name='addInForum'),
    path('call/', views.CallView.as_view(), name='call'),

    #path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),
    path("review/<int:pk>/", views.AddReview.as_view(), name = "add_review"),
    path('auth/', include('authapp.urls')),
    path('', index, name = "index"),
    path('profile/edit/', edit, name='edit'),
    path('comment/<int:id>/',to_get_comment, name = 'delete_com'),
    path('post/<int:id>/',to_get_posts, name = 'delete'),
    path("search/", views.Search.as_view(), name='search'),

    path('forum/', include('Discussion_Forum.urls', namespace='Discussion_Forum')),
    path('category/', views.CategoryView.as_view(), name='category_мшуц'),
    path('courses/zayavka', AddZayavka.as_view(), name = 'add_zayavka'),
    path('mission/', mission, name = 'mission' ),
    path('franchise/', franchise, name = 'franchise'),
    path('contact/', contact, name='contact'),
    path('courses/', include('courses.urls', namespace='Courses')),
    path('i18n/', include('django.conf.urls.i18n'))

]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    #path('', home, name='home'),
    path('add/addInForum/', AddPost.as_view(), name='addInForum'),
    #path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),
    path("review/<int:pk>/", views.AddReview.as_view(), name = "add_review"),
    path('auth/', include('authapp.urls')),
    path('', index, name = "index"),
    path('profile/edit/', edit, name='edit'),
    path('comment/<int:id>/',to_get_comment, name = 'delete_com'),
    path('post/<int:id>/',to_get_posts, name = 'delete'),
    path("search/", views.Search.as_view(), name='search'),

    path('forum/', include('Discussion_Forum.urls', namespace='Discussion_Forum')),
    path('category/', views.CategoryView.as_view(), name='category_мшуц'),
    path('courses/zayavka', AddZayavka.as_view(), name = 'add_zayavka'),
    path('mission/', mission, name = 'mission' ),
    path('franchise/', franchise, name = 'franchise'),
    path('contact/', contact, name='contact'),
    path('courses/', include('courses.urls', namespace='Courses')),
    path('i18n/', include('django.conf.urls.i18n'))

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)