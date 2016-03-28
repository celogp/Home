from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'home.html')

# Create your views here.
def core(request):
    return render(request, 'core.html')
