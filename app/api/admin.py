from django.contrib import admin

# Register your models here.
from .models import Category , Receipe , Ing , Ingredients , TEST



admin.site.register(Category)
admin.site.register(Receipe)
admin.site.register(Ing)
admin.site.register(Ingredients)
admin.site.register(TEST)


