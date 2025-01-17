from django.db import models
from django.db.models import CharField, DecimalField, IntegerField, TextField, BooleanField, ManyToManyField, BinaryField

from hashlib import sha256

# Create your models here.

class Buyer(models.Model):
    name = CharField(max_length=30)
    password = BinaryField()
    balance = DecimalField(max_digits=10, decimal_places=2)
    age = IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = CharField(max_length=100)
    cost = DecimalField(max_digits=7, decimal_places=2)
    size = DecimalField(decimal_places=0, max_digits=12)
    description = TextField()
    age_limited = BooleanField(default=False)
    buyer = ManyToManyField(related_name='games', to='task1.buyer')

    def __str__(self):
        return self.title

