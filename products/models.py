from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=100, verbose_name="nombre")

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name