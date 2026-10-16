from django.shortcuts import render
from django.contrib.auth.decorators import login_required

## Creacion de vista

def index(request):
    return render (request, 'autentificacion_app/index.html')

def home(request):
    return render (request, 'autentificacion_app/home.html')

@login_required
def login(request):
    return render (request, 'autentificacion_app/login.html')
