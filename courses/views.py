from django.shortcuts import render
from django.views.generic.base import View
from  .forms import ZayavkaForm
# Create your views here.
from django.http import HttpResponseRedirect
from .models import Courses
from django.views.generic import ListView, DetailView

class AddZayavka(View):
    """Заявки"""
    def post(self, request):
        form = ZayavkaForm(request.POST)

        if form.is_valid():
            form = form.save()


            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CoursesView(View):
    def get(self,request):
        courses = Courses.objects.all()
        return render(request, 'courses.html', {'course':courses})

def mission(request):
    return render(request, 'mission.html')

def franchise(request):
    return render(request, 'franchise.html')

class CoursesList(ListView):
    model = Courses
    queryset = Courses.objects.filter()
    context_object_name = 'courses'





"""Вывод вопросов деатльно + кол во просмотров"""



class CoursesDetail(DetailView):
    model = Courses
