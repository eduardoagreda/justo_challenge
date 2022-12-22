# Utils
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Models
from django.db import models
from utils.models import BaseModel
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel): 
    USERS_CHOICES = [
        ('hitman', 'Hitman'),
        ('manager', 'Manager')
    ]
    first_name = models.CharField(_("Nombre"), max_length=150, blank=True)
    last_name = models.CharField(_("Apellidos"), max_length=150, blank=True)
    email = models.EmailField(_('Correo Electrónico'), unique=True, blank=False)
    user_type = models.CharField(_('Tipo de usuario'), max_length=8, choices=USERS_CHOICES, default='hitman', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(_('Descipción del Hitman'), blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    # @property
    # def token(self):
    #     token = jwt.encode({'email': self.email, 'exp': datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')
    #     return token