from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse('birinchi blog')

def blog2(request):
    return HttpResponse('2-blog')
