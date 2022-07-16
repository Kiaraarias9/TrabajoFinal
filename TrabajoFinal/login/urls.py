from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name="login"),
    path('registro', views.register, name="registro"),
]