from django.contrib import admin
from .models import Topic, Recipe


admin.site.register(Recipe)
admin.site.register(Topic)