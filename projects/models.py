from django.db import models
from cloudinary.models import CloudinaryField



class Project(models.Model):
    
    name = models.CharField(max_length=18)

    about = models.CharField(max_length=200)

    github= models.CharField(max_length=400)

    url = models.CharField(max_length=300)
    
    
    html = models.BooleanField(
        "HTML",
        default=0,
        blank=False,
    )

    jd = models.BooleanField(
        "Javascript",
        default=0,
        blank=False,
    )
    dj = models.BooleanField(
        "DJango",
        default=0,
        blank=False,
    )
    react = models.BooleanField(
        "React",
        default=0,
        blank=False,
    )

    css = models.BooleanField(
        "CSS",
        default=0,
        blank=False,
    )
    
    


    image = CloudinaryField(
        'image', blank=True, null=False,
    )
