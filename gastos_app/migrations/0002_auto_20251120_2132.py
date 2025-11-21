# gastos_app/migrations/0002_add_cuenta_field.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('gastos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='cuenta',
            field=models.CharField(default='invitado', max_length=20),
        ),
    ]