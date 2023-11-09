from django.urls import path
from .views import home, register, analize, exit ,RegisterGremio

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/registrarGremio/', RegisterGremio, name='registrar'),
    path('analize/', analize, name='analize'),
    path('logout/', exit, name='exit'),
]