from django.db import models

class Paciente (models.Model):
    nome= models.CharField(max_length=50)
    dt_nasc= models.DateField ()
    cpf= models.CharField(max_length=11)
    sexo= models.CharField(max_length=1)

class Medico (models.Model):
    crm= models.CharField(max_length=50)
    nome= models.CharField (max_length=50)
    especialidade= models.CharField(max_length=50)
    idade= models.IntegerField()

class Medicamento(models.Model):
    nome= models.CharField(max_length=50)
    valor= models.DecimalField(max_digits= 30, decimal_places=2)
    gravida= models.BooleanField()