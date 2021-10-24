from django import forms
from django.db import models
from django.forms import fields, widgets

from .models import Suscribers

class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Suscribers
        fields = {
            'email',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electronico...'
                }
            )
        }