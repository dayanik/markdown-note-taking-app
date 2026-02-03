from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    if request.method == "POST":
        context = {"hello": "Helllo worlddd!"}
        return render(request, "index.html", context=context)
    context = {"hello": "Helllo worlddd!"}
    return render(request, "index.html", context=context)
