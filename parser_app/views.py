from django.shortcuts import HttpResponse
from django.views import generic
from . import models, forms

class BookListView(generic.ListView):
    template_name = 'parser/book_list.html'
    context_object_name = 'books'
    model = models.BookModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookFormView(generic.FormView):
    template_name = 'parser/book_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг успешно завершён')
        return super().post(request, *args, **kwargs)

