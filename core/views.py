from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
 return render(request, 'home.html')

#login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Asegúrate que 'home' sea el nombre de tu vista principal
        else:
            messages.error(request, "Credenciales incorrectas")
    
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password != password2:
            messages.error(request, "Las contraseñas no coinciden")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')