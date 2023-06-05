from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        "recipes/index.html",
        context={
            "name": "marcelo",
        },
    )


def sobre(request):
    return HttpResponse("sobre")


def contato(request):
    return HttpResponse("contato")


# Create your views here.
