from django.contrib import admin

from .models import Iha
from .models import Kiralama

# Register your models here.

admin.site.register(Iha)
admin.site.register(Kiralama)