from django.contrib import admin
from .models import Publisher, Genre, Game, Comments

admin.site.register(Game)
admin.site.register(Comments)
admin.site.register(Publisher)
admin.site.register(Genre)


# Register your models here.
