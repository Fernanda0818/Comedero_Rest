from django.db import models

def upload_to(instance, filename):
   return 'images/{filename}'.format(filename=filename)
    
class Mascota(models.Model):
    idMascota = models.AutoField(auto_created=True, primary_key=True)
    fotografia = models.ImageField(null=True, blank=True, upload_to=upload_to)
    nombre = models.CharField(null=False, blank=False, max_length=200)
    sexo = models.CharField( null=False, blank=False, max_length=200, 
                            choices=[('Macho', 'Macho'),('Hembra', 'Hembra')],
                            default='Macho')
    edad = models.IntegerField(null=False, blank=False, )
    talla = models.CharField(null=False, blank=False, max_length=20,
                            choices=[('Chica', 'Chica'),('Mediano', 'Mediano'),('Grande', 'Grande')],
                            default='Chica')

    def _str_(self):
        return "{} {}".format(self.idMascota, self.nombre)