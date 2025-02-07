from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    people_data = [
        {"name": "Arun Singh", "age": 19},
        {"name": "Meena", "age": 16},
        {"name": "Hari", "age": 28},
        {"name": "Mikey", "age": 14},
        {"name": "Andrews", "age": 30},
    ]
    return render(request, "index.html", context={"peoples": people_data})


def successPage(request):
    return HttpResponse("<h1>Hello, This is Success Page.</h1>")
