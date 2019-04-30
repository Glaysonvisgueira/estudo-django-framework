from django.contrib import admin
from django.urls import path, include
from cadastro import views

urlpatterns = [
	path('index/',views.index, name="index"),
	path('<slug>',views.details, name="details"),
	path('motoristas/',views.motoristas, name="motoristas"),
	path('cadastro/cadastrar-veiculos/',views.veiculos, name="veiculos"),
	path('cadastro/cadastrar-zonas/',views.zonas, name="zonas"),
	path('cadastro/pontos-de-visita/',views.pdv, name="pdv"),
	path('relatorios/pontos-de-visita-listagem/',views.pdv_list, name="pdv_list"),
	path('relatorios/zonas-listagem/',views.zonas_list, name="zonas_list"),
	path('relatorios/motoristas-listagem/',views.motoristas_list, name="motoristas_list"),
	path('relatorios/motorista/<id>',views.exibir_motorista, name="exibir_motorista"),
	#path('editar-veiculo/',views.editar_veiculo, name="editar-veiculo"),  	  	
] 
