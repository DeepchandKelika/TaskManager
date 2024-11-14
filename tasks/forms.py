from django import forms
from .models import Task, GoogleOAuthKeys


class UserInviteForm(forms.Form):
    email = forms.EmailField(
        label='User Email',
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CustomLoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class GoogleOAuthKeysForm(forms.ModelForm):
    class Meta:
        model = GoogleOAuthKeys
        fields = ['client_id', 'client_secret']

class UserInvitationForm(forms.Form):
    email = forms.EmailField(label="User's Email")
