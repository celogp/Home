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
	titulos = Titulo.objects.all()
	ctx = {}
	ctx['titulos'] = titulos
	return render(request, template_name, ctx)

@login_required(login_url='/')
def frmtitulos(request, pk):
	template_name='frmtitulos.html'
	ctx = {}
	if (pk != 0):
		titulo = get_object_or_404(Titulo, pk=pk)
	form = TituloForm(request.POST or None, instance=titulo)
	"""
	if request.method == 'POST' and form.is_valid():
		form.save()
		print('form valido')
	"""
	
#	if request.method == 'POST' and request.is_ajax():
	if request.method == 'POST':
		#print('passou no ajax' )
		if form.is_valid():
			form.save()
			#print('form valido')
			data_json = {'row':'Ok'}
			#print(data_json)
			#return JsonResponse(data_json)
		else:
			#print('form invalido')
			data_json = {'row': 'erro'}
			#return JsonResponse(data_json)

	ctx['form'] = form
	#print('passando no fim')
	return render(request, template_name, ctx)