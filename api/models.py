from django.db import models


class Post(models.Model):
    """
    A reddit post found by the EA-Bot
    """

    class Meta:
        indexes = [
            models.Index(fields=['-hit_or_miss'])
        ]

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


from storages.backends.gcloud import GoogleCloudStorage

storage = GoogleCloudStorage()


class PermalinksFile:
    @staticmethod
    def download_permalinks_file():
        with storage.open('permalinks.txt') as f:
            lines = f.readlines()
            posts = map(lambda l: {'permalink': str(l.strip()), 'hit_or_miss': Post.HitOrMiss.HIT}, lines)

        return list(posts)
