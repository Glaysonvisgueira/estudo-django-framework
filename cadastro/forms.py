from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from cadastro.models import Carros, Motorista, Zonas, PontosDeVisitas

UF_DISPONIVEIS = (
        ('PI', 'PI'),
        ('MA', 'MA'),
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('PA', 'PA'),
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

STATUS = (
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
    )

CATEGORIAS_HABILITACAO = (
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )

class Carrosform(forms.ModelForm):

	modelo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o modelo do veículo'}))
	ano = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o ano do veículo'}))
	codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o código do carro'}))

	class Meta:
		model = Carros
		fields = ['modelo','ano','codigo']

class MotoristaForm(forms.ModelForm):
	nome = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do motorista'}))
	apelido = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apelido do motorista'}))
	rg = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Registro geral'}))
	data_expedicao_rg = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'DD/MM/AAAA'}))
	cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Cadastro de pessoa física'}))
	nascimento = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'DD/MM/AAAA'}))
	codigo = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Código do motorista'}))
	num_cnh = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'N° de registro da CNH'}))
	emissao_cnh = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'DD/MM/AAAA'}))
	validade_habilitacao = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'DD/MM/AAAA'}))
	categoria = forms.CharField(widget=forms.Select(choices=CATEGORIAS_HABILITACAO,attrs={'class':'form-control'}))
	#categoria = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'A, B, AB'}))
	endereco = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rua, avenida, travessa, quadra...'}))
	complemento = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Próximo a pizzaria, praça, comércio, condomínio, apartamento e etc...'}))
	bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do bairro'}))
	cep = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'XXXXX-XXX'}))
	cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome da cidade'}))
	uf = forms.CharField(widget=forms.Select(choices=UF_DISPONIVEIS,attrs={'class':'form-control'}))
	contato1 = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'(XX) XXXXX-XXXX'}))
	contato2 = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'(XX) XXXXX-XXXX'}))
	status = forms.CharField(widget=forms.Select(choices=STATUS,attrs={'class':'form-control'}))

	class Meta:
		model = Motorista
		fields = ['nome','apelido','rg','data_expedicao_rg','cpf','nascimento','codigo','num_cnh','emissao_cnh','validade_habilitacao','categoria','endereco','complemento','bairro','cep','cidade','uf','contato1','contato2','status']
		

class ZonaForm(forms.ModelForm):
	
	zona = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome da zona'}))
	cidade = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a cidade que a zona pertence'}))
	uf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira a UF que a zona pertence'}))
	
	class Meta:
		model = Zonas
		fields = ['zona','cidade','uf']

class PontosDeVisitasForm(forms.ModelForm):
	
	cliente = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do cliente'}))
	cpf_cnpj = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CPF: XXX.XXX.XXX-XX / CNPJ: XX.XXX.XXX/XXXX-XX'}))
	endereco = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rua, avenida, travessa, quadra...'}))
	complemento = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Próximo a pizzaria, praça, comércio, condomínio, apartamento e etc...'}))
	bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do bairro'}))
	cep = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'XXXXX-XXX'}))
	cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome da cidade'}))
	uf = forms.CharField(widget=forms.Select(choices=UF_DISPONIVEIS,attrs={'class':'form-control'}))
	
	class Meta:
		model = PontosDeVisitas
		fields = ['cliente','cpf_cnpj','endereco','complemento','bairro','cep','cidade','uf']

	