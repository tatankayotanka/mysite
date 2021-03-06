from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import date


class Task(models.Model):
    """Creates models for Task"""
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
    user = models.ForeignKey(User,default=1)
    assignee = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    created_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        """Gets task URL"""
        return reverse('task:detail', kwargs={'pk':self.pk})

    def create(self):
        """Creates a task"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Returns string representation of a task"""
        return self.title

