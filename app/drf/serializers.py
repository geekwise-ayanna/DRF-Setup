from django.contrib.auth.models import User, Group
from rest_framework import serializers

class User_Serializers(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups',
        ]

class Group_Serializers(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name',] 