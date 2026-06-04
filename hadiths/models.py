from django.db import models

class Hadith(models.Model):
    arabic_text = models.TextField()
    persian_text = models.TextField()
