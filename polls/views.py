from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from polls.models import Users
import os
import json
import jwt
import bcrypt
import datetime

def  index(request):
    return HttpResponse("Hello world, estas en poll index")

@csrf_exempt 
def crudPoll(request):

    if request.method == "GET":
        data = json.loads(request.body)
        correo = data['correo']
        user = None
        try:
            user = Users.objects.get(correo=correo)
        except:
            return JsonResponse({'ok':False,'message':'No se encontro el correo'})

        if bcrypt.checkpw(data['password'].encode('ASCII'),user.password.encode('ASCII')):
            encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
                                        'nombre':user.nombre, 
                                        'correo':user.correo},
                                        (os.environ.get('SECRET_JWT') or 'secret'),
                                        algorithm='HS256')

            return JsonResponse({"Hola":'GET','encoded_jwt':encoded_jwt.decode('ascii')})

        else:
            return JsonResponse({'ok':False,'message':'Contraseña incorrecta'})

    if request.method == "POST":

        data = json.loads(request.body)
        hashed = bcrypt.hashpw(data['password'].encode('ASCII'), bcrypt.gensalt())
        user = Users(nombre = data['nombre'],correo = data['correo'], password = hashed.decode('ASCII'))
        user.save()
        encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
                                    'nombre':user.nombre, 
                                    'correo':user.correo},
                                    (os.environ.get('SECRET_JWT') or 'secret'),
                                    algorithm='HS256')

        return JsonResponse({"Hola":'POST','encoded_jwt':encoded_jwt.decode('ascii')})

    if request.method == "PUT":
        data = json.loads(request.body)
        correo = data['correo']
        user = Users.objects.get(correo=correo)

        user.nombre = data['nombre']
        user.save()
        return JsonResponse({"Hola":'PUT','Guardadado':True})

    if request.method == "DELETE":
        data = json.loads(request.body)

        try: 

            user = Users.objects.get(correo=data['correo'])
            user.delete()
            
            return JsonResponse({'ok':True,'message':'objeto borrado con exito'})

        except:
            return JsonResponse({'ok':False,'message':'El objeto no se encuentra en la base de datos'})
        



