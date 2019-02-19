from django import forms
from cadastro.models import Carros


class ContactCourse(forms.Form):
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

class Carrosform(forms.ModelForm):

    class Meta:
        model = Carros
        fields = ['modelo','ano','codigo']