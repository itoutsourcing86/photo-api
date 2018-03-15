from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PhotoSerializer, RatingSerializer
from .models import Photo, Rating
from django.db.models import Avg, Count
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def get_queryset(self):
        return User.objects.annotate(
            total_photos=Count('photos__image'),
        )


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, ]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return Photo.objects.annotate(
            total_votes=Count('ratings'),
            average_rating=Avg('ratings__rating'),
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    http_method_names = ['post', 'get']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
