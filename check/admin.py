from django.contrib import admin

from .models import Gender, Profile, Classification
# Register your models here.
admin.site.register(Gender)
admin.site.register(Profile)
admin.site.register(Classification)