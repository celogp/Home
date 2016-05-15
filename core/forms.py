from django.forms import ModelForm
from django.contrib.auth.models import User

#se quiser usar outro form para logar/registrar com o usuário ou complementar o cadastro
class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')