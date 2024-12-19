from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_pets/', views.about_pets, name='about_pets'),
    path('system_time/', views.system_time, name='system_time'),
    path('search/', views.SearchView.as_view(), name='search'),

]