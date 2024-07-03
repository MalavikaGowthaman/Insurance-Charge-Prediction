from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['age', 'sex', 'bmi', 'children', 'smoker']
