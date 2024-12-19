from django.shortcuts import render, redirect, get_object_or_404
from Basket.forms import BasketForm
from Basket.models import BasketModel
from django.views import generic


# # CREATE BASKET
class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)


# READ BASKET
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = BasketModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

#READ DETAIL BASKET
class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)

# UPDATE BASKET
class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/basket_update.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=todo_id)

# BASKET DELETE
class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)
