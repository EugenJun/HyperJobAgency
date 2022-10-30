from django import forms
from .models import Vacancy

class NewVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["description", "author"]
        labels = {'description': "Description", 'author': "Author"}