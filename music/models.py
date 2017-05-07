from django.db import models
from django.utils import timezone


class Task(models.Model):
    NOTSTARTED = 'NS'
    INPROGRESS = 'IP'
    FINISHED = 'FIN'
    PROGRESS_CHOICES = (
        (NOTSTARTED, 'Not Started'),
        (INPROGRESS, 'In Progress'),
        (FINISHED, 'F'),
    )
    progress = models.CharField(
        max_length=2,
        choices=PROGRESS_CHOICES,
        default=NOTSTARTED,inished
    )
    assignee = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    deadline = models.DateTimeField(
            default=timezone.now)
    created_date = models.DateTimeField(
        blank=True, null=True)

    def create(self):
      self.published_date = timezone.now()
      self.save()

    def __str__(self):
      return self.title




# Create your models here.
