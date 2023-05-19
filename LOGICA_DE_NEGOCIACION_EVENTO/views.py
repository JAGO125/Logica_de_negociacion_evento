from django.http import HttpResponse
def hola_mundo(request):
    return HttpResponse("Primera aplicacion")
def cerrar_sesion(request):
    return HttpResponse("Su sesion ha sido cerrada")



def saludo_nombre(request,apellido):
    nombre = apellido
    return HttpResponse("Hola " + nombre)

"""def sumar(request,num1,num2):
    numero1 = int (num1)
    numero2 = int(num2)
    suma = numero1 + numero2
    return HttpResponse("La suma es "+ str (suma))"""

def sumar_numeros(numero1,numero2):
    suma = int (numero1) + int (numero2)
    return str (suma)


    
def sumar(request,num1,num2):
    numero1 = int (num1)
    numero2 = int(num2)
    suma = sumar_numeros(numero1,numero2)
    return HttpResponse("La suma es "+ str (suma))


