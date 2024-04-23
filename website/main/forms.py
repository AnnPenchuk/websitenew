from .models import Main
from django.forms import ModelForm, TextInput, Textarea

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ["name",  "experience", "phone","address"]
        widgets = {"name": TextInput(attrs={
                    'class': 'form-control',
                     'placeholder': 'Введите ФИО'

                 }),

                    "experience": Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите опыт работы'
                }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "address": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            })
        }
