from django.db import models
from django.contrib.auth.models import User
from categories.models import Categories
from stores.models import Stores

# Mô hình đặt lịch
class Appointment(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="appointments", default=1)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name="appointments", default=1)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    note = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        ordering = ['-created_at']