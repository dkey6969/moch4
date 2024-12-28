from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeDeleteView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
]