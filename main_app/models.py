from django.db import models

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

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']