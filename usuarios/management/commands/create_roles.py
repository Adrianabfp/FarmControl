from django.core.management.base import BaseCommand
from rolepermissions.roles import assign_role

class Command(BaseCommand):
    help = 'Cria roles iniciais'

    def handle(self, *args, **kwargs):
        from django.contrib.auth.models import User
        from usuarios.roles import Gestor, Atendente
        
        # Verifica se já existe um usuário "Gestor" para não duplicar
        if not User.objects.filter(username='gestor').exists():
            gestor = User.objects.create_user(username='gestor', password='senha123')
            assign_role(gestor, Gestor)  # Atribui a role Gestor ao usuário
        
        # Cria usuário Atendente e atribui a role Atendente
        if not User.objects.filter(username='atendente').exists():
            atendente = User.objects.create_user(username='atendente', password='senha123')
            assign_role(atendente, Atendente)  # Atribui a role Atendente ao usuário
          
        self.stdout.write(self.style.SUCCESS('Roles criadas com sucesso'))

