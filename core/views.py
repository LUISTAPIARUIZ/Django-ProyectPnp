from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from .models import Gremio, Persona , Evento
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
import re


# Create your views here.
@login_required
def obtenerGremio(request):
    gremio = Gremio.objects.all().values()  # Convertir el queryset a una lista de diccionarios
    opcion = 'gremio'
    return JsonResponse({"registro": list(gremio), "Opcion": opcion}, encoder=DjangoJSONEncoder)
def obtenerPersona(request):
    persona = Persona.objects.all().values()  # Convertir el queryset a una lista de diccionarios
    opcion = 'persona'
    return JsonResponse({"registro": list(persona), "Opcion": opcion}, encoder=DjangoJSONEncoder)
def obtenerEvento(request):
    evento = Evento.objects.all().values()  # Convertir el queryset a una lista de diccionarios
    opcion = 'evento'
    return JsonResponse({"registro": list(evento), "Opcion": opcion}, encoder=DjangoJSONEncoder)
def home(request):
    persona=Persona.objects.all()

    return render(request, 'core/home.html', {'persona': persona})

def RegisterPersona(request):
    if request.method=='POST':
        nombres_persona = request.POST.get('nombrePersona', '')
        apellidos_persona = request.POST.get('apellidoPersona', '')
        DNI_persona = request.POST.get('DNIPersona', '')
        fechaNac_persona = request.POST.get('FnacPersona', '')
        departemento_persona = request.POST.get('departamentoPersona', '')
        provincia_persona = request.POST.get('provinciaPersona', '')
        distrito_persona = request.POST.get('distritoPersona', '')
        sexo_persona = request.POST.get('opcionSexo', '')
        domicilio_persona = request.POST.get('domicilioPersona', '')
        nombrePadre_persona = request.POST.get('nompadrePersona', '')
        nombreMadre_persona = request.POST.get('nommadrePersona', '')
        #Si algun campo de texto llega vacio lo completo como 'Vacio'
        nombres_persona=ValidarCampoVacioTexto(nombres_persona)
        apellidos_persona=ValidarCampoVacioTexto(apellidos_persona)
        departemento_persona=ValidarCampoVacioTexto(departemento_persona)
        fechaNac_persona=ValidarCampoVacioTexto(fechaNac_persona)
        provincia_persona=ValidarCampoVacioTexto(provincia_persona)
        distrito_persona=ValidarCampoVacioTexto(distrito_persona)
        domicilio_persona=ValidarCampoVacioTexto(domicilio_persona)
        nombrePadre_persona=ValidarCampoVacioTexto(nombrePadre_persona)
        nombreMadre_persona=ValidarCampoVacioTexto(nombreMadre_persona)
        sexo_persona=ValidarCampoVacioTexto(sexo_persona)
        #Si algun campo numerico llega vacio lo completo con ceros
        DNI_persona=ValidarCampoVacioDni(DNI_persona)
        #validacion de formato
        if  not nombres_persona.replace(' ', '').isalpha() or \
            not apellidos_persona.replace(' ', '').isalpha() or \
            not departemento_persona.replace(' ', '').isalpha() or\
            not provincia_persona.replace(' ', '').isalpha() or \
            not distrito_persona.replace(' ', '').isalpha() or \
            not sexo_persona.replace(' ', '').isalpha() or \
            not domicilio_persona.replace(' ', '').isalpha() or \
            not nombrePadre_persona.replace(' ', '').isalpha() or \
            not nombreMadre_persona.replace(' ', '').isalpha() or \
            not DNI_persona.isdigit() or len(DNI_persona) != 8 :
            return JsonResponse({'message': 'Error en el formato'})
        if not validadFecha(fechaNac_persona.replace(' ', '')) :
            return JsonResponse({'message': 'Error Fecha de nacimiento'})
        nuevo_Persona = Persona(
            DNI = DNI_persona,
            Nombre = nombres_persona,
            Apellido = apellidos_persona, 
            Fecha_Nacimiento =fechaNac_persona,
            Departamento = departemento_persona,
            Provincia = provincia_persona,
            Distrito = distrito_persona,
            Sexo =sexo_persona,
            Domicilio =domicilio_persona,
            Nombre_Padre = nombrePadre_persona,
            Nombre_Madre = nombreMadre_persona,
            Foto_Persona = 'ruta_de_la_imagen',
        )
        nuevo_Persona.save()
        return JsonResponse({'message': 'Registro exitoso'})
    return JsonResponse({})


def buscar(request):
    if request.method=='POST':
        opcionBuscar= request.POST.get('opcionBuscar', '')
        textBuscar = request.POST.get('textBuscar', '')
        #Si algun campo de texto llega vacio lo completo como 'Vacio'
        opcionBuscar=ValidarCampoVacioTexto(opcionBuscar)
        textBuscar=ValidarCampoVacioTexto(textBuscar)
        #validacion de formato
        if  not opcionBuscar.replace(' ', '').isalpha() or \
            not textBuscar.replace(' ', '').isalnum():
            return JsonResponse({'message': 'Error algo salio mal'})
        
        if(opcionBuscar=='Gremio'):
            resultados = Gremio.objects.filter(
                Q(Nombre_Gremio__icontains=textBuscar) |
                Q(RUC_Gremio__icontains=textBuscar) |
                Q(Nombre_Presidente__icontains=textBuscar) |
                Q(DNI_Presidente__icontains=textBuscar) |
                Q(Nombre_Secretario_General__icontains=textBuscar) |
                Q(DNI_Secretario_General__icontains=textBuscar) |
                Q(Nombre_Dirigente__icontains=textBuscar) |
                Q(DNI_Dirigente__icontains=textBuscar)
            )

            # Convertir los resultados a una lista de diccionarios
            resultados_serializados = [
                {
                    'Id': resultado.Id,
                    'Nombre_Gremio': resultado.Nombre_Gremio,
                    'RUC_Gremio': resultado.RUC_Gremio,
                    'DNI_Secretario_General': resultado.DNI_Secretario_General,
                    'Nombre_Secretario_General': resultado.Nombre_Secretario_General,
                    'DNI_Dirigente': resultado.DNI_Dirigente,
                    'Nombre_Dirigente': resultado.Nombre_Dirigente,
                    'DNI_Presidente': resultado.DNI_Presidente,
                    'Nombre_Presidente': resultado.Nombre_Presidente,
                    'Foto_Gremio': resultado.Foto_Gremio,
                }
                for resultado in resultados
            ]
            return JsonResponse({'resultados': resultados_serializados, 'opcion': 'Gremio'})
        if(opcionBuscar=='Evento'):
            resultados = Evento.objects.filter(
                Q(nombreGremio__icontains=textBuscar) |
                Q(resumenSummary__icontains=textBuscar) |
                Q(departamento__icontains=textBuscar) |
                Q(provincia__icontains=textBuscar) |
                Q(distrito__icontains=textBuscar) |
                Q(fecha_inicio__icontains=textBuscar) |
                Q(fecha_termino__icontains=textBuscar) |
                Q(opcion__icontains=textBuscar) |
                Q(medida__icontains=textBuscar)
            )

            # Convertir los resultados a una lista de diccionarios
            resultados_serializados = [
                {
                    'id': resultado.id,
                    'opcion': resultado.opcion,
                    'departamento': resultado.departamento,
                    'provincia': resultado.provincia,
                    'distrito': resultado.distrito,
                    'fecha_inicio': resultado.fecha_inicio,
                    'fecha_termino': resultado.fecha_termino,
                    'nombreGremio': resultado.nombreGremio,
                    'medida': resultado.medida,
                    'resumenSummary': resultado.resumenSummary,
                }
                for resultado in resultados
            ]    
            return JsonResponse({'resultados': resultados_serializados, 'opcion': 'Evento'})
        if(opcionBuscar=='Persona'):
            resultados = Persona.objects.filter(
                Q(Apellido__icontains=textBuscar) |
                Q(DNI__icontains=textBuscar) |
                Q(Departamento__icontains=textBuscar) |
                Q(Distrito__icontains=textBuscar) |
                Q(Domicilio__icontains=textBuscar) |
                Q(Fecha_Nacimiento__icontains=textBuscar) |
                Q(Nombre__icontains=textBuscar) |
                Q(Nombre_Madre__icontains=textBuscar) |
                Q(Nombre_Padre__icontains=textBuscar) |
                Q(Provincia__icontains=textBuscar) |
                Q(Sexo__icontains=textBuscar)
            )
             # Convertir los resultados a una lista de diccionarios
            resultados_serializados = [
                {
                    'id': resultado.id,
                    'DNI': resultado.DNI,
                    'Nombre': resultado.Nombre,
                    'Apellido': resultado.Apellido,
                    'Fecha_Nacimiento': resultado.Fecha_Nacimiento,
                    'Departamento': resultado.Departamento,
                    'Provincia': resultado.Provincia,
                    'Distrito': resultado.Distrito,
                    'Sexo': resultado.Sexo,
                    'Domicilio': resultado.Domicilio,
                    'Nombre_Padre': resultado.Nombre_Padre,
                    'Nombre_Madre': resultado.Nombre_Madre,
                    'Foto_Persona': resultado.Foto_Persona,
                }
                for resultado in resultados
            ]
            return JsonResponse({'resultados': resultados_serializados, 'opcion': 'Persona'})
    return JsonResponse({})


def RegisterEvento(request):
    if request.method=='POST':
       # Obtén los datos del formulario utilizando request.POST.get
        opcion = request.POST.get('opcion', '')
        departamento = request.POST.get('departamento', '')
        provincia = request.POST.get('provincia', '')
        distrito = request.POST.get('distrito', '')
        fecha_inicio = request.POST.get('fecha_inicio', '')
        fecha_termino = request.POST.get('fecha_termino', '')
        nombreGremio = request.POST.get('nombreGremio', '')
        medida = request.POST.get('medida', '')
        resumenSummary = request.POST.get('resumenSummary', '')
        #Si algun campo de texto llega vacio lo completo como 'Vacio'
        opcion=ValidarCampoVacioTexto(opcion)
        departamento = ValidarCampoVacioTexto(departamento)
        provincia = ValidarCampoVacioTexto(provincia)
        distrito = ValidarCampoVacioTexto(distrito)
        fecha_inicio = ValidarCampoVacioTexto(fecha_inicio)
        fecha_termino = ValidarCampoVacioTexto(fecha_termino)
        nombreGremio = ValidarCampoVacioTexto(nombreGremio)
        medida = ValidarCampoVacioTexto(medida)
        resumenSummary = ValidarCampoVacioTexto(resumenSummary)
        #validacion de formato
        print('opcion =', opcion, 'tipo de opcion =', type(opcion))
        print('departamento =', departamento, 'tipo de departamento =', type(departamento))
        print('provincia =', provincia, 'tipo de provincia =', type(provincia))
        print('distrito =', distrito, 'tipo de distrito =', type(distrito))
        print('fecha_inicio =', fecha_inicio, 'tipo de fecha_inicio =', type(fecha_inicio))
        print('fecha_termino =', fecha_termino, 'tipo de fecha_termino =', type(fecha_termino))
        print('nombreGremio =', nombreGremio, 'tipo de nombreGremio =', type(nombreGremio))
        print('medida =', medida, 'tipo de medida =', type(medida))
        print('resumenSummary =', resumenSummary, 'tipo de resumenSummary =', type(resumenSummary))
        if  not opcion.replace(' ', '').isalpha() or \
            not departamento.replace(' ', '').isalpha() or \
            not provincia.replace(' ', '').isalpha() or\
            not distrito.replace(' ', '').isalpha() or\
            not nombreGremio.replace(' ', '').isalpha() or\
            not medida.replace(' ', '').isalpha() or\
            not resumenSummary.replace(' ', '').isalpha() :
            return JsonResponse({'message': 'Error en el formato'})
        if not validadFecha(fecha_inicio.replace(' ', '')) or not validadFecha(fecha_termino.replace(' ', '')) :
            return JsonResponse({'message': 'Error en la fecha'})
        evento = Evento(
            opcion=opcion,
            departamento=departamento,
            provincia=provincia,
            distrito=distrito,
            fecha_inicio=fecha_inicio,
            fecha_termino=fecha_termino,
            nombreGremio=nombreGremio,
            medida=medida,
            resumenSummary=resumenSummary
        )
        evento.save()
        return JsonResponse({'message': 'Registro exitoso'})
    return JsonResponse({})     
  
def RegisterGremio(request):
    
    if request.method=='POST':
        nombre_gremio = request.POST.get('nameGremio', '')
        ruc_gremio = request.POST.get('rucGremio', '')
        dni_secretario_general = request.POST.get('dniSecretarioGeneral', '')
        nombre_secretario_general = request.POST.get('secretarioGeneral', '')
        dni_dirigente = request.POST.get('dniDirigente', '')
        nombre_dirigente = request.POST.get('dirigente', '')
        dni_presidente = request.POST.get('dniPresidente', '')
        nombre_presidente = request.POST.get('presidente', '')
        
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

        
        if not nombre_gremio.replace(' ', '').isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not ruc_gremio.isdigit() or len(ruc_gremio) != 11:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_secretario_general.isdigit() or len(dni_secretario_general) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_secretario_general.replace(' ', '').isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_dirigente.isdigit() or len(dni_dirigente) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_dirigente.replace(' ', '').isalpha():
            return JsonResponse({'message': 'Error en el formato'})
            
        if not dni_presidente.isdigit() or len(dni_presidente) != 8:
            return JsonResponse({'message': 'Error en el formato'})
            
        if not nombre_presidente.replace(' ', '').isalpha():
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
 #validando los campos antes de ingresar a la BD
def ValidarCampoVacioTexto(campo):
    if campo.replace(' ', '')=='':
        return 'Vacio'
    return campo
def ValidarCampoVacioDni(campo):
    if campo.replace(' ', '')=='':
        return'00000000'
    return campo
def ValidarCampoVacioRuc(campo):
    if campo.replace(' ', '')=='':
        return'00000000000'
    return campo
def validadFecha(cadena):
    # Definir la expresión regular para el formato "yyyy-mm-dd"
    patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Verificar si la cadena cumple con el formato
    if patron.match(cadena):
        return True
    else:
        return False

def register(request):
    return render(request, 'core/register.html')

def analize(request):
    return render(request, 'core/analize.html')

def exit(request):
    logout(request)
    return redirect('home')
