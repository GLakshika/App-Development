from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    view_users=[
        {"name":"Lakshi","age":22},
        {"name":"Akshi","age":23},
        {"name":"Shakshi","age":14},
        {"name":"Rakshi","age":25},
    ]
    return render(request, "index.html", context={"users":view_users})

