from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experiences')
    title = models.CharField(max_length=300)
    moral = models.CharField(max_length=300)

    def chapter_list(self):
        return Chapter.objects.filter(experience=self)


class Chapter(models.Model):
    experience = models.ForeignKey(Experience, related_name='chapters')
    title = models.CharField(max_length=300)
    body = models.TextField()
