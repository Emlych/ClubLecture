from django.db import models
from django.utils import timezone


class Article(models.Model):
    auteur = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    date_pulication = models.DateTimeField(blank=True, null=True)

    def publier(self):
        self.date_pulication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre
