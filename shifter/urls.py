"""
URL configuration for shifter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('client_management/', include('client_management.urls', namespace='client_management')),
    #path('personnel_management/', include('personnel_management.urls', namespace='personnel_management')),
    path('agent_mgn/', include('agent_mgn.urls', namespace='agent_mgn')),
    #path('scheduler/', include('scheduler.urls', namespace='scheduler')),
    #path('payment_management/', include('payment_management.urls', namespace='payment_management')),
    #path('incident_management/', include('incident_management.urls', namespace='incident_management')),
    #path('user_management/', include('user_management.urls', namespace='user_management')),
    #path('authentication_management/', include('authentication_management.urls', namespace='authentication_management')),
    #path('log_management/', include('log_management.urls', namespace='log_management')),
]
