from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, logout # funcao que salva o usuario na sessao

from django.contrib.auth.decorators import login_required
from core.models import Titulo
from core.forms import TituloForm


#Login de usuário
def login_user(request):
	logout(request)
	if request.method == 'POST':
		#print('passou no login por post')
		form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
#		print(request.POST)
		if form.is_valid():
			#se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
			login(request, form.get_user())
			return HttpResponseRedirect("/home/") # redireciona o usuario logado para a pagina inicial
		else:
			return render(request, "login.html", {"form": form})
#	print('passou no login por get')
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
	print (request)
	if ('filter_text' in request.GET):
		value = request.GET['filter_text']
		titulos = Titulo.objects.filter(descricao__icontains=value)
		data = {'rows' : list(titulos.values('id', 'descricao'))}
		print (data)
		return JsonResponse(data)
	else:
		titulos = Titulo.objects.all().order_by('-id')
	ctx['titulos'] = titulos
	return render(request, template_name, ctx)

@login_required(login_url='/')
def frmtitulos(request, pk):
	template_name='frmtitulos.html'
	ctx = {}
	print('pk ' + pk)
	if int(pk)>0:
		form = TituloForm(request.POST or None, instance=Titulo.objects.get(id=pk))
	else:
		form = TituloForm(request.POST or None)
	
	if request.method == 'POST':
		print(form)
		if form.is_valid():
			print('salvou')
			form.save()
		else:
			print ('invalido')
			print (form.errors)
			html = form.errors.as_ul()
			print (html)
			return HttpResponse(html, status=406)
	else:
		print('passou no get')
		if int(pk)==0:
			form = ctx

	ctx['form'] = form
		
	return render(request, template_name, ctx)