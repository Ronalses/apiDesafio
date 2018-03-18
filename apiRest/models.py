from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

# These models do not validate :/


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, default='user')
    lastname = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('id', )


class Task(models.Model):
    POSSIBLE_STATES = (
        (0, 'Pending'),
        (1, 'In process'),
        (2, 'Finished'),
    )

    title = models.CharField(max_length=100, blank=False, default="New Task")
    status = models.IntegerField(default=0, choices=POSSIBLE_STATES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )
