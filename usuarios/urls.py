from django.urls import path
from . import views
from .views import LoginRedirecionadoView, dashboard, alternar_para_atendente
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginRedirecionadoView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('alternar/', alternar_para_atendente, name='alternar_para_atendente'),
    path('cadastrar_atendente/', views.cadastrar_atendente, name='cadastrar_atendente'),
    path('perfil-gestor/', views.perfil_gestor, name='perfil_gestor'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),


]


