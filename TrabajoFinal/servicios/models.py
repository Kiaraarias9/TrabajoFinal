from django.db import models


# Create your models here.
class Servicios(models.Model):
    categoria = models.CharField(max_length=200, verbose_name="Category")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="Masajes")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "masajes"
        verbose_name_plural = "masajes"
        ordering = ['-creado']

    def __str__(self):
        return self.title