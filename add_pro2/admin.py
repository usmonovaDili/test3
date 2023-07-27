from django.contrib import admin
from .models import Books

@admin.register(Books)

class AdminBook(admin.ModelAdmin):
    list_display =['title','yozuvchi','publish_time']

