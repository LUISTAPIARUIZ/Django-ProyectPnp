from django.urls import path
from .views import home, register, analize, exit ,RegisterGremio , RegisterPersona,RegisterEvento

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/registrarGremio/', RegisterGremio, name='registrarGremio'),
    path('register/registrarEvento/', RegisterEvento, name='registrarEvento'),
    path('register/registrarPersona/', RegisterPersona, name='registrarPersona'),
    path('analize/', analize, name='analize'),
    path('logout/', exit, name='exit'),
]