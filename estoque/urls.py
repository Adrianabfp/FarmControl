from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from usuarios.views import LoginRedirecionadoView


urlpatterns = [
    # Páginas de controle de estoque
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('adicionar-medicamento/', views.adicionar_medicamento, name='adicionar_medicamento'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'), 
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),

    # Páginas de login
    path('login/', LoginRedirecionadoView.as_view(), name='login'),  # Usa sua view customizada
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
