from django.urls import path
from . import views

urlpatterns = [
    # path('', views.appointment_list, name='appointment_list'),
    path('', views.appointment_create, name='appointment_create'),
    path('thanh-cong', views.appointment_success, name='appointment_success'),
]
