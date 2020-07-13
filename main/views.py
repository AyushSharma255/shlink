from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.urls import reverse
from . import models
from . import forms


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "home.html"


class URLListView(generic.ListView):
    model = models.ShortenedURL
    template_name = "list.html"
    context_object_name = "urlList"

    def get_context_data(self, **kwargs):
        if int(self.kwargs["page"]) <= 0:
            raise Http404()

        context = super().get_context_data(**kwargs)
        urlList = models.ShortenedURL.objects.order_by()[(int(self.kwargs["page"]) * 5 - 5):(int(self.kwargs["page"]) * 5)]
        context[self.context_object_name] = urlList
        context["amount"] = len(urlList)

        if len(urlList) == 0:
            raise Http404()

        context["page"] = self.kwargs["page"]
        return context


def URLCreateView(request):
    form = None

    if request.method == "GET":
        form = forms.URLForm()
    elif request.method == "POST":
        form = forms.URLForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            urlName = form_data.get("name")
            form.name = urlName
            form.save()

            messages.success(
                request,
                f"You have just created a shortened URL, which is {request.get_host()}{reverse('main:url', kwargs={'name': form.name}).replace(form.name.lower(), form.name)}"
            )

    return render(request, "create.html", context={
        "form": form
    })


def URLDetailView(request, name):
    return render(request, "url.html", context={
        "url": models.ShortenedURL.objects.get(name=name)
    })


def handler404(request, exception):
    return render(request, "err.html", status=404)


def handler500(request):
    return render(request, "err.html", status=500)
