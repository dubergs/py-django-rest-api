from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
