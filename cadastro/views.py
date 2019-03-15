from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cadastro.models import Cadastro, Motorista, Carros, Zonas, PontosDeVisitas
from cadastro.forms import ContactCourse, Carrosform, MotoristaForm, ZonaForm, PontosDeVisitasForm

def index(request):
	cadastros = Cadastro.objects.all()
	template_name = 'cadastros/index.html'
	context = {
		'cadastros': cadastros
	}
	return render(request, template_name, context)

def details(request, slug):
    cadastro = get_object_or_404(Cadastro, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['cadastro'] = cadastro
    template_name = 'cadastros/details.html'
    return render(request, template_name, context)

def motoristas(request):
    context = {}
    template_name = 'cadastros/motoristas.html'
    if request.method == "POST":
        form = MotoristaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/', pk=user.pk)
    else:
        form = MotoristaForm()
    context['form'] = form
    return render(request, template_name, context)

def veiculos(request):
    context = {}
    template_name = 'cadastros/veiculos.html'
    if request.method == "POST":
        form = Carrosform(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/', pk=user.pk)
    else:
        form = Carrosform()
    context['form'] = form
    return render(request, template_name, context)

def zonas(request):
    context = {}
    template_name = 'cadastros/cadatro-zonas.html'
    if request.method == "POST":
        form = ZonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/', pk=user.pk)
    else:
        form = ZonaForm()
    context['form'] = form
    return render(request, template_name, context)

def pdv(request):
    context = {}
    template_name = 'cadastros/pontosdevisita.html'
    if request.method == "POST":
        form = PontosDeVisitasForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/', pk=user.pk)
    else:
        form = PontosDeVisitasForm()
    context['form'] = form
    return render(request, template_name, context)

def pdv_list(request):
    pdvs = PontosDeVisitas.objects.all()
    template_name = 'cadastros/pontosdevisita-lista.html'
    context = {
        'pdvs': pdvs
    }
    return render(request, template_name, context)

'''def editar_veiculo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template_name = 'cadastro/editar_veiculo.html'
    context = {}
    if request.method == "POST":
        form = Carrosform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://localhost:8000/', pk=post.pk)
    else:
        form = Carrosform(instance=post)
    context['form'] = form
    return render(request, template_name, context)'''