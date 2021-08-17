from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Cat, Toy

# Class Based Views
class CatCreate(CreateView):
    model = Cat
    fields = "__all__"
    success_url = "/cats/"


class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"


# Define view functions
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cats_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {"cats": cats})


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, "cats/detail.html", {"cat": cat})


# Toy View Functions
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'