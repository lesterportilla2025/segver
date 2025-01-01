from django.shortcuts import render, redirect, reverse
#Librerias para acceder a los pasos de informacion desde el simulador
from rest_framework import viewsets, views
from rest_framework import permissions
from rest_framework.response import Response
import logging
#librerias para convertir en json lo que se retorna desde el simulador
import json
#from django.db import models
#from models.AdmUsuarios import AdmUsuarios
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.db import connection, DatabaseError, Error

# Create your views here.
def login(request):
	return render(request,'login/index.php')
class login_calidad(views.APIView):
    def post(self, request):
        #Obtener el json del lo que se envio desde la vista
        #data = json.load(request)
        data = request.data
        #Impresion del JSON
        print(data)
        usuario = data.get('Username')
        password = data.get('Password')
        print(usuario)
        print(password)
        #Consulta a la base de datos
        try:
            with connection.cursor() as cursor:
                cursor.callproc('CONSULTAR_INGRESO', [usuario, password])
                row=dictfetchall(cursor)
                #Comando para limpiar el cursor
                cursor.nextset()
                if not row:
                    cursor.callproc('CONSULTAR_PREINGRESO', [usuario])
                    row2=dictfetchall(cursor)
                    if not row2:
                        print("Usuario No autorizado")
                        data = {'message': 'noautorizado','mextendido':'Usuario no Autorizado'}
                    else:
                        print("Usuario en Preingreso")
                        data = {'message': 'enpreingreso','mextendido':'Usuario en Preingreso'}
                    #return JsonResponse(data)
                else:
                    #Usuario activo para ingreso
                    print(row[0])
                    print(row[0]['nombre'])
                    print("Usuario autorizado")
                    data = {'message': 'autorizado','mextendido':'Usuario Autorizado'}
                    data_principal={'nombre':row[0]['nombre'][0:12]}
                    cursor.callproc('CONSULTAR_MENU', [usuario])
                    row3=dictfetchall(cursor)
                    data_menu={'menu':row3[0]}
                    print(data)
                    print(row3)
                    #Redirigir a la pagina de ingreso
                    #return JsonResponse(row, safe=False)
        except Error as e:
            print("Failed to execute stored procedure: {}".format(e))
            data = {'message': 'error','mextendido':'Ingrese los datos correctos'}
        print(data['message'])
        if data['message']=='autorizado':
            print(data_principal)
            return render(request,'principal/index.html', {'data_principal': data_principal, 'data_menu': row3})
        else:
            return render(request,'login/index.php', data)
# Aqui se llama la funcion para mostar la bitacora
def mostrar_creacion_bitacora(request):
    return render(request,'digitacion/creacion_bitacora.html')
# Aqui se llama la funcion para mostar la gestion de usuarios
def mostrar_gestion_usuarios(request):
    return render(request,'general/gestion_usuarios.html')
def mostrar_cargue_planos(request):
    return render(request,'informes/cargue_planos.html')
def dictfetchall(cursor):
    ##Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def namedtuplefetchall(cursor):
    ##Return all rows from a cursor as a namedtuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
#########
#########
