from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


COLOR_CHOICES = (
    ('green', 'GREEN'),
    ('blue', 'BLUE'),
    ('red', 'RED'),
    ('orange', 'ORANGE'),
    ('black', 'BLACK'),
)


class Newform(forms.Form):
    order_type = forms.CharField(
        widget=forms.Select(choices=COLOR_CHOICES),
    )
