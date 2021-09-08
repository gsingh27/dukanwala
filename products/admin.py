from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

@admin.register(product)
class product(admin.ModelAdmin):
    list_display = [field.name for field in product._meta.fields]

