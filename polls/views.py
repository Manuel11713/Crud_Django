from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def  index(request):
    return HttpResponse("Hello world, estas en poll index")

@csrf_exempt 
def putPoll(request):

    if request.method == "GET":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'DELETE','data':data})

    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'POST','data':data})

    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'PUT','data':data})

    if request.method == "DELETE":
        data = json.loads(request.body)
        return JsonResponse({"Hola":'DELETE','data':data})



