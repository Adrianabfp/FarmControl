import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY e DEBUG via variável de ambiente para segurança em produção
SECRET_KEY = os.environ.get('SECRET_KEY', 'sua-chave-de-desenvolvimento-aqui')

DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

# Ajuste os hosts permitidos para seu domínio no Heroku e localhost
ALLOWED_HOSTS = ['farmcontrol-adriana-70ca2f0e56ca.herokuapp.com', 'farmcontrol.onrender.com', 'localhost', '127.0.0.1']

# App de usuários customizado
AUTH_USER_MODEL = 'usuarios.Users'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'estoque',
    'usuarios',
    'rolepermissions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir arquivos estáticos no Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'rolepermissions.middleware.RolePermissionsMiddleware',
]

ROOT_URLCONF = 'farmcontrol.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'farmcontrol'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'farmcontrol.wsgi.application'

# Configuração do banco de dados:
# Usa PostgreSQL 


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'farmcontrol_db',
        'USER': 'farmcontrol_db_user',
        'PASSWORD': 'KTKMgcdgJrqxKbCX6rOIWPR7LCm9TTr5',
        'HOST': 'dpg-d0macpjuibrs73ehhc2g-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}




# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Diretório para collectstatic no Heroku
STATICFILES_DIRS = [BASE_DIR / 'estoque' / 'static']

# Config WhiteNoise para otimizar arquivos estáticos no Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configurações de login
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/usuarios/dashboard/'
LOGOUT_REDIRECT_URL = '/usuarios/login/'

# Role permissions
ROLEPERMISSIONS_MODULE = 'usuarios.roles'

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
