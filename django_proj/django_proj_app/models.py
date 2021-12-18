from django.db import models


class Codex(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Law(models.Model):
    text = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    codex = models.ForeignKey(Codex, on_delete=models.CASCADE)
