from django.db import models


class FlashCard(models.Model):
    category = models.CharField(default='', max_length=50)
    cue = models.CharField(default='', max_length=50)
    cue_expanded = models.CharField(default='', max_length=100)
    info = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.cue
