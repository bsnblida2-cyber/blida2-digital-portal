import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-dev-only-key-change-before-deploy')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = [x.strip() for x in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if x.strip()]
CSRF_TRUSTED_ORIGINS = [x.strip() for x in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if x.strip()]
SITE_URL = os.environ.get('SITE_URL', 'http://localhost:8000').rstrip('/')
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.sitemaps','core']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.locale.LocaleMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='config.wsgi.application'
DATABASE_URL=os.environ.get('DATABASE_URL','').strip()
if DATABASE_URL:
 p=urlparse(DATABASE_URL); DATABASES={'default':{'ENGINE':'django.db.backends.postgresql','NAME':p.path.lstrip('/'),'USER':p.username or '', 'PASSWORD':p.password or '', 'HOST':p.hostname or '', 'PORT':str(p.port or 5432),'CONN_MAX_AGE':60,'OPTIONS':{'sslmode':parse_qs(p.query).get('sslmode',['require'])[0]}}}
else:
 DATABASES={'default':{'ENGINE':'django.db.backends.postgresql','NAME':os.environ.get('POSTGRES_DB','blida2'),'USER':os.environ.get('POSTGRES_USER','blida2_app'),'PASSWORD':os.environ.get('POSTGRES_PASSWORD','change-me'),'HOST':os.environ.get('POSTGRES_HOST','db'),'PORT':os.environ.get('POSTGRES_PORT','5432')}}
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='ar'; LANGUAGES=[('ar','العربية'),('fr','Français'),('en','English')]; TIME_ZONE='Africa/Algiers'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATIC_ROOT=BASE_DIR/'staticfiles'; STATICFILES_DIRS=[BASE_DIR/'static']; STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL='media/'; MEDIA_ROOT=BASE_DIR/'media'; DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
SECURE_CONTENT_TYPE_NOSNIFF=True; SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https'); X_FRAME_OPTIONS='DENY'; SECURE_REFERRER_POLICY='strict-origin-when-cross-origin'; SESSION_COOKIE_HTTPONLY=True; CSRF_COOKIE_HTTPONLY=True; SESSION_COOKIE_SAMESITE='Lax'; CSRF_COOKIE_SAMESITE='Lax'
if not DEBUG:
 SECURE_SSL_REDIRECT=os.environ.get('SECURE_SSL_REDIRECT','False').lower()=='true'; SESSION_COOKIE_SECURE=os.environ.get('COOKIE_SECURE','False').lower()=='true'; CSRF_COOKIE_SECURE=os.environ.get('COOKIE_SECURE','False').lower()=='true'; SECURE_HSTS_SECONDS=int(os.environ.get('HSTS_SECONDS','0')); SECURE_HSTS_INCLUDE_SUBDOMAINS=False; SECURE_HSTS_PRELOAD=False
