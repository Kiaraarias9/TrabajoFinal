from django.shortcuts import render
from .models import Servicios

# Create your views here.

def agregarServicios(request):
    form = Servicios()
    data = {'form':form}
    if request.method == 'POST':
        miformulario = Servicios(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            miformulario.save()
            data['mensaje'] = "Datos Resgistrados"
            return render(request, '/servicios.html')
    else:
        miformulario= Servicios()
    return render(request, '', data)

def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, "servicios/servicios.html", {'servicios':servicios})