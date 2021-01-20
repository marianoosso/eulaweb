from django.db import models

# Create your models here.

class Escuela(models.Model):
    descripcion = models.TextField(null=True)
    codigo = models.TextField(null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.descripcion + ':' + self.codigo