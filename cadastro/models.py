from django.db import models

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

STATUS = (
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
    )


class Cadastro(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField('Nome', max_length = 100)
	slug = models.SlugField('Código do carro')
	description = models.TextField('Descrição', blank = True)
	about = models.TextField('Observações da Frota', blank = True)
	start_data = models.DateField('Data de início',null = True, blank = True)
	#image = models.ImageField(upload_to = 'cadastro/images', verbose_name = 'Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)
	

	def __str__(self):
		return self.name 
		
	class Meta:
		verbose_name = "Cadastro"
		verbose_name_plural = "Cadastros"
		ordering = ['name']

class Motorista(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField('Nome:', max_length = 100)
	apelido = models.CharField('Apelido:', max_length = 50, blank=True)
	slug = models.SlugField('Código do motorista:', blank=True)
	rg = models.CharField('RG', max_length = 13)
	data_expedicao_rg = models.DateTimeField('Data de expedição do RG:')	
	cpf = models.CharField('CPF', max_length = 11)
	nascimento = models.DateTimeField('Data de nascimento:')
	codigo = models.CharField('Código:', max_length = 4, default="")
	num_cnh = models.CharField('Número de registro:',max_length = 11)
	emissao_cnh = models.DateTimeField('Data de emissão da CNH:')
	validade_habilitacao = models.DateTimeField('Validade da habilitação:')
	categoria = models.CharField('Categoria:', max_length = 2,default="")
	endereco = models.CharField('Endereço:', max_length = 120, default="")
	complemento = models.CharField('Complemento:', max_length = 120, blank=True, default="")
	bairro = models.CharField('Bairro:', max_length = 40)
	cep = models.CharField('CEP:', max_length = 8)
	cidade = models.CharField('Cidade:', max_length = 30)
	uf = models.CharField('UF:',choices=UF_DISPONIVEIS,max_length = 2)
	contato1 = models.CharField('Contato:',max_length=11, blank=True)
	contato2 = models.CharField('Contato adicional:',max_length=11, blank=True)
	status = models.CharField('Status:',choices=STATUS, max_length=7)		
	created_at = models.DateTimeField('Cadastrado em;',auto_now_add = True)
	updated_at = models.DateTimeField('Cadastro atualizado em:',auto_now = True)	
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Motorista"
		verbose_name_plural = "Motoristas"
		ordering = ['codigo']

class Carros(models.Model):
	id = models.AutoField(primary_key=True)
	modelo = models.CharField('Modelo', max_length = 30)
	codigo = models.CharField('Código do automóvel', max_length = 4)
	ano = models.CharField('Ano', max_length = 4)

	def __str__(self):
		return self.modelo

	class Meta:
		verbose_name = "Carro"
		verbose_name_plural = "Carros"
		ordering = ['modelo']


class Zonas(models.Model):
	id = models.AutoField(primary_key=True)
	zona = models.CharField('Zona:', max_length = 10,default='')
	cidade = models.CharField('Cidade:', max_length = 40,default='')
	uf = models.CharField('UF:',max_length = 2,default='')
	 
	def __str__(self):
		return self.zona

	class Meta:
		verbose_name = "Zona"
		verbose_name_plural = "Zonas"
		ordering = ['id']

class PontosDeVisitas(models.Model):
	

	id = models.AutoField(primary_key=True)
	cliente = models.CharField('Cliente:', max_length = 120)
	cpf = models.CharField('CPF:', max_length = 11)
	endereco = models.CharField('Endereço:', max_length = 120)
	complemento = models.CharField('Complemento:', max_length = 120, blank=True)
	bairro = models.CharField('Bairro:', max_length = 40)
	cep = models.CharField('CEP:', max_length = 8)
	cidade = models.CharField('Cidade:', max_length = 30)
	uf = models.CharField('UF:',choices=UF_DISPONIVEIS,max_length = 2)
	
	def __str__(self):
		return self.bairro

	class Meta:
		verbose_name = "Ponto de visita"
		verbose_name_plural = "Pontos de visitas"
		ordering = ['bairro']