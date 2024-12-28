from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import IngredientModel
from django.urls import reverse_lazy


class IngredientCreateView(CreateView):
    model = IngredientModel
    template_name = 'ingredient/ingredient_form.html'
    fields = ['name', 'quantity', 'unit', 'recipe']
    success_url = reverse_lazy('ingredient_list')


class IngredientListView(ListView):
    model = IngredientModel
    template_name = 'ingredient/ingredient_list.html'
    context_object_name = 'ingredients'
    queryset = IngredientModel.objects.all()


class IngredientDetailView(DetailView):
    model = IngredientModel
    template_name = 'ingredient/ingredient_detail.html'
    context_object_name = 'ingredient'


class IngredientUpdateView(UpdateView):
    model = IngredientModel
    template_name = 'ingredient/ingredient_form.html'
    fields = ['name', 'quantity', 'unit', 'recipe']
    success_url = reverse_lazy('ingredient_list')