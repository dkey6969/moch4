from django.shortcuts import render
from .models import Book, Tag

def book_list(request, tag_id=None):
    if tag_id:
        books = Book.objects.filter(tags__id=tag_id)
    else:
        books = Book.objects.all()
    tags = Tag.objects.all()
    return render(request, 'book_list.html', {'books': books, 'tags': tags})