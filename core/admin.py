from django.contrib import admin

from cadastro.models import Cadastro, Motorista, Carros

class CadastroAdmin(admin.ModelAdmin):

	list_display = ['name','slug','start_data','created_at']
	search_fields =['name','slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Cadastro, CadastroAdmin)	

class MotoristaAdmin(admin.ModelAdmin):

	list_display = ['name','slug','rg_identidade','CPF','num_registro','categoria_habilitacao','validade_habilitacao','start_data','created_at','updated_at']
	search_fields =['name','slug','CPF','rg_identidade','num_registro']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Motorista, MotoristaAdmin)

from cadastro.models import Motorista

class CarrosAdmin(admin.ModelAdmin):

	list_display = ['modelo','ano','codigo']
	search_fields =['modelo','ano','codigo']

admin.site.register(Carros, CarrosAdmin)	
