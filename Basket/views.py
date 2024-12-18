from django.shortcuts import render, redirect, get_object_or_404
from Basket.forms import BasketForm
from Basket.models import BasketModel


def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_list')

    else:
        form = BasketForm()
    return render(request, 'basket/create_basket.html', {'form': form})


def basket_list_view(request):
    if request.method == 'GET':
        basket_list = BasketModel.objects.all().order_by('-id')
        context = {
            'basket_list': basket_list
        }
        return render(request, 'basket/basket_list.html', context=context)


def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(BasketModel, id=id)
        context = {
            'basket_id': basket_id
        }
        return render(request,
                      'basket/basket_detail.html',
                      context=context
                      )

def update_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=basket_id)
    return render(request,
                 'basket/basket_update.html',
                 {
                      'basket_id': basket_id,
                      'form': form,
                  }
                  )

def delete_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    basket_id.delete()
    return redirect('basket_list')