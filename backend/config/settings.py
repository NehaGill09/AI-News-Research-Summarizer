import os
from pathlib import Path
import dj_database_url
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','unsafe-local-dev-key-change-me')
DEBUG=os.getenv('DJANGO_DEBUG','0')=='1'
ALLOWED_HOSTS=[x.strip() for x in os.getenv('DJANGO_ALLOWED_HOSTS','localhost,127.0.0.1').split(',') if x.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','rest_framework','rest_framework_simplejwt','corsheaders','research']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','corsheaders.middleware.CorsMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='config.wsgi.application'
ASGI_APPLICATION='config.asgi.application'
DATABASES={'default':dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",conn_max_age=600)}
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'}]
LANGUAGE_CODE='en-us'; TIME_ZONE='UTC'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
CORS_ALLOWED_ORIGINS=[x.strip() for x in os.getenv('CORS_ALLOWED_ORIGINS','http://localhost:5173').split(',') if x.strip()]
REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework_simplejwt.authentication.JWTAuthentication'],'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.AllowAny'],'DEFAULT_THROTTLE_CLASSES':['rest_framework.throttling.AnonRateThrottle','rest_framework.throttling.UserRateThrottle'],'DEFAULT_THROTTLE_RATES':{'anon':'120/hour','user':'1000/hour'},'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':10}
NEWS_API_KEY=os.getenv('NEWS_API_KEY',''); NEWS_API_BASE_URL=os.getenv('NEWS_API_BASE_URL','https://newsapi.org/v2')
AI_API_KEY=os.getenv('AI_API_KEY',''); AI_API_BASE_URL=os.getenv('AI_API_BASE_URL','https://api.openai.com/v1'); AI_MODEL=os.getenv('AI_MODEL','gpt-4o-mini')
