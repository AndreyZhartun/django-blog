from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # TODO images

    def __str__(self):
        return self.title