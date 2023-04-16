from django.shortcuts import render
from django.http import HttpResponse
from CoderApp3.models import Jugador, DT, Socio
# Create your views here.

def inicio(self):

    return render(self,"inicio.html")


def jugadores(request):
    print('method: ', request.method)
    print ('post ', request.POST) 
    if request.method == 'POST':
        jugador = Jugador(nombre=request.post['nombre'], apellido=request.post['apellido'], email=request.post['email'], numero=request.post['nro'])
        jugador.save() 
        
    return render(request,"jugadores.html")   

def DTs(request):
    print('method: ', request.method)
    print ('post ', request.POST) 
    if request.method == 'POST':
        jugador = DT(nombre=request.post['nombre'], apellido=request.post['apellido'], equipo=request.post['equipo'])
        jugador.save() 
    return render(request,"DT.html")

def socio(request):
    print('method: ', request.method)
    print ('post ', request.POST) 
    if request.method == 'POST':
        jugador = Socio(nombre=request.post['nombre'], apellido=request.post['apellido'], SocioNro=request.post['SocioNro'])
        jugador.save() 
    return render(request,"socio.html")


def jugadorFormulario (request):
   

    return render(request, 'jugadores.html')

def socioFormulario (request):
    return render(request, 'socio.html')

def dtFormulario (request):
  
 return render(request, 'DT.html')