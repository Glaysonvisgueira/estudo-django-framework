from django import forms
from cadastro.models import Carros, Motorista, Zonas, PontosDeVisitas

UF_DISPONIVEIS = (
        ('PI', 'PI'),
        ('MA', 'MA'),
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('ES', 'ES'),
        ('CE', 'CE'),
        ('GO', 'GO'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )


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

	
	zona = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome da zona'}))
	cidade = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a cidade que a zona pertence'}))
	uf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a UF que a zona pertence'}))
	
	class Meta:
		model = Zonas
		fields = ['zona','cidade','uf']

class PontosDeVisitasForm(forms.ModelForm):
	
	cliente = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do cliente'}))
	cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'XXX.XXX.XXX-XX'}))
	endereco = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rua, avenida, travessa, quadra...'}))
	complemento = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Próximo a pizzaria, praça, comércio, condomínio, apartamento e etc...'}))
	bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do bairro'}))
	cep = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'XXXXX-XXX'}))
	cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome da cidade'}))
	#uf = forms.CharField(max_length=2,widget=forms.TextInput(attrs={'class':'form-control'}))
	uf = forms.CharField(widget=forms.Select(choices=UF_DISPONIVEIS,attrs={'class':'form-control'}))
	
	class Meta:
		model = PontosDeVisitas
		fields = ['cliente','cpf','endereco','complemento','bairro','cep','cidade','uf']

	def __init__(self, *args, **kwargs):
		super(PontosDeVisitasForm, self).__init__(*args, **kwargs)
		self.fields['uf'].initial = ' '
