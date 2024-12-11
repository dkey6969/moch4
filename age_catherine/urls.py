from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:tag_id>/', views.book_list, name='book_list_by_tag'),
]