from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField()
    lc_path = models.CharField(max_length=255, null=True)
    base_atk = models.IntegerField()
    base_hp = models.IntegerField()
    base_def = models.IntegerField()
