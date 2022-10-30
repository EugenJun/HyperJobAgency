from django import forms
from .models import Resume

class NewVacancyForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["description", "author"]
        labels = {'description': "Description", 'author': "Author"}