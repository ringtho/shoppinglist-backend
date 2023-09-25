from django.db import models

# Create your models here.

# Model Item


class Item(models.Model):
    # Item Model
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    notes = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    # Orders Model
    # user = models.ForeignKey(
    #     'auth.User', on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
