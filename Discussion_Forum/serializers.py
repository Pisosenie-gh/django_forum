from rest_framework import serializers
from .models import forum
class forumSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=120)
    email = serializers.CharField()
    topic = serializers.CharField()
    description = serializers.CharField()
    link = serializers.CharField()
    date_created = serializers.DateTimeField()

    def create(self, validated_data):
        return forum.objects.create(**validated_data)