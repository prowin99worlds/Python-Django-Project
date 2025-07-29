# django_app/admin.py

from django.contrib import admin
from .models import Blog, FormEntry

admin.site.register(Blog)
admin.site.register(FormEntry)

