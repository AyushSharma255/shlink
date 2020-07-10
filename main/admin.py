from django.contrib import admin
from . import models
from . import forms


# Register your models here.
@admin.register(models.ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    # Set Form

    form = forms.URLForm

    # List Settings

    list_display = ("name", "url")
    list_search = ("name", "url")
    list_filter = ("name", "url")
    list_editable = ("url",)

    # Detailed Settings

    fieldsets = (
        (
            # Title (string), then options such as fields (dict)
            "Shortened URL Configuration", {
                "description": "Configure the Shortened URL",
                "fields": ("name", "url"),
                'classes': ("wide", "form-control")  # classes for both fields
            }
        ),
    )
