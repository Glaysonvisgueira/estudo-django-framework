from django.db import models

class CadastroManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains = query) |  models.Q(description__incontains = query))

class MotoristaManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains = query))

class Cadastro(models.Model):
	name = models.CharField('Nome', max_length = 100)
	slug = models.SlugField('Código do carro')
	description = models.TextField('Descrição', blank = True)
	about = models.TextField('Observações da Frota', blank = True)
	start_data = models.DateField('Data de início',null = True, blank = True)
	image = models.ImageField(upload_to = 'cadastro/images', verbose_name = 'Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)
	objects = CadastroManager()	

	def __str__(self):
		return self.name 
		
	class Meta:
		verbose_name = "Cadastro"
		verbose_name_plural = "Cadastros"
		ordering = ['name']

class Motorista(models.Model):
	name = models.CharField('Nome', max_length = 100)
	slug = models.SlugField('Código do motorista')
	rg_identidade = models.CharField('RG', max_length = 13)
	CPF = models.CharField('CPF', max_length = 11)
	num_registro = models.CharField('Número de registro',max_length = 11)
	categoria_habilitacao = models.CharField('Categoria', max_length = 2)
	validade_habilitacao = models.DateTimeField('Validade da habilitação')
	start_data = models.DateField('Data de início',null = True, blank = True)
	image = models.ImageField(upload_to = 'cadastro/images/motoristas', verbose_name = 'Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Cadastrado em',auto_now_add = True)
	updated_at = models.DateTimeField('Cadastro atualizado em',auto_now = True)
	objects = MotoristaManager()	
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Motorista"
		verbose_name_plural = "Motoristas"
		ordering = ['name']

class Carros(models.Model):
	modelo = models.CharField('Modelo', max_length = 30)
	codigo = models.CharField('Código do automóvel', max_length = 4)
	ano = models.CharField('Ano', max_length = 4)

	def __str__(self):
		return self.modelo

	class Meta:
		verbose_name = "Carro"
		verbose_name_plural = "Carros"
		ordering = ['modelo']