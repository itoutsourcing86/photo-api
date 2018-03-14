from django.contrib import admin
from .models import Rating, Photo

# Register your models here.


admin.site.register(Photo)
admin.site.register(Rating)