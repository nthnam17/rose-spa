from django.contrib import admin
from .models import Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)