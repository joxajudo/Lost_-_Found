from django.contrib import admin

from app.models import Category, Item, User, SubCategory

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(SubCategory)
