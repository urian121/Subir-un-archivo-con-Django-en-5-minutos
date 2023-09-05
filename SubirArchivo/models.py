from django.db import models

# Create your models here.


class Archivo(models.Model):
    title = models.CharField(max_length=200)
    archivo = models.FileField(upload_to="Mis_archivos/")
    date_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "archivos"
        ordering = ['-date_at']
