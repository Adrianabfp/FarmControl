from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar_atendente/', views.cadastrar_atendente, name='cadastrar_atendente')
]


