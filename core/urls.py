from django.urls import path
from .views import home, register, analize, exit

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/registrar/', home, name='registrar'),
    path('analize/', analize, name='analize'),
    path('logout/', exit, name='exit'),
]