from django.contrib import admin
from django.urls import path, include
from cadastro import views

urlpatterns = [
	path('index/',views.index, name="index"),
	path('<slug>',views.details, name="details"),
	path('motoristas/',views.motoristas, name="motoristas"),
	path('cadastrar-veiculos/',views.veiculos, name="veiculos"),
	path('cadastrar-zonas/',views.zonas, name="zonas"),
	path('pontos-de-visita/',views.pdv, name="pdv"),
	path('pontos-de-visita-listagem/',views.pdv_list, name="pdv_list"),
	#path('editar-veiculo/',views.editar_veiculo, name="editar-veiculo"),  	  	
] 
