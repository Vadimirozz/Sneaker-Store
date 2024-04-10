from django.db import models
from django.contrib.auth.models import User

class Sneakers(models.Model):
    image = models.ImageField(upload_to="main/images/sneakers/")
    name = models.CharField('Name', max_length=50)
    price = models.CharField('Price', max_length=15)
    description = models.CharField('Description', max_length=250, default='Description')
    sizes = models.CharField('Available Sizes', max_length=250, default='40')
    post_description = models.TextField('Post-Description')

    class Meta:
        verbose_name = 'Sneaker'
        verbose_name_plural = 'Sneakers'

    def __str__(self):
        return self.name

