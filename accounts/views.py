
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Homepage')  # Cambia 'homepage' por la vista a la que quieres redirigir
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
from django.shortcuts import render

