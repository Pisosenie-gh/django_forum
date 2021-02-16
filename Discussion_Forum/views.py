from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import forum, PodCategory
from django.shortcuts import get_object_or_404
from django.db.models import Count

from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import forum, Like, Like_2, ForumPopular
from .models import Reviews as Rev
from .serializers import forumSerializer
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from hitcount.views import HitCountDetailView

"""Вывод полпулярных вопросов """

class Popular(View):

    def get_popular(self):
        return ForumPopular.objects.all()

    """Бесполезная"""
def like_post(request):
    user = request.user
    post_id = request.POST.get('post_id')
    post_obj = forum.objects.get(id=post_id)

    if user in post_obj.likes.all():
        post_obj.likes.remove(user)
    else:
        post_obj.likes.add(user)

    like, created = Like.objects.get_or_create(user=user, post_id=post_id)

    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def like_review(request):
    user = request.user
    review_id = request.POST.get('review_id')
    review_obj = Rev.objects.get(id=review_id)

    if user in review_obj.likes.all():
        review_obj.likes.remove(user)
    else:
        review_obj.likes.add(user)

    like, created = Like_2.objects.get_or_create(user=user, review_id=review_id)

    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'home.html', context)


"""Добавлние Вопроса"""


class AddPost(View):
    def post(self,request):
        if request.user.is_authenticated:
            form = CreateInForum()
            if request.method == 'POST':
                form = CreateInForum(request.POST)
                category = Category.objects.all()


                if form.is_valid():
                    form.save()
                    return redirect('/')
            context = {'form': form, 'category':category}
            return render(request, 'addInForum.html' , context)
        else:
            return render(request, 'error.html')

    def get(self,request):
        if request.user.is_authenticated:
            form = CreateInForum()
            if request.method == 'POST':
                form = CreateInForum(request.POST)
                category = Category.objects.all()


                if form.is_valid():
                    form.save()
                    return redirect('/')
            context = {'form': form}
            return render(request, 'addInForum.html' , context)
        else:
            return render(request, 'error.html')

    """Отзывы"""


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)

        movie = forum.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get(self):
        queryset = forum.objects.all().annotate(cnt=Count('comments').order_by('cnt'))
        context = {'queryset':queryset}
        return render(context)


"""Вопросы"""





class GenreYear:
    """Жанры и года выхода фильмов"""

    def get_genres(self):
        return Category.objects.all()


class PostList(ListView, GenreYear, Popular):
    model = forum
    queryset = forum.objects.filter()


"""Вывод вопросов деатльно + кол во просмотров"""



class PostDetail(HitCountDetailView, GenreYear, Popular):
    model = forum

    count_hit = True



""" Удаление коментов """


def to_get_comment(request, id):

    selected_comment = get_object_or_404(Reviews, id=id)
    selected_comment.delete()
    return redirect('profile')


""" Удаление Постов """


def to_get_posts(request, id):

    selected_comment = get_object_or_404(forum, id=id)
    selected_comment.delete()
    return redirect('Discussion_Forum:my_q')


"""АPI"""


class ArticleView(APIView):
    def get(self, request):
        articles = forum.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = forumSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        serializer = forumSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


"""ПОЙСК"""


class Search(ListView):

    def get_queryset(self):
        return forum.objects.filter(description__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'

        return context




"""Вывод категорий"""


class CategoryView(View):

    def get(self,request):

        category = Category.objects.all()


        return render(request, 'addInForum.html' , {'category': category})



class CategoryViewSet(View, GenreYear):

    def get(self,request, pk):
        get_genres = Category.objects.all()
        forum_list = ForumPopular.objects.all()
        posts = forum.objects.filter(topic__id = pk)
        menu = Category.objects.all()

        return render(request, 'Discussion_Forum/home.html', {'posts':posts, 'menu':menu, 'get_genres': get_genres, 'forum_list':forum_list} )







def contact(request):
    return   render(request, 'contact.html')


def q_author(request):
    q = forum.objects.filter(username = request.user)

    return render(request, 'my_q.html', {'q': q})


class CallView(View):

    def post(self, request):
        form = CallForm(request.POST)

        movie = Call.objects.all()
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


