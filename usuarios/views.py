from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator


@has_permission_decorator ('cadastrar_atendente')
def cadastrar_atendente(request):
    return HttpResponse ('teste')

# Create your views here.
