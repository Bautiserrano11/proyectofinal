
from django.urls import path
from .views import Homepage

urlpatterns = [
    path('', Homepage, name='Homepage'),
    # Agrega otras rutas según sea necesario
]
