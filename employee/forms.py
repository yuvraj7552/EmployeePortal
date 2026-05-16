from django.contrib.auth import forms as auth_forms
from .models import User

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = None

class AuthenticationForm(auth_forms.AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PasswordResetForm(auth_forms.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
                                          
class SetPasswordForm(auth_forms.SetPasswordForm):
    class Meta:
        fields = ['new_password1', 'new_password2']