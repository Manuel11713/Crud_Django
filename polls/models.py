from django.db import models

class Users(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.correo