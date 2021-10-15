from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    login = forms.CharField(label='Your login', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Your password', max_length=100)


class RegisterForm(forms.Form):
    login = forms.CharField(label='Your login', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Your password', max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm your password', max_length=100)

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['confirm_password']


class CarForm(forms.Form):
    brand = forms.CharField(label='Car brand', max_length=100)
    model = forms.CharField(label='Car model', max_length=100)
    power = forms.IntegerField(label='Car engine power')
    type = forms.CharField(label='Car type', max_length=100)


class OfficeForm(forms.Form):
    location = forms.CharField(label='Office location', max_length=100)


class CarInOfficeForm(forms.Form):
    model = forms.ChoiceField(label='Car model', choices=())
    registration_number = forms.CharField(label='Car registration number', max_length=100)

    def __init__(self, model_choices, *args, **kwargs):
        super(CarInOfficeForm, self).__init__(*args, **kwargs)
        self.fields['model'].choices = model_choices


class PaymentForm(forms.Form):
    card_number = forms.IntegerField()
    secret_code = forms.IntegerField(widget=forms.PasswordInput)


class NewBookingForm(forms.Form):
    return_to_office = forms.ChoiceField(label='Office to return', choices=())
    booking_start = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    booking_end = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

    def __init__(self, office_choices, *args, **kwargs):
        super(NewBookingForm, self).__init__(*args, **kwargs)
        self.fields['return_to_office'].choices = office_choices

    def clean_booking_end(self):
        cd = self.cleaned_data
        if cd['booking_end'] <= cd['booking_start']:
            raise forms.ValidationError('Incorrect date.')
        return cd['booking_end']


class CarsFilterForm(forms.Form):
    take_from_office = forms.ChoiceField(label='Office', choices=())
    booking_start = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    booking_end = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

    def __init__(self, office_choices, *args, **kwargs):
        super(CarsFilterForm, self).__init__(*args, **kwargs)
        self.fields['take_from_office'].choices = office_choices

    def clean_booking_end(self):
        cd = self.cleaned_data
        if cd['booking_end'] <= cd['booking_start']:
            raise forms.ValidationError('Incorrect date.')
        return cd['booking_end']
