from django import forms
from .models import *

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), max_length=15, label='Password')


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=15)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=15, label='Confirm Password')

    class Meta:
        model = User
        fields = ('firstName', 'contactNo', 'email','password',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['id'] = "uemail_id"
        self.fields['password'].widget.attrs['id'] = "upassword_id"


class LeaveForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='State', empty_label="Select",
                           queryset=User.objects.all().values('firstName'))
    class Meta:
        model = Leave
        fields = ('desc', 'user','date',)


class LeaveEditForm(forms.ModelForm):
     class Meta:
        model = Leave
        fields = ('desc','date',)