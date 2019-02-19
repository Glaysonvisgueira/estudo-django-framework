from django.contrib import admin
from django.urls import path, include
from cadastro import views

urlpatterns = [
	path('index/',views.index, name="index"),
	path('<slug>',views.details, name="details"),
	path('motoristas/',views.motoristas, name="motoristas"),
	path('veiculos-cadastrados/',views.veiculos, name="veiculos"),
	#path('editar-veiculo/',views.editar_veiculo, name="editar-veiculo"),  	  	
] 
