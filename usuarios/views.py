from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator

def cadastrar_atendente(request):
    return HttpResponse ('teste')

# Create your views here.
