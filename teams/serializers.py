from rest_framework import serializers
from .models import *

# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    banner = serializers.CharField()

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.banner = validated_data.get("banner", instance.banner)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance