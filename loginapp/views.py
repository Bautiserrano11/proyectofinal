from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('homepage')  # Cambia 'homepage' por la vista a la que quieres redirigir después del inicio de sesión
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')

    return render(request, 'loginapp/login.html')

