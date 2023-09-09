from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField()
    lc_path = models.CharField(max_length=255, default="-")
    base_atk = models.IntegerField()
    base_hp = models.IntegerField()
    base_def = models.IntegerField()
