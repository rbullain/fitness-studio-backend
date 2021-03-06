from allauth.account.views import SignupView
from django.views.generic import TemplateView

from apps.accounts.forms import SignUpForm


class UserSignUpView(SignupView):
    form_class = SignUpForm
    template_name = 'accounts/sign-up.html'


class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'
