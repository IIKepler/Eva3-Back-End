from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=200)),
                ('apellido_empleado', models.CharField(max_length=100)),
                ('email_empleado', models.EmailField(max_length=50)),
                ('edad_empleado', models.IntegerField()),
                ('genero_empleado', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=80)),
                ('salario_empleado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('foto_empleado', models.ImageField(blank=True, null=True, upload_to='fotos_empleados/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'empleados',
                'ordering': ['-created_at'],
            },
        ),
    ]
