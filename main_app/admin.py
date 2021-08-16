from django.contrib import admin

# Import your models here
from .models import Cat 

# Register your models here.
admin.site.register(Cat)