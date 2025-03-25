from rest_framework import viewsets, status
from .models import House
from .serializers import HouseSerializer
from .permissions import IsHouseManagerOrNone
from rest_framework.decorators import action
from rest_framework.response import Response

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = [IsHouseManagerOrNone, ]
    serializer_class = HouseSerializer

    @action(detail=True, methods=['post'], name='Join')
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if (user_profile.house == None):
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif(user_profile in house.members.all()):
                return Response({'details': 'Already a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'details': 'Already a member in another house'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    @action(detail=True, methods=['post'], name='Leave')
    def leave(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if(user_profile in house.members.all()):
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'details': 'Already a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)