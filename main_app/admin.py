from django.contrib import admin

# Import your models here
from .models import *

# Register your models here.
admin.site.register(Cat)
# Register Feeding model
admin.site.register(Feeding)