from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from polls.models import Users


import json
def  index(request):
    return HttpResponse("Hello world, estas en poll index")

@csrf_exempt 
def putPoll(request):

    if request.method == "GET":
        #data = json.loads(request.body)
        total = Users.objects.all()
        print('total: ',total)
        print(total[0])
        return JsonResponse({"Hola":'DELETE'})

    if request.method == "POST":
        data = json.loads(request.body)
        user = Users(nombre = data['nombre'],correo = data['correo'], password = data['password'])
        user.save()

        return JsonResponse({"Hola":'POST','data':data,'id':user.id})

    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'PUT','data':data})

    if request.method == "DELETE":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'DELETE','data':data})



