from rest_framework import serializers
from api import models

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    marks = serializers.IntegerField()

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = models.Article
        fields = '__all__'

