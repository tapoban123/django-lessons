from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def successPage(request):
    return HttpResponse("<h1>Hello, This is Success Page.</h1>")