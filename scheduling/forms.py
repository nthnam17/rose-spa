from django import forms
from .models import Appointment
from categories.models import Categories
from stores.models import Stores

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'note', 'is_confirmed', 'date']
        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder': 'Nhập tên khách hàng'}),
            'phone': forms.TextInput(attrs={ 'placeholder': 'Nhập số điện thoại'}),
            'note': forms.Textarea(attrs={ 'rows': 10, 'cols': 60, 'placeholder': 'Ghi chú nếu có'}),
            'date': forms.DateTimeInput(attrs={ 'type': 'datetime-local'}),
        }

    # category = forms.ModelChoiceField(
    #     queryset = Categories.objects.all(),
    #     empty_label="Chọn dịch vụ",
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )

    # store = forms.ModelChoiceField(
    #     queryset = Stores.objects.all(),
    #     empty_label="Chọn Cửa hàng",
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )