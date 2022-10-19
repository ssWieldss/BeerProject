from django.contrib import admin

# Register your models here.
from beer.models import Beer

admin.site.register(Beer)