from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import fields, serializers
from .models import (Job, ProfilUser, ProfilRetruteur, Competence, Formation, Experience)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash


class LoginSerializer(Serializer):
    """
    Description: Model Description
    """
    username = fields.CharField()
    password = fields.CharField(write_only=True, required=True)
    token = fields.SerializerMethodField()

    def get_token(self, instance: User):
        return Token.objects.get(user=instance).key

    class Meta:
        extra_kwargs = {'password': {"write_only": True}}


class UserSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    password = fields.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):

        validated_data.pop('password')

        for key, value in validated_data.items():

            setattr(instance, key, value)

            instance.save()

        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'email',)
        extra_kwargs = {'password': {"write_only": True}}


