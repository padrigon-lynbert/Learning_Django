from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

# def index(response):
#     return HttpResponse("<h1>My Project</h1>")

# def v1(response):
#     return HttpResponse("<h1>view 1!</h1>")

def index(response, name):
    ls = TodoList.objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(items.text)))
