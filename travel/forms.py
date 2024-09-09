from django import forms
from .models import Travel, Booking


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    # name = forms.CharField(max_length=100, label="Ismingiz",
    #                        widget=forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'}))
    # email = forms.EmailField(label="E-mailingiz",
    #                          widget=forms.EmailInput(attrs={'placeholder': 'E-mailingizni kiriting'}))
    # tour = forms.CharField(max_length=100, label="Tur nomi", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
