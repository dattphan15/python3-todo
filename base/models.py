from django.db import models
# from django.conf import settings
from api.models import MyUser
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = [
        ('TODO', 'Todo'),
        ('INPROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
    status = models.CharField(default='TODO', max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
