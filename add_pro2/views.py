from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Books


class HomePage(ListView):
    model = Books
    template_name = 'home.html'

class textpage(ListView):
    model = Books
    template_name = 'text.html'


