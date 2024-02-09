from django.db import models


class Books(models.Model):
    nome = models.CharField(max_length=255)
    password = models.CharField(max_length=255)