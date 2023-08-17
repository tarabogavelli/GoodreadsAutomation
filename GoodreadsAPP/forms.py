from django import forms
from django.forms import ModelForm

from .models import input, recommendationForm, findLibrary

class input(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = input
        fields = "__all__"

class recommendationForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = recommendationForm
        fields = "__all__"
class findLibrary(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = findLibrary
        fields = "__all__"