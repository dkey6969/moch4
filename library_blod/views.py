from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from . import models
from .forms import CommentForm
from django.views import generic

from .models import BookModel


def book_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            'book_id': book_id,
        }
        return render(request, 'book_detail.html', context=context)

def book_list_view(request):
    if request.method == 'GET':
        book_list = models.BookModel.objects.all().order_by('-id')
        context = {
            'book_list': book_list,
        }
        return render(request,template_name='book.html', context=context)

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('меня зовут Даулет учусь в гиикс')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('Домашние животные – это животные, которых люди содержат дома для общения, удовольствия или помощи. Они могут быть разными по виду, характеру и целям содержания')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse('19;51')


class BookDetailView(generic.DetailView):
    template_name = 'main_page/book_detail.html'
    model = BookModel
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def __post__(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object
            comment.save()
            return redirect('book_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)