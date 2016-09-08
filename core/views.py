from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.template import RequestContext, Template

from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, logout # funcao que salva o usuario na sessao

from django.contrib.auth.decorators import login_required
from core.models import Titulo
from core.forms import TituloForm

LIMIT_CONSULTA = 10
STR_VAZIA = ''

#Login de usuário
def login_user(request):
	logout(request)
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
		if form.is_valid():
			#se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
			login(request, form.get_user())
			return HttpResponse(request, status=200)
		else:
			html = form.errors.as_ul()
			return HttpResponse(html, status=406)
	#se nenhuma informacao for passada, exibe a pagina de login com o formulario
	return render(request, "login.html", {"form": AuthenticationForm()})

#Registro de usuário
def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): # se o formulario for valido
			form.save() # cria um novo usuario a partir dos dados enviados 
			return HttpResponseRedirect("/login/") # redireciona para a tela de login
		else:
			return render(request, "register.html", {"form": form})
	return render(request, "register.html", {"form": UserCreationForm() })

@login_required(login_url='/')
def home(request):
	template_name = 'home.html'
	return render(request, template_name)

@login_required(login_url='/')
def cadastros(request):
	template_name = 'cadastros.html'
	return render(request, template_name)
	
@login_required(login_url='/')
def pestitulos(request):
	template_name = 'pestitulos.html'
	ctx = {}
	if request.is_ajax():
		template_name = 'restitulos.html'
		value = request.GET['filter_text']
		if (value==STR_VAZIA):
			titulos = Titulo.objects.all().order_by('-id')[:LIMIT_CONSULTA]
		else:
			titulos = Titulo.objects.filter(descricao__icontains=value).order_by('-id')
	else:
		titulos = Titulo.objects.all().order_by('-id')[:LIMIT_CONSULTA]
	ctx['titulos'] = titulos
	return render(request, template_name, ctx)

@login_required(login_url='/')
def frmtitulos(request, pk):
	template_name='frmtitulos.html'
	ctx = {}
	print(request)
	print('pk ' + pk)
	try:
		if int(pk)>0:
			form = TituloForm(request.POST or None, instance=Titulo.objects.get(id=pk))
		else:
			form = TituloForm(request.POST or None)
	except:
		print('passando na exception')
		html = 'Registro nao encontrado.'
		return HttpResponse(html, status=400)
		
	print('passou para baixo')
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		else:
			html = form.errors.as_ul()
			return HttpResponse(html, status=406)
	elif request.method == 'DELETE':
		Titulo.objects.get(id=pk).delete()
		return HttpResponse(request, status=200)
	else:
		if int(pk)==0:
			form = ctx
	ctx['form'] = form
	return render(request, template_name, ctx)