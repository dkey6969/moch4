from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('form_parser_book/', views.BookFormView.as_view(), name='form_parser_book'),
]
