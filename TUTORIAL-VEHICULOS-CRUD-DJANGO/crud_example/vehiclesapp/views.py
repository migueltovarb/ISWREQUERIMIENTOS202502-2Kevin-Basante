from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import vehiculo
from .forms import VehicleForm

# Vista para listar todos los vehículos
def list_view(request):
    vehicles = vehiculo.objects.all()
    
    # DEBUG: Ver qué estamos enviando a la plantilla
    print(f"🔍 Número de vehículos encontrados: {vehicles.count()}")
    for v in vehicles:
        print(f"   - {v.placa} | {v.marca} | {v.color} | {v.modelo}")
    
    return render(request, "list_view.html", {'vehicles': vehicles})

# Vista para crear un nuevo vehículo
def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, "create_view.html", context)

# Vista para actualizar un vehículo existente
def update_view(request, id):
    context = {}
    obj = get_object_or_404(vehiculo, id=id)
    form = VehicleForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, "update_view.html", context)

# Vista para eliminar un vehículo
def delete_view(request, id):
    obj = get_object_or_404(vehiculo, id=id)
    
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "delete_view.html", {'vehicle': obj})

# Vista de prueba "Hello World"
def hello_world(request):
    return render(request, "hello_world.html")