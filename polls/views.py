from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
# should access Model objects and use Templates to prepare responses.
    response_data = {
            "Message": "Hello World!"
            }
    return JsonResponse(response_data)
# return render(request, 'polls/index.html')

