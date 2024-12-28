from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import RecipeModel

class RecipeListView(ListView):
    model = RecipeModel
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = RecipeModel
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = RecipeModel
    template_name = 'recipe/recipe_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('recipe_list')


class RecipeDeleteView(DeleteView):
    model = RecipeModel
    template_name = 'recipe/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
