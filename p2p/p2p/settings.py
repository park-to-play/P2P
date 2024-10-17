"""
Django settings for p2p project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""


# 전체 프로젝트의 설정을 관리하는 파일입니다.


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+3563400o7e+_8hcw%8ytr_p(cr6owxnr-6-1#0_x)$c5=k7@k"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

"""
INSTALLED_APPS는 프로젝트에 설치된 앱을 등록하는 곳입니다.
Django에서는 새로운 기능(앱)을 추가할때, 해당 앱이 프로젝트에 인식되도록 이곳에 등록을 해야합니다.
"""

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 생성한 앱
    "rest_framework",
    "location",
    'maps',
    'corsheaders',
]

"""
HTTP 요청과 응답을 처리하는 데 있어 중간 단계에서 개입하는 여러 처리기(미들웨어)를 지정하는 부분입니다.


"""
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "p2p.urls"


"""
Django 프로젝트에서 템플릿 엔진의 설정을 정의하는 부분입니다.
이 설정을 통해 템플릿 파일의 경로와 처리 방법, 추가적으로 사용할 수 있는 옵션들을 설정합니다.
"""

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "p2p.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

"""
Django 프로젝트에서 사용할 데이터베이스를 정의하는 곳입니다.
Django가 어떤 데이터베이스를 사용할지, 데이터베이스에 어떻게 연결할지를 지정합니다.
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

"""
정적 파일(static files)을 제공할 때 사용되는 URL 경로를 지정하는 부분입니다.
"""

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Next.js가 실행 중인 도메인
    'http://127.0.0.1:3000',
]

