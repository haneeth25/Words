from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.word