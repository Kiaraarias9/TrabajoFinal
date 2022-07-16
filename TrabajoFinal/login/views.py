from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm

# Create your views here.

#login

def login_request(request):
    
      if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  
                  if user is not None:
                        login(request, user)

                        return render (request, "core/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        
                        return render (request, "login/login.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login/login.html", {"mensaje":"Formulario erroneo"})
      

      form = AuthenticationForm()
      return render(request, "login/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "core/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "login/registro.html", {"form": form})
