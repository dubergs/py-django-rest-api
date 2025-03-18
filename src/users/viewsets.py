from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .serializer import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsProfileOwnerOrReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
