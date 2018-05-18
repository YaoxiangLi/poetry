from rest_framework import serializers
from . import models


class CiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'value',
            'rhythmic',
            'author',
            'content',
        )
        model = models.Ci


class CiauthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'value',
            'name',
            'long_desc',
            'short_desc',
        )
        model = models.Ciauthor