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
def putPoll(request):

    if request.method == "GET":
        #data = json.loads(request.body)
        total = Users.objects.all()
        print('total: ',total)
        print(total[0])
        return JsonResponse({"Hola":'GET'})

    if request.method == "POST":

        data = json.loads(request.body)
        hashed = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
        user = Users(nombre = data['nombre'],correo = data['correo'], password = hashed)
        user.save()
        encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30), 'user':user.correo},(os.environ.get('SECRET_JWT') or 'secret'), algorithm='HS256')
        return JsonResponse({"Hola":'POST','encoded_jwt':encoded_jwt.decode('ascii')})

    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'PUT','data':data})

    if request.method == "DELETE":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'DELETE','data':data})



