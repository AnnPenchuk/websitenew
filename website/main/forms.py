from .models import Main
from django.forms import ModelForm, TextInput, Textarea

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ["name", "description"]
        widgets = {"name": TextInput(attrs={
                    'class': 'form-control',
                     'placeholder': 'Введите название'
                 }),
                   "description": Textarea(attrs={
                       'class': 'form-control',
                       'placeholder': 'Введите описание'
                 }),
        }
