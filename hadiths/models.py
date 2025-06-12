from django.db import models

class Hadith(models.Model):
    person = models.CharField(max_length=255)
    text = models.TextField()
    source = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.person[:30]} - {self.text[:50]}"
