from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cadastro.models import Cadastro
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):

	email = forms.EmailField(label='E-mail')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Já existe usuário com este e-mail cadastrado!')
		return email	

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']