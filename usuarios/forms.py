from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm  
from .models import Users

class UserChargeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users
        fields = ('username', 'email', 'cargo')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Aqui, garantir que o email não se repita (exceto o próprio usuário)
        if Users.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email



class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users        
        fields = ('username', 'email', 'cargo', 'password1', 'password2')  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
