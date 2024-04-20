import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *

from .validation import ValidationError


# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ



class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(allow_null=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, allow_null=True)
    photo = serializers.CharField()
    team_id = serializers.IntegerField()
    is_captain = serializers.BooleanField()
    password = serializers.CharField(write_only=True)

    extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

        if re.match(pattern, validated_data['password']) is None:
            raise ValidationError('Password has incorrecr format.')

        validated_data['password'] = make_password(validated_data['password'])  # Хешируем пароль
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
