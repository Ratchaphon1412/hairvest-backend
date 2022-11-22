from rest_framework import serializers
from .models import User, UserProfile
from django.core.files.storage import default_storage


class UserSerializer(serializers.ModelSerializer):
    # user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True},
                        }

    def create(self, validated_data):

        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)

        if password is not None:
            print(password)
            instance.set_password(password)
        instance.save()

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"
