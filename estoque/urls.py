from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    # Paginas de controle de estoque
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('adicionar-medicamento/', views.adicionar_medicamento, name='adicionar_medicamento'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),  # 👈 este aqui
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
    #Paginas de login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
