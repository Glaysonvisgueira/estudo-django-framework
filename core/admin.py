from django.contrib import admin

from cadastro.models import Cadastro, Motorista, Carros, Zonas, PontosDeVisitas

class CadastroAdmin(admin.ModelAdmin):

	list_display = ['name','slug','start_data','created_at']
	search_fields =['name','slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Cadastro, CadastroAdmin)	

class MotoristaAdmin(admin.ModelAdmin):

	list_display = ['nome','apelido','slug','rg','data_expedicao_rg','cpf','codigo','num_cnh','emissao_cnh','categoria','validade_habilitacao','categoria','endereco','complemento','bairro','cep','cidade','uf','contato1','contato2','status','created_at','updated_at']
	search_fields =['nome','slug','cpf','rg','num_cnh']
	prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Motorista, MotoristaAdmin)

from cadastro.models import Motorista

class CarrosAdmin(admin.ModelAdmin):

	list_display = ['modelo','ano','codigo']
	search_fields =['modelo','ano','codigo']

admin.site.register(Carros, CarrosAdmin)

class ZonasAdmin(admin.ModelAdmin):

	list_display = ['zona','cidade','uf']
	search_fields =['zona','cidade','uf']

admin.site.register(Zonas, ZonasAdmin)	

class PontosDeVisitasAdmin(admin.ModelAdmin):

	list_display = ['cliente','cpf_cnpj','endereco','complemento','bairro','cep','cidade','uf']
	search_fields =['cliente','cpf_cnpj','endereco','complemento','bairro','cep','cidade','uf']

admin.site.register(PontosDeVisitas, PontosDeVisitasAdmin)	


