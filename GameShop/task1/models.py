from django.db import models
from django.db.models import CharField, DecimalField, IntegerField, TextField, BooleanField, ManyToManyField, \
    BinaryField, DateField, DateTimeField, CASCADE

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


class News(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Delivery(models.Model):
    bill_no = models.CharField(max_length=30)
    date = models.DateField()
    vendor = models.ForeignKey(to='task1.vendor', related_name='delivery', on_delete=CASCADE)

    def __str__(self):
        return f'Накладная №{self.bill_no} от {self.date}'

    class Meta:
        managed = False
        db_table = 'task1_delivery'

class DeliveryDet(models.Model):
    delivery = models.ForeignKey(to='delivery', related_name='delivery_det', on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    size = models.DecimalField(max_digits=12, decimal_places=0)
    age_limited = models.BooleanField(blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Игра {self.title} bp накладной Id={self.delivery}'

    class Meta:
        managed = False
        db_table = 'task1_delivery_det'


class Vendor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'task1_vendor'

