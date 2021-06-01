from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    objects = models.manager

    def __str__(self):
        return self.title
