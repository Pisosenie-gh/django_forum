from django.db import models
import random as r
from django.urls import reverse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    """Категории"""

    name = models.CharField("Навание категории", max_length=5000, default=None, blank=True)
    description = models.TextField("Описание категории", default=None, blank=True)
    objects = models.Manager()
    slug = models.SlugField(verbose_name='Транслит', null=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"





class forum(models.Model):
    """Вопросы"""
    username = models.CharField("Для валидации", blank=True,max_length=5000)

    name = models.CharField(max_length=200, default="{{ request.user }}")
    email = models.CharField(max_length=200, null=True)
    topic = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    opisanie = models.TextField("Описание", null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    user_photo = models.CharField("Photo", blank=True, max_length=50000)



    @property
    def num_likes(self):
        return str(self.likes.all().count())

    def __str__(self):
        return str(self.topic)


LIKE_CHOICES = ( ('Like', 'Like'),
                 ('Unlike', 'Unlike'))




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(forum, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class PodCategory(models.Model):


    father = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField("Навание подкатегории", max_length=5000, default=None, blank=True)
    description = models.TextField("Описание категории", default=None, blank=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("forum_detail", kwargs={"slug": self.slug})

class Reviews(models.Model):
    """Отзывы"""
    username = models.CharField("Для валидации", blank=True,max_length=5000)
    user_photo = models.CharField("Photo", blank=True, max_length=50000)
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(forum, verbose_name="фильм", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='reviews')






    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Like_2(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


    def __str__(self):

        return str(self.user)


class Call(models.Model):
    text = models.TextField('Text', blank=True)
    name = models.CharField("name", max_length=2000, blank=True)
    email = models.EmailField('Email', blank=True)


    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name = "Связь"
        verbose_name_plural = "Свзяь"


class ForumPopular(models.Model):
    vopros = models.OneToOneField(forum, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vopros)

    class Meta:
        verbose_name = "Популярная статья"
        verbose_name_plural = "Популярные статьи"
