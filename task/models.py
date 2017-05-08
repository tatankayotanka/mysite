from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import date


class Task(models.Model):
    NOTSTARTED = 'Not Started'
    INPROGRESS = 'In Progress'
    FINISHED = 'Finished'
    PROGRESS_CHOICES = (
        (NOTSTARTED, 'Not Started'),
        (INPROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    )
    progress = models.CharField(
        max_length=20,
        choices=PROGRESS_CHOICES,
        default=NOTSTARTED,
    )

    assignee = models.CharField(max_length=250)
   # assignee = models.ForeignKey('auth.User',default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    deadline = models.DateField()
    created_date = models.DateTimeField(
        blank=True, null=True)

    def get_absolute_url(self):
        return reverse('task:detail', kwargs={'pk':self.pk})

    def create(self):
      self.published_date = timezone.now()
      self.save()

    def __str__(self):
      return self.title




# Create your models here.
