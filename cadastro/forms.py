from django import forms
from cadastro.models import Carros, Motorista, Zonas, PontosDeVisitas


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

class MotoristaForm(forms.ModelForm):
	nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do motorista'}))
	RG = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o RG do motorista'}))
	CPF = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o CPF do motorista'}))
	número_de_registro = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o N° de reg. do motorista'}))

	class Meta:
		model = Motorista
		fields = ['nome','RG','CPF','número_de_registro']

class ZonaForm(forms.ModelForm):

	id_zona = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o número identificador da zona'}))
	zona = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome da zona'}))
	
	class Meta:
		model = Zonas
		fields = ['id_zona','zona']

class PontosDeVisitasForm(forms.ModelForm):
	cliente = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
	cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class':'form-control'}))
	endereço = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
	complemento = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
	bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control'}))
	cep = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))
	cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control'}))
	uf = forms.CharField(max_length=2,widget=forms.TextInput(attrs={'class':'form-control'}))
	
	class Meta:
		model = PontosDeVisitas
		fields = ['cliente','cpf','endereço','complemento','bairro','cep','cidade','uf']
