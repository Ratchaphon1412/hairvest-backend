from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

        # def create(self, validated_data):
        #     user_data = validated_data.pop('user')
        #     userProfile = UserProfile.objects.create(**validated_data)

        #     for user in user_data:
        #         User.objects.create(userProfile=userProfile, **user)

        #     return userProfile


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_profile = validated_data.pop('user_profile')

        # instance = User(
        #     name=validated_data['name'], email=validated_data['email'], password=validated_data['password'])

        # instance = User.objects.create(**validated_data)

        # instance.save()

        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        UserProfile.objects.create(
            user=instance, imageProfile=user_profile[0]['imageProfile'])
        # profileImage.save()

        return instance
