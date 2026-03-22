from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    if request.method == 'GET':
        return HttpResponse('Hello Blog!')
    else:
        return HttpResponse(f'Method: {request.method}')
