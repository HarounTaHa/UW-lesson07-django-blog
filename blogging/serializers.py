from rest_framework import serializers

from blogging.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PostSerializers(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Post
        fields = '__all__'
