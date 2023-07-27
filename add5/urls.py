from django.urls import path
from .views import blog,blog2

urlpatterns=[
    path('',blog),
    path('all/',blog2)
]