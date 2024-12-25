from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

LEVELS = (
    ('jun', 'Junior'),
    ('middle', 'Middle'),
    ('senior', 'Senior'),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Укажите почту')
    phone_number = forms.CharField(required=True, label='Укажите номер телефона')
    level = forms.ChoiceField(choices=LEVELS, required=True, label='Уровень IT специалиста')

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'level',
            'phone_number',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.level = self.cleaned_data['level']

        if commit:
            user.save()
        return user
