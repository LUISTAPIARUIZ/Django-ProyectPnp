from django.urls import path
from .views import home,buscar, register, analize, exit ,RegisterGremio , RegisterPersona,RegisterEvento,obtenerGremio,obtenerPersona, obtenerEvento

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/registrarGremio/', RegisterGremio, name='registrarGremio'),
    path('register/registrarEvento/', RegisterEvento, name='registrarEvento'),
    path('register/registrarPersona/', RegisterPersona, name='registrarPersona'),
    path('obtenerGremio/', obtenerGremio, name='obtenerGremio'),
    path('obtenerPersona/', obtenerPersona, name='obtenerPersona'),
    path('obtenerEvento/', obtenerEvento, name='obtenerEvento'),
    path('analize/', analize, name='analize'),
    path('buscar/', buscar, name='buscar'),
    path('logout/', exit, name='exit'),
]