from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from .models import Gremio

# Create your views here.
@login_required

def home(request):
    gremio=Gremio.objects.all()
    return render(request, 'core/home.html', {'gremio': gremio})

def RegisterGremio(request):
    if request.method=='POST':
        nombre_gremio=request.POST['nameGremio']
        ruc_gremio = request.POST['rucGremio']
        dni_secretario_general = request.POST['dniSecretarioGeneral']
        nombre_secretario_general = request.POST['secretarioGeneral']
        dni_dirigente = request.POST['dniDirigente']
        nombre_dirigente = request.POST['dirigente']
        dni_presidente = request.POST['dniPresidente']
        nombre_presidente = request.POST['presidente']
        #validando los campos antes de ingresar a la BD
        def ValidarCampoVacioTexto(campo):
            if campo.strip()=='':
                return 'Vacio'
            return campo
        def ValidarCampoVacioDni(campo):
            if campo.strip()=='':
                return'00000000'
            return campo
        def ValidarCampoVacioRuc(campo):
            if campo.strip()=='':
                return'00000000000'
            return campo
        #Si algun campo de texto llega vacio lo completo como 'Vacio'
        nombre_gremio =ValidarCampoVacioTexto(nombre_gremio)
        nombre_dirigente=ValidarCampoVacioTexto(nombre_dirigente)
        nombre_presidente=ValidarCampoVacioTexto(nombre_presidente)
        nombre_secretario_general=ValidarCampoVacioTexto(nombre_secretario_general)
        #Si algun campo numerico llega vacio lo completo con ceros
        ruc_gremio=ValidarCampoVacioRuc(ruc_gremio)
        dni_dirigente=ValidarCampoVacioDni(dni_dirigente)
        dni_presidente=ValidarCampoVacioDni(dni_presidente)
        dni_secretario_general=ValidarCampoVacioDni(dni_secretario_general)

        
        if not nombre_gremio.strip().isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not ruc_gremio.isdigit() or len(ruc_gremio) != 11:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_secretario_general.isdigit() or len(dni_secretario_general) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_secretario_general.strip().isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_dirigente.isdigit() or len(dni_dirigente) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_dirigente.strip().isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_presidente.isdigit() or len(dni_presidente) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_presidente.strip().isalpha():
            return JsonResponse({'message': 'Error en el formato'})

        nuevo_gremio = Gremio(
            Nombre_Gremio=nombre_gremio,
            RUC_Gremio=ruc_gremio,
            DNI_Secretario_General=dni_secretario_general,
            Nombre_Secretario_General=nombre_secretario_general,
            DNI_Dirigente=dni_dirigente,
            Nombre_Dirigente=nombre_dirigente,
            DNI_Presidente=dni_presidente,
            Nombre_Presidente=nombre_presidente,
            Foto_Gremio='ruta_de_la_imagen',
        )
        nuevo_gremio.save()
        return JsonResponse({'message': 'Registro exitoso'})
    return JsonResponse({})

def register(request):
    return render(request, 'core/register.html')

def analize(request):
    return render(request, 'core/analize.html')

def exit(request):
    logout(request)
    return redirect('home')
