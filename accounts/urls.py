from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import register_view


urlpatterns = [
    path('register/', views.register_view, name="register" ),
]