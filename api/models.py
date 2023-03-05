from django.db import models


class Post(models.Model):
    """
    A reddit post found by the EA-Bot
    """

    class HitOrMiss(models.TextChoices):
        """
        Used to label posts ass hit or miss
        """
        HIT = 'H', 'Hit'
        MISS = 'M', 'Miss'

    permalink = models.CharField(max_length=500)
    hit_or_miss = models.CharField(max_length=2,
                                   choices=HitOrMiss.choices,
                                   default=HitOrMiss.HIT)

    def __str__(self):
        return self.permalink
