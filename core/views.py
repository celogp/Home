from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from models import User #you can use get_user_model
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, logout # funcao que salva o usuario na sessao

from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm
#from core.forms import LoginForm

#Login de usuário
def login_user(request):
	logout(request)
	if request.method == 'POST':
		print('passou no login por post')
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
# Se dados forem passados via POST
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
#		print(request.POST)
		
		if form.is_valid(): # se o formulario for valido
			form.save() # cria um novo usuario a partir dos dados enviados 
			print('salvou ',form)
			return HttpResponseRedirect("/login/") # redireciona para a tela de login
		else:
			# mostra novamente o formulario de cadastro com os erros do formulario atual
#			print('nao salvou',form)
			return render(request, "register.html", {"form": form})
	# se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
	return render(request, "register.html", {"form": UserCreationForm() })

@login_required(login_url='/')
def home(request):
	return render(request, 'home.html')

@login_required(login_url='/')
def cadastros(request):
	return render(request, 'cadastros.html')