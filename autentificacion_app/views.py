from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm
## Creacion de vista


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = UserRegistrationForm()
    return render(request, 'autentificacion_app/register.html', {'form': form})

def index(request):
    return render (request, 'autentificacion_app/index.html')

def home(request):
    return render (request, 'autentificacion_app/home.html')

@login_required
def login(request):
    return render (request, 'autentificacion_app/login.html')
