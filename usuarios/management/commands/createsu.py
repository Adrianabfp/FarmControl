from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'senha123')
            self.stdout.write(self.style.SUCCESS('Superuser criado com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser já existe.'))

