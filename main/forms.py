from django import forms

from .models import *
from .services.validators import *


class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. John'}),
            'surname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'ex. Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. john.doe@ex.com'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        word_validator(name)

        return name

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        word_validator(surname)

        return surname

    def clean_email(self):
        email = self.cleaned_data['email']
        email_validator(email)

        return email
