from django import forms
from . import models, book_parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('book', 'Books'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'book':
            books_data = book_parser.parsing()
            for book in books_data:
                models.BookModel.objects.create(**book)
