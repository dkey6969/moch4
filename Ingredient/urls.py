# ingredient/urls.py
from django.urls import path
from .views import IngredientCreateView, IngredientListView, IngredientDetailView, IngredientUpdateView

urlpatterns = [
    path('new/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('list/', IngredientListView.as_view(), name='ingredient_list'),
    path('<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient_update'),
]