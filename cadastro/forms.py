from django import forms
from cadastro.models import Carros, Motorista


class ContactCourse(forms.Form):
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

class Carrosform(forms.ModelForm):

	modelo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o modelo do veículo'}))
	ano = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o ano do veículo'}))
	codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o código do carro'}))

	class Meta:
		model = Carros
		fields = ['modelo','ano','codigo']

class Motoristaform(forms.ModelForm):
	nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do motorista'}))
	RG = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o RG do motorista'}))
	CPF = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o CPF do motorista'}))
	número_de_registro = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o N° de reg. do motorista'}))
	#categoria_habilitacao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a categoria da habilitação'}))
	#validade_habilitacao = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a validade da habilitação'}))
	class Meta:
		model = Motorista
		fields = ['nome','RG','CPF','número_de_registro']