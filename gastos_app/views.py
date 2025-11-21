from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movimiento

# agregar vista para login
def login_view(request):
    if request.method == 'POST':
        return redirect('inicio')
    return render(request, 'gastos_app/login.html')

# Agregar vista para modo invitado
def modo_invitado(request):
    messages.success(request, 'Modo invitado activado')
    return redirect('inicio')

# agregar vista para inicio
def inicio(request):
    # Obtener el tipo de cuenta desde la URL
    cuenta = request.GET.get('cuenta', 'invitado')
    
    # Filtrar movimientos por cuenta
    movimientos = Movimiento.objects.filter(cuenta=cuenta).order_by('-fecha')
    
    # Calcular totales
    total_gastos = sum(m.valor for m in movimientos if m.tipo == 'GASTO')
    total_ingresos = sum(m.valor for m in movimientos if m.tipo == 'INGRESO')
    saldo = total_ingresos - total_gastos
    
    # Determinar el nombre de la cuenta para mostrar
    nombre_cuenta = "Invitado"
    if cuenta == '1':
        nombre_cuenta = "Cuenta 1"
    elif cuenta == '2':
        nombre_cuenta = "Cuenta 2"
    
    context = {
        'movimientos': movimientos,
        'total_gastos': total_gastos,
        'total_ingresos': total_ingresos,
        'saldo': saldo,
        'cuenta_actual': cuenta,
        'nombre_cuenta': nombre_cuenta,
    }
    return render(request, 'gastos_app/inicio.html', context)

# agregar vista para agregar gastos
def agregar_gasto(request):
    # Obtener la cuenta actual desde la URL
    cuenta = request.GET.get('cuenta', 'invitado')
    
    if request.method == 'POST':
        categoria = request.POST.get('categoria', 'COMPRAS')
        nota = request.POST.get('nota', '').strip()
        valor = request.POST.get('valor', 0)
        
        # Validaciones
        if not nota:
            messages.error(request, 'La nota no puede estar vacía')
            return render(request, 'gastos_app/agregar_gasto.html', {'cuenta_actual': cuenta})
        
        if not valor or float(valor) <= 0:
            messages.error(request, 'El valor debe ser mayor a 0')
            return render(request, 'gastos_app/agregar_gasto.html', {'cuenta_actual': cuenta})
        
        # Crear el movimiento con la cuenta específica
        movimiento = Movimiento(
            tipo='GASTO',
            categoria=categoria,
            nota=nota,
            valor=valor,
            cuenta=cuenta  # ← ¡IMPORTANTE! Guardar la cuenta correcta
        )
        movimiento.save()
        messages.success(request, f'Gasto de ${valor} agregado correctamente a {cuenta}')
        return redirect(f'/inicio/?cuenta={cuenta}')  # ← Redirigir manteniendo la cuenta
    
    return render(request, 'gastos_app/agregar_gasto.html', {'cuenta_actual': cuenta})

# Agregar vista para agregar ingresos
def agregar_ingreso(request):
    # Obtener la cuenta actual desde la URL
    cuenta = request.GET.get('cuenta', 'invitado')
    
    if request.method == 'POST':
        categoria = request.POST.get('categoria', 'SALARIO')
        nota = request.POST.get('nota', '').strip()
        valor = request.POST.get('valor', 0)
        
        # Validaciones
        if not nota:
            messages.error(request, 'La nota no puede estar vacía')
            return render(request, 'gastos_app/agregar_ingreso.html', {'cuenta_actual': cuenta})
        
        if not valor or float(valor) <= 0:
            messages.error(request, 'El valor debe ser mayor a 0')
            return render(request, 'gastos_app/agregar_ingreso.html', {'cuenta_actual': cuenta})
        
        # Crear el movimiento con la cuenta específica
        movimiento = Movimiento(
            tipo='INGRESO',
            categoria=categoria,
            nota=nota,
            valor=valor,
            cuenta=cuenta  # ← ¡IMPORTANTE! Guardar la cuenta correcta
        )
        movimiento.save()
        messages.success(request, f'Ingreso de ${valor} agregado correctamente a {cuenta}')
        return redirect(f'/inicio/?cuenta={cuenta}')  # ← Redirigir manteniendo la cuenta
    
    return render(request, 'gastos_app/agregar_ingreso.html', {'cuenta_actual': cuenta})

#Boton eliminar movimiento
def eliminar_movimiento(request, movimiento_id):
    if request.method == 'POST':
        try:
            movimiento = Movimiento.objects.get(id=movimiento_id)
            cuenta = movimiento.cuenta  # Obtener la cuenta del movimiento
            movimiento.delete()
            messages.success(request, 'Movimiento eliminado correctamente')
            return redirect(f'/inicio/?cuenta={cuenta}')  # ← Redirigir a la cuenta correcta
        except Movimiento.DoesNotExist:
            messages.error(request, 'El movimiento no existe')
    
    return redirect('inicio')
#Boton volver
def volver_login(request):
    return redirect('login')