from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def fruit_list(request):
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    return render(request, 'fruits/fruits.html', {'fruits': fruits})
    # return JsonResponse({'Msg': 'Ok'})
