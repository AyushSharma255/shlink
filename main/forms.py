from django import forms
from django.core import validators
from . import models


class URLForm(forms.ModelForm):
    name = forms.SlugField(validators=[validators.MinLengthValidator(2)], widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Name"
        }
    ))

    url = forms.URLField(validators=[validators.URLValidator], widget=forms.URLInput(
        attrs={
            "class": "form-control",
            "placeholder": "URL"
        }
    ))

    def clean_name(self):
        data = self.cleaned_data["name"]
        if not data.islower():
            raise forms.ValidationError("Shortened URL names should be in lowercase.")
        return data

    class Meta:
        model = models.ShortenedURL
        fields = "__all__"

