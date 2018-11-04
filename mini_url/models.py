from django.db import models
from django.utils import timezone
import random
import string


# Create your models here.
class MiniURL(models.Model):
    url = models.CharField(max_length=100, verbose_name="url", unique=True)
    code = models.CharField(max_length=6, unique=True, verbose_name="code")
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='creation date')
    pseudo = models.CharField(max_length=255, verbose_name="pseudo")
    count_access = models.IntegerField(default=0, verbose_name="access counter")

    class Meta:
        verbose_name = "mini_URL"
        ordering = ['creation_date']

    def __str__(self):
        return "{0] {1}".format(self.code, self.url)

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        return ''.join(aleatoire)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.code = self.generer(6)
        super(MiniURL, self).save(*args, **kwargs)
