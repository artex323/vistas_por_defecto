from django.db import models
from django.utils import timezone

class Libro(models.Model):
    # Define tus campos aquí
    titulo = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    autor = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    img =models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

