from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In progress'
        PROCRASTINATED = 'procrastinated', 'Procrastinated'
        CANCELED = 'canceled', 'Canceled'
        DONE = 'done', 'Done'

    class Priority(models.IntegerChoices):
        TRIVIAL = 1
        MINOR = 2
        MAJOR = 3
        CRITICAL = 4
        BLOCKER = 5

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.NEW,
    )
    priority = models.SmallIntegerField(
        choices=Priority.choices,
        default=Priority.MAJOR,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
