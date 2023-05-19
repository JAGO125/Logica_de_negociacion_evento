"""
URL configuration for LOGICA_DE_NEGOCIACION_EVENTO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from LOGICA_DE_NEGOCIACION_EVENTO.views import hola_mundo,cerrar_sesion,saludo_nombre,sumar
from LOGICA_DE_NEGOCIACION_EVENTO.views import hola_mundo
from LOGICA_DE_NEGOCIACION_EVENTO.views import cerrar_sesion
from LOGICA_DE_NEGOCIACION_EVENTO.views import saludo_nombre
from LOGICA_DE_NEGOCIACION_EVENTO.views import sumar
from LOGICA_DE_NEGOCIACION_EVENTO.view_project_evento import abrir_REPS,abrir_MAESTRA


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', hola_mundo),
    path("estado/", cerrar_sesion),
    path("name/<str:apellido>", saludo_nombre ),
    path("operacion/<int:num1>/<int:num2>",sumar),
    path("reps/",abrir_REPS),
    path("maestra/",abrir_MAESTRA),
]
