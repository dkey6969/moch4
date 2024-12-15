from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket
from library_blod.models import BookModel



def basket_list(request):
    baskets = Basket.objects.all()
    return render(request, 'basket/basket_list.html', {'baskets': baskets})



def basket_form(request, pk=None):
    basket = None
    if pk:
        basket = get_object_or_404(Basket, pk=pk)
    books = BookModel.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        book = get_object_or_404(BookModel, pk=request.POST['book'])

        if basket:
            basket.name = name
            basket.email = email
            basket.phone_number = phone_number
            basket.book = book
            basket.save()
        else:
            Basket.objects.create(name=name, email=email, phone_number=phone_number, book=book)

        return redirect('basket_list')

    return render(request, 'basket/basket_form.html', {'basket': basket, 'books': books})



def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        basket.delete()
        return redirect('basket_list')
    return render(request, 'basket/basket_confirm_delete.html', {'basket': basket})
