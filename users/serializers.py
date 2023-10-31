from rest_framework import serializers
from .models import User
from characters.serializers import CharacterSerializer


class UserSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "characters"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return super().create(validated_data)
