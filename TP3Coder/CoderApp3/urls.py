from django.contrib import admin
from django.urls import path
from CoderApp3.views import inicio, dtFormulario, socioFormulario, jugadorFormulario

urlpatterns = [
    path('', inicio),
    path('jugadores/', jugadorFormulario, name= "jugadores"),
    path('Dts/', dtFormulario, name= "DTs"),
    path('socio/', socioFormulario, name= "socio"),
]