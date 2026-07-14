from django.db import models
from django.forms import IntegerField


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"

class Game(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.genre})"


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.title