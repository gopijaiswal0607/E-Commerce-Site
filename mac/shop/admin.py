from django.contrib import admin
# import database first

from .models import Product , Contact

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)

