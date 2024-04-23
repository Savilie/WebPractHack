from rest_framework import serializers
from .models import *

# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    banner = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.banner = validated_data.get("banner", instance.banner)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance