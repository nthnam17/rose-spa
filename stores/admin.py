from django.contrib import admin
from .models import Stores

@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'created_at')
    list_filter = ('name','address')
    ordering = ('-created_at',)