from django.db import models


class Ci(models.Model):
    value = models.IntegerField(primary_key=True)
    rhythmic = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        """A string representation of the model"""
        return self.rhythmic

    class Meta:
        managed = False
        db_table = 'ci'


class Ciauthor(models.Model):
    value = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    long_desc = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        """A string representation of the model"""
        return self.name

    class Meta:
        managed = False
        db_table = 'ciauthor'
