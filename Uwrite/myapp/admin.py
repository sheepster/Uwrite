from django.contrib import admin

from .models import Product, Tasks

admin.site.register(Product)
admin.site.register(Tasks)