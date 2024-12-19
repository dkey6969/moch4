from django.urls import path, include
from . import views

urlpatterns = [
    path('older/', views.OlderListView.as_view(), name='older'),
    path('kid/',views.KidsListView.as_view(), name='kid'),
    path('teeneger/',views.TeenegersListView.as_view(), name='teenegers'),
    path('youth/',views.YouthsListView.as_view(), name='youth'),
    path('all/',views.AllListView.as_view(), name='all'),

]