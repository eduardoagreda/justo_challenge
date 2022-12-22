from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Fecha y hora de creación de hit', auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name='Fecha y hora de modificación de hit', auto_now = True)
    active     = models.BooleanField(verbose_name='Bandera de eliminación de datos', default=True)

    class Meta:
        abstract = True
        ordering = ('-created_at')