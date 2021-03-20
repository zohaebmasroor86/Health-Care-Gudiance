"""zuhaibproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from zuhaibApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gun/', views.biss_view),
    path('veg/', views.veg_view),
    path('nonveg/', views.nonveg_view),
    path('feedback/', views.feedback_view),
    path('submit/', views.submit_view),
    path('protein/', views.protein_view),
    path('daibetes/', views.daibetes_view),
    path('health/', views.health_view),
    path('blood/', views.blood_view),
    path('carbo/', views.carbo_view),
    path('order/', views.order_view),
    path('veglist/', views.veglist_view),
    path('nonveglist/', views.nonveglist_view),
    path('register/', views.register_view),

]
