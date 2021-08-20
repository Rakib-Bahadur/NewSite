from django.db import models
from django.db.models import UniqueConstraint


class Source(models.Model):
    source_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["source_id", "name"],
                             name="source_unique"),
        ]


class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=1000)
    url_to_image = models.CharField(max_length=1000, null=True)
    published_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["source", "title", "url"],
                             name="article_unique"),
        ]
