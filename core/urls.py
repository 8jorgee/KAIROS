"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from .views import home, registros, historial, experimento, materia_prima, confrontar, PLC, exit


urlpatterns = [
    path('', home, name='home'),
    path('registros/', registros, name='registros'),
    path('logout/', exit, name='exit'),
    path('historial/', historial, name='historial'),
    path('PLC/', PLC, name='PLC'),
    path('materia_prima/', materia_prima, name='materia_prima'),
    path('experimento/', experimento, name='experimento'),
    path('confrontar/', confrontar, name='confrontar'),
]
