from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def greet(request):
    return HttpResponse('Good Morning Tharun')

def message(request):
    return JsonResponse({'message': 'This is a message'})