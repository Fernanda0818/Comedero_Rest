from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, nombre, apellidos, correo, usuario, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            nombre = nombre,
            apellidos= apellidos,
            correo = correo,
            usuario = usuario,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,nombre,apellidos, correo, usuario , password=None, **extra_fields):
        return self._create_user(nombre,apellidos, correo, usuario,  password, False, False, **extra_fields)

    def create_superuser(self,nombre,apellidos, correo, usuario, password=None, **extra_fields):
        return self._create_user(nombre, apellidos, correo, usuario,  password, True, True, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    nombre = models.CharField('Nombres', max_length=100, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    correo = models.EmailField('Correo Electrónico',max_length=200, unique=True, null=True)
    usuario = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre','apellidos','correo']

    def _str_(self):
        return f'{self.usuario}'