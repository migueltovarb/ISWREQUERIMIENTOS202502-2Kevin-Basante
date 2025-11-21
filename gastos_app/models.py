from django.db import models
from django.contrib.auth.models import User

class Movimiento(models.Model):
    TIPO_CHOICES = [
        ('GASTO', 'Gasto'),
        ('INGRESO', 'Ingreso'),
    ]
    
    CATEGORIA_GASTOS = [
        ('COMPRAS', 'Compras'),
        ('ALIMENTOS', 'Alimentos'),
        ('TELEFONO', 'Teléfono'),
        ('EDUCACION', 'Educación'),
        ('BELLEZA', 'Belleza'),
        ('ENTRENAMIENTO', 'Entrenamiento'),
    ]
    
    CATEGORIA_INGRESOS = [
        ('SALARIO', 'Salario'),
        ('INVERSIONES', 'Inversiones'),
        ('MEDIO_TIEMPO', 'Medio tiempo'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    categoria = models.CharField(max_length=20)
    nota = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    cuenta = models.CharField(max_length=20, default='invitado')  # 'invitado', '1', '2'
    
    def __str__(self):
        return f"{self.tipo} - {self.categoria} - ${self.valor} - Cuenta: {self.cuenta}"