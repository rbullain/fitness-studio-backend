from django import forms
from allauth.account.forms import SignupForm


class SignUpForm(SignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
