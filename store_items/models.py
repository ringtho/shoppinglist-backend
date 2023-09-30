from django.db import models
from django.conf import settings


class Order(models.Model):
    """
    Orders Model
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    notes = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
