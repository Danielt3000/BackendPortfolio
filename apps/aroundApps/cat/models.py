from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Cat(models.Model):
    class Meta(object):
        db_table = 'categoriesAround'

    name = models.CharField(
        'Name', max_length=50, null=False, blank=False
    )
    image = CloudinaryField(
        'Image', null=False, blank=True
    )

    def __str__(self):
        return self.name