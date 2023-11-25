from django.db import models

class ImgProducts(models.Model):
    #id = models.AutoField(_(""))
    name = models.CharField(max_length=80,verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    price = models.FloatField(verbose_name="Precio")
    image = models.ImageField(upload_to='projects', verbose_name="Foto")

    class Meta:
        verbose_name="Tienda"
        verbose_name_plural="Tienda"

    def __str__(self):
        return self.name
