from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'note', 'date', 'category', 'store', 'created_at')
    list_filter = ('name','phone')
    search_fields = ('name', 'phone', 'category__name', 'store__name')
    ordering = ('-created_at',)