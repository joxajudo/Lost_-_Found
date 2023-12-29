from django.contrib import admin

from app.models import Category, Item, User, SubCategory, About, AboutCategory, NewsLetter

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(SubCategory)
admin.site.register(AboutCategory)
admin.site.register(About)

admin.site.register(NewsLetter)
