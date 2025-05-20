from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.views import LoginView  
from django.urls import reverse_lazy
from .models import Users



# view de login com redirecionamento
class LoginRedirecionadoView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')



@login_required
def dashboard(request):
    is_gestor = request.user.cargo == 'G'
    is_temporarily_atendente = request.user.is_temporarily_atendente
    return render(request, 'usuarios/dashboard.html', {
        'is_gestor': is_gestor,
        'is_temporarily_atendente': is_temporarily_atendente,
    })

@login_required
def perfil_gestor(request):
    # Só permite acesso se for gestor (cargo G)
    if request.user.cargo != 'G':
        # Se não for gestor, pode redirecionar para dashboard 
        return redirect('dashboard')
    
    return render(request, 'usuarios/perfil_gestor.html', {
        'user': request.user,
    })

# View para alternar o cargo de Gestor para Atendente
@login_required
def alternar_para_atendente(request):
    if request.user.cargo == 'G':
       request.user.is_temporarily_atendente = not request.user.is_temporarily_atendente
       request.user.save()
       return redirect('dashboard') 
    return redirect('login')



@login_required
def configuracoes(request):
    return render(request, 'usuarios/configuracoes.html')



@has_permission_decorator ('cadastrar_atendente')
def cadastrar_atendente(request):
    return render(request, 'cadastrar_atendente.html')



# Create your views here.
