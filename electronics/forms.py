
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse

from electronics.models import CustomUser


class SignupForm(forms.ModelForm):
    """user signup form"""
    first_name = forms.CharField
    last_name = forms.CharField
    email = forms.EmailField
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=12)

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password' ]

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            return HttpResponse("Error!!!!")
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.Form):
    """user login form"""
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name')