from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('cadastre-se/', views.register, name='register'),
	path('sair/', LogoutView.as_view(next_page='http://localhost:8000/'), name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('editar/', views.editar, name='editar'),
	path('editar-senha/', views.edit_password, name='edit_password'),
] 	
