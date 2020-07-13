from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.URLCreateView, name="create"),
    path("url/<name>/", views.URLDetailView, name="url"),
    path("list/<page>", views.URLListView.as_view(), name="list")
]

