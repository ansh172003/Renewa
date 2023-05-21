from django.contrib import admin

# Register your models here.

from .models import BlogModel, NightFood, Grocery

admin.site.register(BlogModel)
admin.site.register(NightFood)
admin.site.register(Grocery)

