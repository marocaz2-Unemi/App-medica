from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=[("pendiente", "Pendiente"), ("atendida", "Atendida")])


class AtencionMedica(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    costo = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_atencion = models.DateField(auto_now_add=True)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dosis = models.CharField(max_length=100)

class RecetaMedica(models.Model):
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    indicaciones = models.TextField()


class ServicioAdicional(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=7, decimal_places=2)

class AtencionServicio(models.Model):
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
