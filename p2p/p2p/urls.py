"""
URL configuration for p2p project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



"""
Django 프로젝트의 URL 경로와 그 경로에 대한 처리를 정의하는 리스트입니다.
모든 Django 프로젝트는 urls.py 파일에 이 리스트를 정의해야 합니다.
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include('maps.urls')),
]
