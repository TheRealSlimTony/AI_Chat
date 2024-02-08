from django.db import models


class Mensaje(models.Model):
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje[:50]
