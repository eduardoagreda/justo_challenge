#importacion de modelos
from django.contrib.auth import get_user_model
from django.db import models

# importacion de librerias utils 
from utils.base_model import BaseModel


class Hit(BaseModel):
    '''
        Clase que representa la tabla para los hits.

        Tiene los campos siguientes:
            name: nombre del hit.
            description: descripción del hit.
            assign_hitman: asesino asignado al hit.
            failed_mission: bandera que nos indica si la misión fue exitosa o fallida
            created_at: fecha y hora en que se creó el hit.
            updated_at: fecha y hora en que se modificó el hit.
    '''

    name            = models.CharField(verbose_name='Nombre del asesinato', max_length=50, blank=True, null=True)
    description     = models.TextField(verbose_name='Descripción del asesinato', blank=True, null=True)
    failed_mission  = models.BooleanField(verbose_name='Bandera de misión fallida', blank=True, null=True)
    assign_hitmans   = models.ForeignKey(get_user_model(), verbose_name='Asesino que asignado a la misión',
                                            related_name='assign_hitmans', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.name)