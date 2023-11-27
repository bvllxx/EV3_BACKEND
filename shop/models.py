from django.db import models

class Album(models.Model):
    product_id = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    band_name = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()
    subgenre = models.CharField(max_length=50)
    description = models.TextField()
    price_clp = models.DecimalField(max_digits=10, decimal_places=6)  
    image = models.ImageField(upload_to='projects', verbose_name="Foto")
    stock = models.IntegerField()

    class Meta:
        verbose_name="Album"
        verbose_name_plural="Albums"

    def __str__(self):
        return self.title