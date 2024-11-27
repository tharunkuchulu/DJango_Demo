from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def greet(request):
    return HttpResponse('Good Morning Tharun')

def message(request):
    return JsonResponse({'message': 'This is a message'})

def details(request):
    return HttpResponse('This is details')

from django.http import JsonResponse

def calculator(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return JsonResponse({"error": "Invalid input. 'a' and 'b' must be valid numbers."}, status=400)

    results = {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": "Undefined (Division by zero)" if b == 0 else a / b,
    }
    return JsonResponse({"results": results})

    # http://127.0.0.1:8000/demo1/calculator/?a=10&b=5 use this type of url to display the results (values given in the format of a,b)