from django.shortcuts import render
from .models import Alumno

# Create your views here.
def principal(request):
    obj = Alumno.objects.raw('select * from cronos_alumno')
    context = {
        'data': obj
    }
    return (render(request, 'index.html',context))