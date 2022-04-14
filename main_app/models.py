from django.db import models
from django.contrib.auth.models import User

# Create your models here.
FAMILY_CHOICES = (
    ('Fr', 'Fringillidae'),
    ('Es', 'Estrildidae'),
    ('Pl', 'Ploceidae'),
    ('Pa', 'Passeridae')
)

class Finch(models.Model):

    name = models.CharField(max_length=20)
    img = models.CharField(max_length=250)
    age = models.IntegerField()
    family = models.CharField(max_length=12, choices = FAMILY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)
class BirdHouse(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
