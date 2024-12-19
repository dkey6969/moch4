from django.shortcuts import render
from .models import Tag, Book
from django.views import generic


class OlderListView(generic.ListView):
    template_name = 'tags/older.html'
    context_object_name = 'older'
    model = Book

    def get_queryset(self):
        return Book.objects.filter(tags__name='книги для стариков')


class KidsListView(generic.ListView):
    template_name = 'tags/kid.html'
    context_object_name = 'kid'
    model = Book

    def get_queryset(self):
        return Book.objects.filter(tags__name='книги для детей')


class TeenegersListView(generic.ListView):
    template_name = 'tags/teenegers.html'
    context_object_name = 'teenegers'
    model = Book

    def get_queryset(self):
        return Book.objects.filter(tags__name='книги для подростков')

class YouthsListView(generic.ListView):
    template_name = 'tags/youth.html'
    context_object_name = 'youth'
    model = Book

    def get_queryset(self):
        return Book.objects.filter(tags__name='книги для молодежи')

class AllListView(generic.ListView):
    template_name = 'tags/all.html'
    context_object_name = 'all'
    model = Book

    def get_queryset(self):
        return Book.objects.all()