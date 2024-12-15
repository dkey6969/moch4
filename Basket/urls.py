from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_list, name='basket_list'),
    path('form/', views.basket_form, name='basket_create'),
    path('form/<int:pk>/', views.basket_form, name='basket_edit'),
    path('delete/<int:pk>/', views.basket_delete, name='basket_delete'),
]
