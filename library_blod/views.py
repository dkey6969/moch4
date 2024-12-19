from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from . import models
from django.views import generic
from .models import BookModel
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BookDetailView(DetailView):
    model = models.BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs.get('id'))


class BookListView(ListView):
    model = models.BookModel
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('меня зовут Даулет учусь в гиикс')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('Домашние животные – это животные, которых люди содержат дома для общения, удовольствия или помощи. Они могут быть разными по виду, характеру и целям содержания')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse('19;51')


