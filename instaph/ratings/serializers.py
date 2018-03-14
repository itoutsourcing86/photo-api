from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Photo


class UserSerializer(serializers.ModelSerializer):
    photos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='photo-detail')
    total_photos = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'total_photos', 'photos')


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    total_votes = serializers.IntegerField(read_only=True)
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Photo
        fields = ('owner', 'url', 'image', 'total_votes', 'average_rating')